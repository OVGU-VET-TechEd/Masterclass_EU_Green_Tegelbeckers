"""Shared code for the scripts in this folder.

Each lab script calls run_lab(). The result is printed in the terminal; with
--out FILE it is also written to a file:

  --out result.json   the complete result as JSON (prompts, settings, outputs,
                      checks, interpretation)
  --out result.txt    the terminal text (any extension other than .json)
"""

from __future__ import annotations

import argparse
import datetime
import io
import json
import pathlib
import sys
from contextlib import redirect_stdout

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from llmlab import __version__, backend as be, labs  # noqa: E402
from llmlab.cli import print_result  # noqa: E402


def common_arguments(ap: argparse.ArgumentParser) -> None:
    ap.add_argument("--model", default=None, help="model name, e.g. gemma3:12b (default: automatic)")
    ap.add_argument("--backend", default="auto", choices=["auto", "ollama", "openai", "simulated"],
                    help="model route (default: auto)")
    ap.add_argument("--full", action="store_true", help="print prompts and materials unabridged")
    ap.add_argument("--brief", action="store_true", help="omit background, procedure and materials")


def parse_set(pairs) -> dict:
    params = {}
    for kv in pairs or []:
        if "=" not in kv:
            raise SystemExit("--set expects key=value, got %r" % kv)
        k, v = kv.split("=", 1)
        params[k] = v
    return params


def render(res: dict, full: bool, brief: bool) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        print_result(res, full=full, brief=brief)
    return buf.getvalue()


def write(path: str, res, text: str) -> None:
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix.lower() == ".json":
        p.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        p.write_text(text, encoding="utf-8")
    print("written: %s" % p)


def header(b) -> str:
    return "llmlab %s · %s · model %s · %s%s" % (
        __version__, datetime.datetime.now().isoformat(timespec="seconds"), b.model, b.endpoint,
        "  (SIMULATED: no model service reachable)" if b.simulated else "")


def run_lab(name: str) -> int:
    info = labs.INFO[name]
    ap = argparse.ArgumentParser(description="%s. %s" % (info["title"], info["aim"]))
    common_arguments(ap)
    ap.add_argument("--set", action="append", metavar="key=value",
                    help="lab parameter; defaults: %s" % (
                        ", ".join("%s=%s" % kv for kv in labs.DEFAULTS[name].items()
                                  if not isinstance(kv[1], str) or len(kv[1]) < 20) or "none"))
    ap.add_argument("--out", metavar="FILE", help="also write the result to FILE (.json = full data, otherwise text)")
    args = ap.parse_args()

    b = be.detect(args.model, prefer=args.backend)
    print(header(b))
    try:
        res = labs.run(name, b, parse_set(args.set))
    except RuntimeError as e:
        print("\n  %s\n  `python -m llmlab check` shows what is reachable; "
              "`--backend simulated` runs without a model." % e, file=sys.stderr)
        return 1
    text = render(res, args.full, args.brief)
    print(text)
    if args.out:
        write(args.out, res, header(b) + "\n" + text)
    return 0
