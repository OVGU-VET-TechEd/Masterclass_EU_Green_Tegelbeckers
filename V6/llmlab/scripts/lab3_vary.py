"""Lab 3 · Temperature and seed: distinct outputs at temperature 0 with seed and at a higher temperature.

Run from the folder V6/llmlab:

    python scripts/lab3_vary.py
    python scripts/lab3_vary.py --set n=5 --set temperature=1.0
    python scripts/lab3_vary.py --out results/lab3.json

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab3_vary.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("vary"))
