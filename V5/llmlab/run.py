#!/usr/bin/env python3
"""Start the browser interface without touching the command line.

In VS Code: open this folder, open this file, press F5 (or the Run button).
Elsewhere: python run.py
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from llmlab.cli import main

if __name__ == "__main__":
    raise SystemExit(main(["serve"] + sys.argv[1:]))
