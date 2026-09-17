"""Lab 5 · Grounding: answers with and without a supplied source text.

Run from the folder V6/llmlab:

    python scripts/lab5_ground.py
    python scripts/lab5_ground.py --model gemma3:12b --out results/lab5.json

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab5_ground.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("ground"))
