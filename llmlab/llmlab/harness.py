"""Rung four of the prompting ladder, as an actual command.

One specification file, one folder of inputs, one output file per input, each
carrying a record of how it was produced. Nothing here is clever. That is the
argument: the difference between rung one and rung four is not sophistication,
it is that this leaves a trail.
"""

from __future__ import annotations

import datetime
import pathlib
from typing import List

from .backend import Backend

SUFFIXES = {".md", ".txt"}


def run_harness(
    backend: Backend,
    spec_path: str,
    inputs_dir: str,
    out_dir: str,
    temperature: float = 0.0,
    seed: int = 42,
    max_tokens: int = 400,
) -> List[str]:
    spec = pathlib.Path(spec_path).read_text(encoding="utf-8")
    in_dir = pathlib.Path(inputs_dir)
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in in_dir.iterdir() if p.suffix.lower() in SUFFIXES)
    if not files:
        raise SystemExit("No .md or .txt files in %s" % in_dir)

    written = []
    for p in files:
        body = p.read_text(encoding="utf-8")
        r = backend.generate(
            body, system=spec, temperature=temperature, seed=seed, max_tokens=max_tokens
        )
        stamp = datetime.datetime.now().isoformat(timespec="seconds")
        target = out / (p.stem + ".out.md")
        target.write_text(
            "\n".join(
                [
                    "<!--",
                    "  produced by llmlab harness",
                    "  input:       %s" % p.name,
                    "  spec:        %s" % pathlib.Path(spec_path).name,
                    "  model:       %s" % r.model,
                    "  endpoint:    %s" % r.endpoint,
                    "  temperature: %s   seed: %s" % (temperature, seed),
                    "  simulated:   %s" % r.simulated,
                    "  produced:    %s" % stamp,
                    "-->",
                    "",
                    r.text,
                    "",
                ]
            ),
            encoding="utf-8",
        )
        written.append(str(target))
    return written
