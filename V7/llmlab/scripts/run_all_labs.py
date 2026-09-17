"""All seven labs in sequence.

Run from the folder V6/llmlab:

    python scripts/run_all_labs.py
    python scripts/run_all_labs.py --model gemma3:12b --out-dir results

With --out-dir DIR, each lab is written twice: DIR/labN_name.json (complete
data) and DIR/labN_name.txt (terminal text), plus DIR/summary.txt.
A lab that fails is reported and the next one is started.
"""

import argparse
import pathlib
import sys
import time

from _runner import be, common_arguments, header, labs, render, write


def main() -> int:
    ap = argparse.ArgumentParser(description="Run all seven llmlab exercises.")
    common_arguments(ap)
    ap.add_argument("--out-dir", metavar="DIR", help="write one .json and one .txt file per lab to DIR")
    args = ap.parse_args()

    b = be.detect(args.model, prefer=args.backend)
    head = header(b)
    print(head)
    summary, failed = [head, ""], []
    for i, name in enumerate(labs.ORDER, 1):
        t0 = time.time()
        try:
            res = labs.run(name, b)
        except RuntimeError as e:
            failed.append(name)
            line = "lab %d %-8s FAILED: %s" % (i, name, e)
            print(line, file=sys.stderr)
            summary.append(line)
            continue
        text = render(res, args.full, args.brief)
        print(text)
        summary.append("lab %d %-8s %5.1f s  %s" % (i, name, time.time() - t0, res["reading"][:160]))
        if args.out_dir:
            stem = pathlib.Path(args.out_dir) / ("lab%d_%s" % (i, name))
            write(str(stem) + ".json", res, text)
            write(str(stem) + ".txt", res, head + "\n" + text)
    if args.out_dir:
        p = pathlib.Path(args.out_dir) / "summary.txt"
        p.write_text("\n".join(summary) + "\n", encoding="utf-8")
        print("written: %s" % p)
    print("\n%d of %d labs completed" % (len(labs.ORDER) - len(failed), len(labs.ORDER)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
