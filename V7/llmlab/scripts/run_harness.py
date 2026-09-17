"""Stages 3 to 5 on the student-email task, with files written.

Run from the folder V6/llmlab:

    python scripts/run_harness.py --stage 3
    python scripts/run_harness.py --stage 4 --rounds 3
    python scripts/run_harness.py --stage 5 --rounds 3 --out-dir results/harness

Output in DIR (default results/harness):
  ready/*.reply.md, review/*.reply.md   one reply per email with provenance header
  log.md                                table of categories, checks and routes
  wiki.md                               stage 5 only; edit 'Approved answers' and run again
  run.json                              every record: prompts, rounds, checks, route
"""

import argparse
import json
import pathlib

from _runner import be, header
from llmlab.harness import run_harness


def main() -> int:
    ap = argparse.ArgumentParser(description="Stages 3 to 5 of prompting on a folder of emails.")
    ap.add_argument("--stage", type=int, choices=[3, 4, 5], default=5)
    ap.add_argument("--rounds", type=int, default=3, help="maximum rounds at stages 4 and 5")
    ap.add_argument("--task", default="student_emails", help="built-in task name or path to a task folder")
    ap.add_argument("--limit", type=int, default=None, help="process the first N emails only")
    ap.add_argument("--out-dir", default="results/harness")
    ap.add_argument("--model", default=None)
    ap.add_argument("--backend", default="auto", choices=["auto", "ollama", "openai", "simulated"])
    args = ap.parse_args()

    b = be.detect(args.model, prefer=args.backend)
    print(header(b))
    out = pathlib.Path(args.out_dir)
    log = []
    records = run_harness(b, args.task, str(out),
                          loop=args.rounds if args.stage >= 4 else 0,
                          wiki_path=str(out / "wiki.md") if args.stage == 5 else None,
                          limit=args.limit, log=log)
    print("\n    %-24s %-12s %-18s %s" % ("email", "category", "checks per round", "route"))
    for line in log:
        print("    " + line)
    (out / "run.json").write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nwritten: %s (ready/, review/, log.md%s, run.json)" % (out, ", wiki.md" if args.stage == 5 else ""))
    for r in records:
        print("\n--- %s · %s · %s (%s)\n%s" % (r["name"], r["category"], r["route"], r["reason"], r["text"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
