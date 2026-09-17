"""Lab 6 · Five stages of prompting on replies to student emails.

Run from the folder V6/llmlab:

    python scripts/lab6_ladder.py
    python scripts/lab6_ladder.py --set stage=loop --set emails=7
    python scripts/lab6_ladder.py --set emails=7 --out results/lab6.json

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab6_ladder.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("ladder"))
