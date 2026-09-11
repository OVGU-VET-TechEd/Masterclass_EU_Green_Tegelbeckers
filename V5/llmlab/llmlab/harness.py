"""Stages three to five of the prompting evolution, as one command.

Stage three, the harness prompt: one specification file, one folder of inputs,
one output file per input, each carrying a record of how it was produced.
Nothing here is clever. That is the argument: the difference between stage one
and stage three is not sophistication, it is that this leaves a trail.

Stage four, `--loop N`: each output is checked against the five written
feedback rules and revised until it meets them, N rounds at most. The header
records every round.

Stage five, `--wiki FILE`: rules an input's first draft missed become lines in
a plain markdown file, and every later run reads that file into its
instructions. The model does not change; the file does. Open it, edit it,
delete a line — that is the whole of what the system "learned".

The loop and the wiki use the feedback checks from labs.py, so they fit
specifications like examples/feedback_spec.md and not arbitrary ones.
"""

from __future__ import annotations

import datetime
import pathlib
import re
from typing import List, Optional

from .backend import Backend
from .labs import check_feedback, lessons_for, revise_until_met

SUFFIXES = {".md", ".txt"}

WIKI_HEADER = (
    "# Wiki — lessons llmlab wrote after its own mistakes\n\n"
    "Every run with --wiki reads this file into its instructions. Edit or delete "
    "any line; the next run will follow what is here, and nothing else.\n\n"
)


def read_wiki(path: pathlib.Path) -> List[str]:
    """The lesson lines, without the date comment each one carries."""
    if not path.exists():
        return []
    return [
        re.sub(r"\s*<!--.*?-->\s*$", "", l[2:]).strip()
        for l in path.read_text(encoding="utf-8").splitlines()
        if l.startswith("- ")
    ]


def _lessons(n: int) -> str:
    return "%d lesson%s" % (n, "" if n == 1 else "s")


def run_harness(
    backend: Backend,
    spec_path: str,
    inputs_dir: str,
    out_dir: str,
    temperature: float = 0.0,
    seed: int = 42,
    max_tokens: int = 400,
    loop: int = 0,
    wiki_path: Optional[str] = None,
    log: Optional[List[str]] = None,
) -> List[str]:
    spec = pathlib.Path(spec_path).read_text(encoding="utf-8")
    in_dir = pathlib.Path(inputs_dir)
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in in_dir.iterdir() if p.suffix.lower() in SUFFIXES)
    if not files:
        raise SystemExit("No .md or .txt files in %s" % in_dir)

    wiki = pathlib.Path(wiki_path) if wiki_path else None
    lessons = read_wiki(wiki) if wiki else []
    system = spec
    if lessons:
        system += "\n\nLessons from earlier runs:\n" + "\n".join("- " + l for l in lessons)
    added: List[str] = []

    written = []
    for p in files:
        body = p.read_text(encoding="utf-8")
        r = backend.generate(
            body, system=system, temperature=temperature, seed=seed, max_tokens=max_tokens
        )
        text, header_extra = r.text, []
        if loop or wiki:
            rounds = revise_until_met(backend, system, r.text, max(1, int(loop)),
                                      seed=seed, max_tokens=max_tokens)
            text = rounds[-1]["text"]
            scores = " → ".join("%d/5" % sum(c["ok"] for c in e["checks"]) for e in rounds)
            if loop:
                header_extra.append("  loop:        %d of %d rounds used  (checks %s)"
                                    % (len(rounds), int(loop), scores))
            if wiki:
                for lesson in lessons_for(rounds[0]["checks"]):
                    if lesson not in lessons and lesson not in added:
                        added.append(lesson)
            if log is not None:
                log.append("%s: %s" % (p.name, scores))
        if wiki:
            header_extra.append("  wiki:        %s  (%s read)" % (wiki.name, _lessons(len(lessons))))
        stamp = datetime.datetime.now().isoformat(timespec="seconds")
        target = out / (p.stem + ".out.md")
        target.write_text(
            "\n".join(
                [
                    "<!--",
                    "  produced by llmlab harness",
                    "  input:       %s" % p.name,
                    "  spec:        %s" % pathlib.Path(spec_path).name,
                    "  model:       %s" % r.model,
                    "  endpoint:    %s" % r.endpoint,
                    "  temperature: %s   seed: %s" % (temperature, seed),
                    *header_extra,
                    "  simulated:   %s" % r.simulated,
                    "  produced:    %s" % stamp,
                    "-->",
                    "",
                    text,
                    "",
                ]
            ),
            encoding="utf-8",
        )
        written.append(str(target))

    if wiki:
        today = datetime.date.today().isoformat()
        if not wiki.exists():
            wiki.write_text(WIKI_HEADER, encoding="utf-8")
        if added:
            with wiki.open("a", encoding="utf-8") as f:
                for lesson in added:
                    f.write("- %s  <!-- added %s -->\n" % (lesson, today))
        if log is not None:
            log.append("wiki %s: %s read, %d added" % (wiki, _lessons(len(lessons)), len(added)))
    return written
