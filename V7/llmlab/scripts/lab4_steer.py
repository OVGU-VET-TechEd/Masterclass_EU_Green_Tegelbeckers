"""Lab 4 · Rules absent, in the user message, or in the system prompt.

Run from the folder V6/llmlab:

    python scripts/lab4_steer.py
    python scripts/lab4_steer.py --model llama3.1:8b --out results/lab4.json

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab4_steer.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("steer"))
