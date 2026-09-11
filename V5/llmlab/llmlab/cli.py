"""Command line entry point: python -m llmlab <command>"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import textwrap

from . import __version__, backend as be, labs
from .harness import run_harness

W = 78


def wrap(text: str, indent: str = "  ") -> str:
    out = []
    for para in text.split("\n"):
        out.append(textwrap.fill(para, W, initial_indent=indent, subsequent_indent=indent))
    return "\n".join(out)


def rule(char: str = "-") -> str:
    return char * W


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
            "No model service answered, so llmlab will run in simulated mode. "
            "Every result will say so on its face. The exercises still make "
            "their point; the text they show was written by llmlab, not by a "
            "model. To get the real thing: install Ollama, then run "
            "`ollama pull gemma3:4b` and try this command again. Any Gemma "
            "model already installed will be found and used.", "  "))
    else:
        print(wrap("Backend: %s, model %s, at %s" % (b.name, b.model, b.endpoint), "  "))
    print(rule())
    return 0


def print_result(res: dict) -> None:
    print()
    print(rule("="))
    print("  %s" % res["title"].upper() if False else "  %s" % res["title"])
    print("  %s" % res.get("block", ""))
    print(rule("="))
    print(wrap("Claim under test: " + res["claim"]))
    if res.get("simulated"):
        print()
        print(wrap("SIMULATED MODE — no model was called. The text below was "
                   "assembled by llmlab. Treat the structure as real and the "
                   "wording as scaffolding."))
    for run in res["runs"]:
        print()
        print("  " + rule("-")[2:])
        head = "  [%s]" % run.get("label", "")
        meta = []
        if run.get("prompt_tokens") and run.get("wrapper_tokens"):
            meta.append("%d text tokens + %d template tokens"
                        % (run["prompt_tokens"], run["wrapper_tokens"]))
        elif run.get("prompt_tokens"):
            meta.append("%d prompt tokens" % run["prompt_tokens"])
        if run.get("output_tokens"):
            meta.append("%d output tokens" % run["output_tokens"])
        if run.get("seconds"):
            meta.append("%.2fs" % run["seconds"])
        if run.get("correct") is not None:
            meta.append("code word found" if run["correct"] else "code word missed")
        print(head + ("   " + " · ".join(meta) if meta else ""))
        if run.get("chips"):
            chips = run["chips"]
            shown = chips[:60]
            print(wrap("tokens: " + " | ".join(shown) + (" …" if len(chips) > 60 else "")))
        if run.get("spec"):
            print(wrap("instruction: " + run["spec"]))
        if run.get("wiki"):
            print(wrap("wiki read this run: " + run["wiki"]))
        print(wrap(run.get("text", "")))
        if run.get("checks"):
            checks = run["checks"]
            missed = [c["rule"] for c in checks if not c["ok"]]
            print(wrap("checks: %d of %d rules met%s" % (
                len(checks) - len(missed), len(checks),
                " · missed: " + "; ".join(missed) if missed else "")))
        for n in run.get("notes", []) or []:
            print(wrap("· " + n, "    "))
    print()
    print("  " + rule("-")[2:])
    print(wrap("Reading: " + res["reading"]))
    print()
    print(wrap("Ask the room: " + res["ask"]))
    print()


def cmd_lab(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    params = {}
    for kv in args.set or []:
        if "=" not in kv:
            raise SystemExit("--set expects key=value, got %r" % kv)
        k, v = kv.split("=", 1)
        try:
            v = int(v)
        except ValueError:
            try:
                v = float(v)
            except ValueError:
                pass
        params[k] = v
    if args.text:
        params["text"] = args.text
    res = labs.run(args.lab, b, params)
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print_result(res)
    return 0


def cmd_all(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    failed = []
    for name in labs.ORDER:
        try:
            print_result(labs.run(name, b))
        except RuntimeError as e:
            failed.append(name)
            print()
            print("  " + rule("-")[2:])
            print(wrap("Lab %r did not complete: %s" % (name, e)))
            print(wrap("Continuing with the next lab. Retry this one on its "
                       "own with `python -m llmlab lab %s`." % name))
    if failed:
        print()
        print(wrap("%d of %d labs did not complete: %s"
                   % (len(failed), len(labs.ORDER), ", ".join(failed))))
        return 1
    return 0


def cmd_harness(args) -> int:
    b = be.detect(args.model, prefer=args.backend)
    log = []
    written = run_harness(b, args.spec, args.inputs, args.out,
                          temperature=args.temperature, seed=args.seed,
                          loop=args.loop, wiki_path=args.wiki, log=log)
    print()
    print(wrap("Specification: %s" % args.spec))
    print(wrap("Model: %s at %s%s" % (b.model, b.endpoint,
                                      "  (SIMULATED)" if b.simulated else "")))
    print()
    for w in written:
        print("  wrote  %s" % w)
    if log:
        print()
        for line in log:
            print(wrap(line))
    print()
    print(wrap("Each file carries a header recording the input, the "
               "specification, the model, the settings and the time. That "
               "header is what stage three leaves behind."))
    if args.loop:
        print(wrap("With --loop, the header also records every round of checks: "
                   "that is stage four's log."))
    if args.wiki:
        print(wrap("With --wiki, open %s. It is everything the system \"learned\" "
                   "- edit or delete a line and run again." % args.wiki))
    print()
    return 0


def cmd_serve(args) -> int:
    from .server import serve
    serve(host=args.host, port=args.port, model=args.model,
          prefer=args.backend, open_browser=not args.no_browser)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="llmlab",
        description="Seven exercises that make claims from the AI in Teaching "
                    "session checkable against a model running on your own machine.",
    )
    p.add_argument("--version", action="version", version="llmlab " + __version__)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default=None, help="model name, e.g. gemma3:4b")
    common.add_argument("--backend", default="auto",
                        choices=["auto", "ollama", "openai", "simulated"])

    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("check", parents=[common], help="what is installed and reachable")
    s.set_defaults(func=cmd_check)

    s = sub.add_parser("lab", parents=[common], help="run one exercise")
    s.add_argument("lab", choices=labs.ORDER)
    s.add_argument("--text", default=None, help="input text, for the tokens lab")
    s.add_argument("--set", action="append", metavar="key=value",
                   help="lab parameter, e.g. --set num_ctx=128")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_lab)

    s = sub.add_parser("all", parents=[common], help="run all seven in order")
    s.set_defaults(func=cmd_all)

    s = sub.add_parser("harness", parents=[common],
                       help="apply one specification to a folder of inputs (stages 3 to 5)")
    s.add_argument("--spec", required=True)
    s.add_argument("--inputs", required=True)
    s.add_argument("--out", default="out")
    s.add_argument("--temperature", type=float, default=0.0)
    s.add_argument("--seed", type=int, default=42)
    s.add_argument("--loop", type=int, default=0, metavar="N",
                   help="stage 4: revise each output until the five checks pass, N rounds at most")
    s.add_argument("--wiki", default=None, metavar="FILE",
                   help="stage 5: write lessons from missed rules to FILE, and read them on every run")
    s.set_defaults(func=cmd_harness)

    s = sub.add_parser("serve", parents=[common], help="open the browser interface")
    s.add_argument("--host", default="127.0.0.1")
    s.add_argument("--port", type=int, default=8765)
    s.add_argument("--no-browser", action="store_true")
    s.set_defaults(func=cmd_serve)

    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if getattr(args, "backend", "auto") == "simulated":
        args.backend = "simulated"
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nstopped")
        return 130
    except RuntimeError as e:
        print("\n  %s\n" % e, file=sys.stderr)
        print(wrap("Run `python -m llmlab check` to see what is reachable, or "
                   "add `--backend simulated` to continue without a model."))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
