"""Command line entry point: python -m llmlab <command>"""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import sys
import textwrap

from . import __version__, backend as be, labs, tasks
from .harness import run_harness

W = 88


def wrap(text: str, indent: str = "  ") -> str:
    out = []
    for para in (text or "").split("\n"):
        if not para.strip():
            out.append("")
        else:
            out.append(textwrap.fill(para, W, initial_indent=indent, subsequent_indent=indent,
                                     replace_whitespace=False, drop_whitespace=True))
    return "\n".join(out)


def block(text: str, indent: str = "    ", full: bool = False, head: int = 14, tail: int = 4) -> str:
    """Preformatted text, shortened in the middle unless `full`."""
    lines = (text or "").strip("\n").split("\n")
    if not full and len(lines) > head + tail + 2:
        lines = lines[:head] + ["[... %d lines omitted; use --full to print everything ...]"
                                % (len(lines) - head - tail)] + lines[-tail:]
    return "\n".join(textwrap.fill(l, W, initial_indent=indent, subsequent_indent=indent)
                     if l.strip() else "" for l in lines)


def rule(char: str = "-") -> str:
    return char * W


def table(t: dict, indent: str = "    ") -> str:
    cols, rows = t["columns"], [[str(c) for c in r] for r in t["rows"]]
    widths = [min(34, max(len(str(c)) for c in [h] + [r[i] for r in rows])) for i, h in enumerate(cols)]
    fmt = lambda cells: indent + "  ".join(str(c)[:w].ljust(w) for c, w in zip(cells, widths))
    return "\n".join([fmt(cols), indent + "  ".join("-" * w for w in widths)] + [fmt(r) for r in rows])


def cmd_check(args) -> int:
    s = be.survey()
    print(rule("="))
    print("  llmlab %s" % __version__)
    print(rule("="))
    print("  Python   %s  on  %s %s"
          % (platform.python_version(), platform.system(), platform.release()))
    for key, label in (("ollama", "Ollama"), ("openai", "OpenAI-compatible server")):
        info = s[key]
        state = "reachable" if info["up"] else "not reachable"
        print("  %-24s %-14s %s" % (label, state, info["endpoint"]))
        if info["up"]:
            models = info["models"] or []
            print("  %-24s %s" % ("", ", ".join(models) if models else "no models installed"))
    print(rule())
    b = be.detect(args.model)
    if b.simulated:
        print(wrap(
            "No model service is reachable, so llmlab will run in simulated mode: the texts "
            "are produced by llmlab, not by a model, and every result is marked as simulated. "
            "To use a model, install Ollama (https://ollama.com), run `ollama pull gemma3:4b` "
            "and repeat this command."))
    else:
        print(wrap("Backend: %s, model %s, at %s" % (b.name, b.model, b.endpoint)))
    print(rule())
    return 0


def print_run(run: dict, full: bool) -> None:
    print()
    print("  " + rule("-")[2:])
    meta = []
    if run.get("prompt_tokens") and run.get("wrapper_tokens"):
        meta.append("%d text tokens + %d template tokens" % (run["prompt_tokens"], run["wrapper_tokens"]))
    elif run.get("prompt_tokens"):
        meta.append("%d prompt tokens" % run["prompt_tokens"])
    if run.get("output_tokens"):
        meta.append("%d output tokens" % run["output_tokens"])
    if run.get("seconds"):
        meta.append("%.2f s" % run["seconds"])
    if run.get("correct") is not None:
        meta.append("date found" if run["correct"] else "date not found")
    print("  [%s]%s" % (run.get("label", ""), "   " + " · ".join(meta) if meta else ""))
    if run.get("settings"):
        print(wrap("settings: " + ", ".join("%s %s" % kv for kv in run["settings"].items()), "    "))
    if run.get("artefact"):
        print(wrap("artefact: " + run["artefact"], "    "))
    if run.get("system"):
        print("    system prompt:")
        print(block(run["system"], "      ", full, head=8, tail=2))
    if run.get("prompt"):
        print("    user message:")
        print(block(run["prompt"], "      ", full, head=10, tail=4))
    if run.get("chips"):
        print(wrap("approximate segmentation: " + " | ".join(run["chips"][:60])
                   + (" ..." if len(run["chips"]) > 60 else ""), "    "))
    if run.get("text"):
        print("    output:")
        print(block(run["text"], "      ", True))
    if run.get("checks"):
        missed = [c for c in run["checks"] if not c["ok"]]
        print(wrap("checks: %d of %d passed%s" % (
            len(run["checks"]) - len(missed), len(run["checks"]),
            "; failed: " + "; ".join(c["rule"] + (" (%s)" % c["detail"] if c.get("detail") else "")
                                     for c in missed) if missed else ""), "    "))
    if run.get("table"):
        print()
        print(table(run["table"]))
    for f in run.get("files") or []:
        print()
        print("    file: %s" % f["name"])
        print(block(f["text"], "      ", True))
    for item in run.get("items") or []:
        print()
        print("    > %s" % item["label"])
        for b in item["blocks"]:
            if not full and b["label"].split(" · ")[-1].startswith(("classification prompt", "drafting prompt", "revision prompt")):
                continue
            print("      %s:" % b["label"])
            print(block(b["text"], "        ", full, head=8, tail=3))
    for n in run.get("notes") or []:
        print(wrap("· " + n, "    "))


def print_result(res: dict, full: bool = False, brief: bool = False) -> None:
    print()
    print(rule("="))
    print("  %s" % res["title"])
    print("  %s" % res.get("block", ""))
    print(rule("="))
    print(wrap("Aim: " + res["aim"]))
    if not brief:
        print()
        print("  Background")
        for para in res["background"]:
            print(wrap(para, "    "))
            print()
        print("  Procedure")
        for i, step in enumerate(res["procedure"], 1):
            print(textwrap.fill(step, W, initial_indent="    %d. " % i, subsequent_indent="       "))
        if res.get("materials"):
            print()
            print("  Materials")
            for m in res["materials"]:
                print("    %s:" % m["label"])
                print(block(m["text"], "      ", full, head=16, tail=4))
    if res.get("simulated"):
        print()
        print(wrap("SIMULATED MODE: no model was called. The texts below were produced by "
                   "llmlab. The procedure and the figures derived from it are real; the wording "
                   "is not model output."))
    print()
    print("  Results")
    for run in res["runs"]:
        print_run(run, full)
    print()
    print("  " + rule("-")[2:])
    print(wrap("Interpretation: " + res["reading"]))
    print()


def _params(args) -> dict:
    params = {}
    for kv in args.set or []:
        if "=" not in kv:
            raise SystemExit("--set expects key=value, got %r" % kv)
        k, v = kv.split("=", 1)
        params[k] = v
    if getattr(args, "text", None):
        params["text"] = args.text
    return params


def cmd_lab(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    res = labs.run(args.lab, b, _params(args))
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print_result(res, full=args.full, brief=args.brief)
    return 0


def cmd_all(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    failed = []
    for name in labs.ORDER:
        try:
            print_result(labs.run(name, b), full=args.full, brief=args.brief)
        except RuntimeError as e:
            failed.append(name)
            print()
            print(wrap("Lab %r did not complete: %s" % (name, e)))
            print(wrap("To repeat it on its own: python -m llmlab lab %s" % name))
    if failed:
        print()
        print(wrap("%d of %d labs did not complete: %s" % (len(failed), len(labs.ORDER), ", ".join(failed))))
        return 1
    return 0


def cmd_harness(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    log: list = []
    records = run_harness(b, args.task, args.out, loop=args.loop, wiki_path=args.wiki,
                          limit=args.limit, seed=args.seed, log=log)
    stage = 5 if args.wiki else 4 if args.loop else 3
    print()
    print(wrap("Stage %d · task %s · model %s at %s%s" % (
        stage, args.task, b.model, b.endpoint, "  (SIMULATED)" if b.simulated else "")))
    print()
    print("    %-24s %-12s %-18s %s" % ("email", "category", "checks per round", "route"))
    for line in log:
        print("    " + line)
    print()
    ready = sum(r["route"] == "ready" for r in records)
    print(wrap("%d replies in %s/ready, %d in %s/review; summary in %s/log.md. Each reply file "
               "begins with a header recording input, category, route and reason, checks, "
               "model, settings and time." % (ready, args.out, len(records) - ready, args.out, args.out)))
    if args.wiki:
        print(wrap("Wiki: %s. Answer open questions by adding a line under 'Approved answers' "
                   "and deleting the open question, then run the command again." % args.wiki))
    print()
    return 0


def cmd_copy_task(args) -> int:
    src = tasks.resolve(args.name)
    shutil.copytree(src, args.dest)
    print(wrap("Copied %s to %s. Edit the files there and pass --task %s to the harness."
               % (src.name, args.dest, args.dest)))
    return 0


def cmd_serve(args) -> int:
    from .server import serve
    serve(host=args.host, port=args.port, model=args.model,
          prefer=args.backend, open_browser=not args.no_browser)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="llmlab",
        description="Seven exercises on the behaviour of language models, run against a "
                    "model on this computer.",
    )
    p.add_argument("--version", action="version", version="llmlab " + __version__)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default=None, help="model name, e.g. gemma3:4b")
    common.add_argument("--backend", default="auto",
                        choices=["auto", "ollama", "openai", "simulated"])
    output = argparse.ArgumentParser(add_help=False)
    output.add_argument("--full", action="store_true", help="print prompts and materials unabridged")
    output.add_argument("--brief", action="store_true", help="omit background, procedure and materials")

    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("check", parents=[common], help="show what is installed and reachable")
    s.set_defaults(func=cmd_check)

    s = sub.add_parser("lab", parents=[common, output], help="run one exercise")
    s.add_argument("lab", choices=labs.ORDER)
    s.add_argument("--text", default=None, help="input text for the tokens lab")
    s.add_argument("--set", action="append", metavar="key=value",
                   help="lab parameter, e.g. --set num_ctx=128")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_lab)

    s = sub.add_parser("all", parents=[common, output], help="run all seven exercises in order")
    s.set_defaults(func=cmd_all)

    s = sub.add_parser("harness", parents=[common],
                       help="process a folder of emails (stages 3 to 5)")
    s.add_argument("--task", default="student_emails",
                   help="built-in task name or path to a task folder")
    s.add_argument("--out", default="out")
    s.add_argument("--seed", type=int, default=42)
    s.add_argument("--limit", type=int, default=None, metavar="N", help="process the first N inputs only")
    s.add_argument("--loop", type=int, default=0, metavar="N",
                   help="stage 4: check and revise each reply, N rounds at most")
    s.add_argument("--wiki", default=None, metavar="FILE",
                   help="stage 5: read and extend a wiki file")
    s.set_defaults(func=cmd_harness)

    s = sub.add_parser("copy-task", help="copy a built-in task folder for editing")
    s.add_argument("name")
    s.add_argument("dest")
    s.set_defaults(func=cmd_copy_task)

    s = sub.add_parser("serve", parents=[common], help="open the browser interface")
    s.add_argument("--host", default="127.0.0.1")
    s.add_argument("--port", type=int, default=8765)
    s.add_argument("--no-browser", action="store_true")
    s.set_defaults(func=cmd_serve)

    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nstopped")
        return 130
    except (RuntimeError, KeyError, ValueError) as e:
        print("\n  %s\n" % e, file=sys.stderr)
        print(wrap("`python -m llmlab check` shows what is reachable; `--backend simulated` "
                   "runs without a model."))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
