"""Stages three to five of prompting, as one command.

  llmlab harness --task student_emails --out out                         stage 3
  llmlab harness --task student_emails --out out --loop 3                stage 4
  llmlab harness --task student_emails --out out --loop 3 --wiki wiki.md stage 5

Stage 3 classifies and drafts a reply for every email in the task's inputs
folder, writes each reply to out/ready/ or out/review/ with a provenance
header, and writes out/log.md. Routing depends on the category.

Stage 4 (--loop N) checks every draft and requests revisions until all checks
pass or N rounds are used. Routing then also depends on the checks.

Stage 5 (--wiki FILE) reads lessons and approved answers from FILE before the
run and appends lessons and open questions after it. The section 'Approved
answers' is never written by the harness.
"""

from __future__ import annotations

import datetime
import pathlib
from typing import Any, Dict, List, Optional

from . import tasks
from .backend import Backend
from .checks import score


def _header(rec: Dict[str, Any], task: tasks.Task, loop: int, wiki_info: str,
            seed: int, stamp: str) -> str:
    rounds = rec["rounds"]
    if loop:
        checks = "%s  (%d of %d rounds)" % (" → ".join(score(r["checks"]) for r in rounds),
                                           len(rounds), loop)
    else:
        checks = "%s  (evaluated, not used for routing; use --loop to apply them)" % score(rec["checks"])
    failed = ", ".join(c["id"] for c in rec["checks"] if not c["ok"]) or "none"
    lines = [
        "<!--",
        "  produced by   llmlab harness",
        "  task         %s" % task.name,
        "  input        %s" % rec["name"],
        "  category     %s%s" % (rec["category"],
                                 "  (model answer: %r)" % rec["classify_answer"].strip()[:40]
                                 if rec.get("classify_answer") is not None else ""),
        "  route        %s: %s" % (rec["route"], rec["reason"]),
        "  checks       %s" % checks,
        "  failed       %s" % failed,
    ]
    if wiki_info:
        lines.append("  wiki         %s" % wiki_info)
    lines += [
        "  model        %s" % rec["model"],
        "  endpoint     %s" % rec["endpoint"],
        "  temperature  0.0   seed %s" % seed,
        "  simulated    %s" % rec["simulated"],
        "  produced     %s" % stamp,
        "-->",
        "",
    ]
    return "\n".join(lines)


def run_harness(
    backend: Backend,
    task_ref: str,
    out_dir: str,
    loop: int = 0,
    wiki_path: Optional[str] = None,
    limit: Optional[int] = None,
    seed: int = 42,
    log: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    task = tasks.load_task(task_ref)
    out = pathlib.Path(out_dir)
    for sub in ("ready", "review"):
        (out / sub).mkdir(parents=True, exist_ok=True)
        for old in (out / sub).glob("*.reply.md"):
            old.unlink()  # replies from an earlier run would otherwise remain in the wrong folder

    wiki = pathlib.Path(wiki_path) if wiki_path else None
    w = tasks.read_wiki(wiki)
    lessons, approved = w["Lessons from failed checks"], w["Approved answers"]
    system = tasks.system_prompt(task, lessons, approved)
    wiki_info = ("%s: %d lessons, %d approved answers read" % (wiki.name, len(lessons), len(approved))
                 if wiki else "")

    inbox = task.inputs[: int(limit)] if limit else task.inputs
    if not inbox:
        raise SystemExit("No .txt or .md files in %s" % (task.path / "inputs"))
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    records = []
    for name, email in inbox:
        rec = tasks.draft(backend, task, name, email, system, approved=approved, seed=seed)
        if loop:
            rec = tasks.loop(backend, task, rec, int(loop), approved=approved, seed=seed)
        target = out / rec["route"] / (pathlib.Path(name).stem + ".reply.md")
        target.write_text(_header(rec, task, int(loop), wiki_info, seed, stamp) + rec["text"] + "\n",
                          encoding="utf-8")
        rec["file"] = str(target)
        records.append(rec)
        if log is not None:
            log.append("%-24s %-12s %-18s %s" % (name, rec["category"],
                                                 " → ".join(score(r["checks"]) for r in rec["rounds"]),
                                                 rec["route"]))

    if wiki:
        new_lessons = []
        for rec in records:
            for l in tasks.lessons_for(rec["rounds"][0]["checks"]):
                if l not in new_lessons:
                    new_lessons.append(l)
        new_open = [tasks.open_question_entry(r) for r in records if r["open_question"]]
        added_l, added_o = tasks.update_wiki(wiki, task, new_lessons, new_open)
        if log is not None:
            log.append("wiki %s: %d lessons and %d approved answers read; %d lessons and "
                       "%d open questions added" % (wiki, len(lessons), len(approved), added_l, added_o))

    rows = ["| email | category | checks per round | route | reason |",
            "| --- | --- | --- | --- | --- |"]
    rows += ["| %s | %s | %s | %s | %s |" % (r["name"], r["category"],
                                            " → ".join(score(x["checks"]) for x in r["rounds"]),
                                            r["route"], r["reason"]) for r in records]
    (out / "log.md").write_text(
        "# Harness log\n\n"
        "- task: %s\n- model: %s (%s)\n- simulated: %s\n- loop: %s\n- wiki: %s\n- produced: %s\n\n%s\n"
        % (task.name, backend.model, backend.endpoint, backend.simulated,
           "%d rounds at most" % loop if loop else "off", wiki_info or "off", stamp, "\n".join(rows)),
        encoding="utf-8")
    return records
