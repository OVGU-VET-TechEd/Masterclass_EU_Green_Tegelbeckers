"""Lab 2 · Context window: answer to a question whose source passage lies outside the window.

Run from the folder V6/llmlab:

    python scripts/lab2_context.py
    python scripts/lab2_context.py --set num_ctx=1024 --set sections=200
    python scripts/lab2_context.py --out results/lab2.txt

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab2_context.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("context"))
