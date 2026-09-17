"""The automated test suite (test_llmlab.py), with optional file output.

Run from the folder V6/llmlab:

    python scripts/run_tests.py
    python scripts/run_tests.py --out results/tests.txt

The suite uses a mock model service and the simulated route; it needs no
running model and takes a few seconds. Exit code 0 means all checks passed.
"""

import argparse
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser(description="Run the llmlab test suite.")
    ap.add_argument("--out", metavar="FILE", help="also write the test output to FILE")
    args = ap.parse_args()
    proc = subprocess.run([sys.executable, str(ROOT / "test_llmlab.py")], cwd=str(ROOT),
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(proc.stdout)
    if args.out:
        p = pathlib.Path(args.out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(proc.stdout, encoding="utf-8")
        print("written: %s" % p)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
