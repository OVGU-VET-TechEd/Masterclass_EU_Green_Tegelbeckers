"""The student-email task used by lab 6 and by the harness.

A task is a folder:

  task.json                  signature, word limit, categories and their handling
  spec.md                    the specification (the standing instruction)
  context/*.md               reference documents
  inputs/*.txt               the emails to be answered
  example_approved_answer.md an answer entry used by lab 6 in place of a person

Processing one email takes these steps:

  1 classify  the model assigns one category from task.json
  2 draft     the model writes a reply, given the specification, the reference
              documents and the handling rule for that category
  3 check     check_email tests the reply against seven rules    (stage 4)
  4 revise    failed checks are returned to the model, up to a
              fixed number of rounds                             (stage 4)
  5 route     the reply goes to 'ready' or 'review'

The wiki (stage 5) is a Markdown file read before and extended after a run.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .backend import Backend
from .checks import EMAIL_LESSONS, all_passed, check_email, language

TASKS_DIR = pathlib.Path(__file__).parent / "tasks"
MAX_TOKENS = 320


@dataclass
class Task:
    name: str
    path: pathlib.Path
    title: str
    spec: str
    context: List[Tuple[str, str]]
    inputs: List[Tuple[str, str]]
    signature: str
    signature_pattern: str
    max_words: int
    open_phrases: List[str]
    categories: Dict[str, Dict[str, Any]]
    approved_example: str

    @property
    def context_text(self) -> str:
        return "\n\n".join(text.strip() for _, text in self.context)

    def input(self, name: str) -> str:
        return dict(self.inputs)[name]


def resolve(name_or_path: str) -> pathlib.Path:
    p = pathlib.Path(name_or_path)
    if (p / "task.json").exists():
        return p
    if (TASKS_DIR / name_or_path / "task.json").exists():
        return TASKS_DIR / name_or_path
    raise SystemExit("No task folder at %s (expected a task.json in it)." % name_or_path)


def load_task(name_or_path: str = "student_emails") -> Task:
    path = resolve(name_or_path)
    cfg = json.loads((path / "task.json").read_text(encoding="utf-8"))

    def read_dir(sub: str, suffixes: Iterable[str]) -> List[Tuple[str, str]]:
        d = path / sub
        if not d.is_dir():
            return []
        return [(f.name, f.read_text(encoding="utf-8"))
                for f in sorted(d.iterdir()) if f.suffix.lower() in suffixes]

    example = path / "example_approved_answer.md"
    return Task(
        name=path.name,
        path=path,
        title=cfg.get("title", path.name),
        spec=(path / "spec.md").read_text(encoding="utf-8"),
        context=read_dir("context", {".md", ".txt"}),
        inputs=read_dir("inputs", {".md", ".txt"}),
        signature=cfg["signature"],
        signature_pattern=cfg.get("signature_pattern", re.escape(cfg["signature"])),
        max_words=int(cfg.get("max_words", 150)),
        open_phrases=cfg.get("open_question_phrases", []),
        categories=cfg["categories"],
        approved_example=example.read_text(encoding="utf-8").strip() if example.exists() else "",
    )


# -------------------------------------------------------------------- prompts

CLASSIFY_TEMPLATE = (
    "Classify the email below into exactly one of these categories.\n\n"
    "{categories}\n\n"
    "Email:\n\n{email}\n\n"
    "Answer with the category name only."
)

DRAFT_TEMPLATE = (
    "Category: {label} ({description})\n"
    "Handling rule for this category: {handling}\n\n"
    "Email:\n\n{email}\n\n"
    "Write the reply. Output only the reply text."
)

REVISE_TEMPLATE = (
    "Category: {label}\n\n"
    "Email:\n\n{email}\n\n"
    "Your draft reply:\n\n{draft}\n\n"
    "The draft did not pass these checks:\n{failures}\n\n"
    "Revise the reply so that it passes these checks. Keep everything that is "
    "correct. Output only the revised reply."
)


def classify_prompt(task: Task, email: str) -> str:
    cats = "\n".join("- %s: %s" % (k, v["description"]) for k, v in task.categories.items())
    return CLASSIFY_TEMPLATE.format(categories=cats, email=email.strip())


def parse_category(task: Task, answer: str) -> str:
    """The first category name in the answer; 'other' if there is none."""
    norm = re.sub(r"[\s-]+", "_", answer.lower())
    hits = [(m.start(), k) for k in task.categories for m in [re.search(r"\b%s\b" % k, norm)] if m]
    return min(hits)[1] if hits else ("other" if "other" in task.categories else next(iter(task.categories)))


def draft_prompt(task: Task, email: str, label: str) -> str:
    c = task.categories[label]
    return DRAFT_TEMPLATE.format(label=label, description=c["description"],
                                 handling=c["handling"], email=email.strip())


def system_prompt(task: Task, lessons: Iterable[str] = (), approved: Iterable[str] = ()) -> str:
    parts = [task.spec.strip(), "Reference documents:\n\n" + task.context_text]
    approved, lessons = list(approved), list(lessons)
    if approved:
        parts.append("Approved answers (written by the module team; use them as reference "
                     "documents):\n" + "\n".join("- " + a for a in approved))
    if lessons:
        parts.append("Lessons recorded from earlier runs:\n" + "\n".join("- " + l for l in lessons))
    return "\n\n".join(parts)


# ------------------------------------------------------------ checks, routing

def run_checks(task: Task, reply: str, email: str, label: str,
               approved: Iterable[str] = ()) -> List[Dict[str, Any]]:
    sources = task.context_text + "\n" + "\n".join(approved)
    return check_email(reply, email, sources, bool(task.categories[label].get("refer")),
                       task.signature_pattern, task.max_words,
                       open_question=has_open_question(task, reply),
                       topic_required=task.categories[label].get("route") == "auto")


def has_open_question(task: Task, reply: str) -> bool:
    low = reply.lower()
    return any(p.lower().rstrip(".") in low for p in task.open_phrases)


def route(task: Task, label: str, checks: List[Dict[str, Any]], reply: str,
          checked: bool) -> Tuple[str, str]:
    """'ready' or 'review', with the reason."""
    if task.categories[label].get("route") == "human":
        return "review", "category '%s' is always reviewed by a person" % label
    if has_open_question(task, reply):
        return "review", "the sources do not answer the question (open question)"
    if not checked:
        return "ready", "category handled automatically; reply not checked"
    if not all_passed(checks):
        failed = [c["id"] for c in checks if not c["ok"]]
        return "review", "checks failed: " + ", ".join(failed)
    return "ready", "category handled automatically; all checks passed"


def lessons_for(checks: List[Dict[str, Any]]) -> List[str]:
    return [EMAIL_LESSONS[c["id"]] for c in checks if not c["ok"] and c["id"] in EMAIL_LESSONS]


def subject(email: str) -> str:
    m = re.search(r"^(?:Subject|Betreff):\s*(.+)$", email, re.M)
    return (m.group(1) if m else email.strip().splitlines()[0])[:90].strip()


def failures_text(checks: List[Dict[str, Any]]) -> str:
    return "\n".join(
        "- %s. %s%s" % (c["rule"], EMAIL_LESSONS.get(c["id"], ""),
                        " (found: %s)" % c["detail"] if c.get("detail") else "")
        for c in checks if not c["ok"]
    )


# ----------------------------------------------------------------- pipeline

def draft(backend: Backend, task: Task, name: str, email: str, system: str,
          label: Optional[str] = None, approved: Iterable[str] = (),
          seed: int = 42, max_tokens: int = MAX_TOKENS) -> Dict[str, Any]:
    """Steps 1 and 2. If `label` is given, classification is skipped."""
    approved = list(approved)
    rec: Dict[str, Any] = {"name": name, "email": email, "language": language(email)}
    if label is None:
        cp = classify_prompt(task, email)
        c = backend.generate(cp, temperature=0.0, seed=seed, max_tokens=12)
        label = parse_category(task, c.text)
        rec.update(classify_prompt=cp, classify_answer=c.text)
    rec["category"] = label
    dp = draft_prompt(task, email, label)
    r = backend.generate(dp, system=system, temperature=0.0, seed=seed, max_tokens=max_tokens)
    rec.update(model=r.model, endpoint=r.endpoint, simulated=r.simulated, system=system)
    rec["rounds"] = [{"round": 1, "prompt": dp, "text": r.text,
                      "checks": run_checks(task, r.text, email, label, approved)}]
    return finish(task, rec, checked=False)


def loop(backend: Backend, task: Task, rec: Dict[str, Any], rounds: int,
         approved: Iterable[str] = (), seed: int = 42, max_tokens: int = MAX_TOKENS) -> Dict[str, Any]:
    """Steps 3 and 4: check, revise what failed, check again.

    Stops when all checks pass, when the reply contains an open question (a
    revision cannot supply missing information), or after `rounds` rounds in
    total, counting the first draft.
    """
    approved = list(approved)
    while len(rec["rounds"]) < rounds:
        last = rec["rounds"][-1]
        if all_passed(last["checks"]) or has_open_question(task, last["text"]):
            break
        rp = REVISE_TEMPLATE.format(label=rec["category"], email=rec["email"].strip(),
                                    draft=last["text"], failures=failures_text(last["checks"]))
        r = backend.generate(rp, system=rec["system"], temperature=0.0, seed=seed,
                             max_tokens=max_tokens)
        rec["rounds"].append({"round": len(rec["rounds"]) + 1, "prompt": rp, "text": r.text,
                              "checks": run_checks(task, r.text, rec["email"], rec["category"], approved)})
    rec["max_rounds"] = rounds
    return finish(task, rec, checked=True)


def finish(task: Task, rec: Dict[str, Any], checked: bool) -> Dict[str, Any]:
    last = rec["rounds"][-1]
    rec["text"], rec["checks"] = last["text"], last["checks"]
    rec["open_question"] = has_open_question(task, last["text"])
    rec["route"], rec["reason"] = route(task, rec["category"], last["checks"], last["text"], checked)
    return rec


# ---------------------------------------------------------------------- wiki

SECTIONS = ("Lessons from failed checks", "Open questions", "Approved answers")

WIKI_PREAMBLE = (
    "# Wiki: {title}\n\n"
    "The harness reads this file at the start of every run and adds entries at the end.\n\n"
    "- 'Lessons from failed checks' is written by the harness. Each line is added to\n"
    "  the instructions of later runs. Edit or delete lines as required.\n"
    "- 'Open questions' is written by the harness. It lists emails the sources could\n"
    "  not answer. Delete an entry once it has been answered.\n"
    "- 'Approved answers' is written by people only. Each line is used as a reference\n"
    "  document in later runs. The harness never writes to this section.\n"
)


def read_wiki(path: Optional[pathlib.Path]) -> Dict[str, List[str]]:
    """Entries per section, without the date comment each one carries."""
    out: Dict[str, List[str]] = {s: [] for s in SECTIONS}
    if not path or not path.exists():
        return out
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip() if line[3:].strip() in out else None
        elif current and line.startswith("- "):
            entry = re.sub(r"\s*<!--.*?-->\s*$", "", line[2:]).strip()
            if entry:
                out[current].append(entry)
    return out


def render_wiki(task: Task, wiki: Dict[str, List[str]], dated: Optional[Dict[str, str]] = None) -> str:
    dated = dated or {}
    lines = [WIKI_PREAMBLE.format(title=task.title)]
    for s in SECTIONS:
        lines.append("## %s\n" % s)
        for e in wiki.get(s, []):
            lines.append("- %s%s" % (e, "  <!-- added %s -->" % dated[e] if e in dated else ""))
        lines.append("")
    return "\n".join(lines)


def update_wiki(path: pathlib.Path, task: Task, lessons: Iterable[str],
                open_questions: Iterable[str]) -> Tuple[int, int]:
    """Append new lessons and open questions; leave approved answers untouched.

    Rewrites the file from its parsed sections, so the date comments of
    existing entries are kept by re-reading them first.
    """
    today = datetime.date.today().isoformat()
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    dated = {}
    for line in text.splitlines():
        m = re.match(r"- (.*?)\s*<!-- added (\S+) -->\s*$", line)
        if m:
            dated[m.group(1).strip()] = m.group(2)
    wiki = read_wiki(path)
    added = [0, 0]
    for i, (section, new) in enumerate((("Lessons from failed checks", lessons),
                                        ("Open questions", open_questions))):
        for e in new:
            if e not in wiki[section]:
                wiki[section].append(e)
                dated[e] = today
                added[i] += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_wiki(task, wiki, dated), encoding="utf-8")
    return added[0], added[1]


def open_question_entry(rec: Dict[str, Any]) -> str:
    return '%s: "%s"' % (rec["name"], subject(rec["email"]))
