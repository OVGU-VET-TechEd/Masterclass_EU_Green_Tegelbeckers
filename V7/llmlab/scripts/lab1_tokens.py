"""Lab 1 · Tokens: token count of a text, English and German compared, chat-template overhead.

Run from the folder V6/llmlab:

    python scripts/lab1_tokens.py
    python scripts/lab1_tokens.py --set text="Ihre Prüfungsleistung wurde bewertet."
    python scripts/lab1_tokens.py --out results/lab1.json

Options: --model, --backend, --set key=value, --out FILE, --full, --brief
(python scripts/lab1_tokens.py --help lists them with the defaults).
"""

from _runner import run_lab

if __name__ == "__main__":
    raise SystemExit(run_lab("tokens"))
