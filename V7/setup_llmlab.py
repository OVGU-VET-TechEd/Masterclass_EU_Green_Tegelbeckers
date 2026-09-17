#!/usr/bin/env python3
"""Guided setup for llmlab (Workshop 4 — AI in Teaching, version 7).

Runs the installation steps of llmlab/README.md one after another and says
what it finds at each step. Standard library only; Windows, macOS and Linux.

    python setup_llmlab.py              guided setup, asks before changing anything
    python setup_llmlab.py --check      report only, change nothing
    python setup_llmlab.py --yes        accept the recommended answers
    python setup_llmlab.py --help       all options

Steps
    1  Python 3.9 or later
    2  the llmlab folder next to this file
    3  Ollama installed and its service reachable (install / start on request)
    4  a model for the exercises, by default gemma3:4b (download on request)
    5  optional: install llmlab as a command in a virtual environment
    6  verification: `python -m llmlab check`, optionally the test suite
    7  optional: open the browser interface

Without Ollama the exercises still run, in simulated mode: every result is
then marked as simulated. Nothing in this script sends data anywhere except
the downloads you confirm (Ollama installer, model).

CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab · EU GREEN Alliance.
"""

# No f-strings before the version check, so that an old Python prints a
# readable message instead of a syntax error.
import sys

if sys.version_info < (3, 9):
    sys.stdout.write(
        "llmlab needs Python 3.9 or later; this is Python %d.%d.\n"
        "Install a current Python from https://www.python.org/downloads/ and run this "
        "script again (on macOS and Linux possibly as `python3 setup_llmlab.py`).\n"
        % sys.version_info[:2])
    sys.exit(1)

import argparse
import json
import os
import pathlib
import platform
import shutil
import subprocess
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
LAB = HERE / "llmlab"
OLLAMA_URL = os.environ.get("LLMLAB_OLLAMA", "http://127.0.0.1:11434").rstrip("/")
DEFAULT_MODEL = os.environ.get("LLMLAB_MODEL", "gemma3:4b")
MODEL_SIZE_GB = {"gemma3:1b": 0.9, "gemma3:4b": 3.3, "gemma3:12b": 8.1, "llama3.1:8b": 4.9}
SYSTEM = platform.system()  # "Windows", "Darwin", "Linux"

WIDTH = 78
issues = []      # (step, text) that remain open at the end
notes = []       # things worth repeating in the summary


# ---------------------------------------------------------------- output

def head(n, title):
    print()
    print("-" * WIDTH)
    print(" %s  %s" % (n, title))
    print("-" * WIDTH)


def ok(text):
    print("  [ ok ]  " + text)


def warn(text):
    print("  [note]  " + text)


def fail(text):
    print("  [open]  " + text)


def info(text):
    for line in text.splitlines():
        print("          " + line)


def ask(question, default, args):
    """Yes/no question. --check answers no, --yes takes the default."""
    if args.check:
        return False
    if args.yes or not sys.stdin.isatty():
        return default
    hint = "[Y/n]" if default else "[y/N]"
    while True:
        try:
            answer = input("  ?       %s %s " % (question, hint)).strip().lower()
        except EOFError:
            return default
        if not answer:
            return default
        if answer in ("y", "yes", "j", "ja"):
            return True
        if answer in ("n", "no", "nein"):
            return False


def run(cmd, cwd=None, env=None):
    """Run a command with its output shown; return the exit code."""
    info("$ " + " ".join(str(c) for c in cmd))
    sys.stdout.flush()
    try:
        return subprocess.call([str(c) for c in cmd], cwd=cwd, env=env)
    except OSError as e:
        fail("could not start %s: %s" % (cmd[0], e))
        return 127


# ---------------------------------------------------------------- Ollama

def ollama_models():
    """Installed model names, or None if the service does not answer."""
    try:
        with urllib.request.urlopen(OLLAMA_URL + "/api/tags", timeout=3) as r:
            data = json.loads(r.read().decode("utf-8"))
        return [m.get("name", "") for m in data.get("models", [])]
    except (urllib.error.URLError, OSError, ValueError):
        return None


def ollama_binary():
    found = shutil.which("ollama")
    if found:
        return found
    candidates = []
    if SYSTEM == "Darwin":
        candidates = ["/usr/local/bin/ollama", "/opt/homebrew/bin/ollama",
                      "/Applications/Ollama.app/Contents/Resources/ollama"]
    elif SYSTEM == "Windows":
        local = os.environ.get("LOCALAPPDATA", "")
        candidates = [os.path.join(local, "Programs", "Ollama", "ollama.exe")]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None


def install_ollama(args):
    """Offer the platform's usual installation route. Returns True if attempted."""
    manual = "Download and install Ollama from https://ollama.com/download, then run this script again."
    if SYSTEM == "Darwin":
        if shutil.which("brew"):
            if ask("Install Ollama with Homebrew (brew install ollama)?", False, args):
                return run(["brew", "install", "ollama"]) == 0
        info(manual)
    elif SYSTEM == "Windows":
        if shutil.which("winget"):
            if ask("Install Ollama with winget (winget install Ollama.Ollama)?", False, args):
                return run(["winget", "install", "-e", "--id", "Ollama.Ollama"]) == 0
        info(manual)
    elif SYSTEM == "Linux":
        info("The official route is the install script from ollama.com:")
        info("  curl -fsSL https://ollama.com/install.sh | sh")
        if shutil.which("curl") and shutil.which("sh"):
            if ask("Run the official install script now (needs sudo)?", False, args):
                return run(["sh", "-c", "curl -fsSL https://ollama.com/install.sh | sh"]) == 0
    else:
        info(manual)
    return False


def start_ollama(binary, args):
    """Start `ollama serve` in the background and wait until it answers."""
    if SYSTEM == "Darwin" and os.path.exists("/Applications/Ollama.app"):
        if not ask("Start the Ollama app?", True, args):
            return False
        subprocess.Popen(["open", "-a", "Ollama"])
    else:
        if not ask("Start the Ollama service in the background (ollama serve)?", True, args):
            return False
        kwargs = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL, "stdin": subprocess.DEVNULL}
        if SYSTEM == "Windows":
            kwargs["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | NEW_PROCESS_GROUP
        else:
            kwargs["start_new_session"] = True
        try:
            subprocess.Popen([binary, "serve"], **kwargs)
        except OSError as e:
            fail("could not start Ollama: %s" % e)
            return False
    info("waiting for the service ...")
    for _ in range(30):
        time.sleep(1)
        if ollama_models() is not None:
            return True
    return False


def is_text_gemma(name):
    n = name.lower()
    return n.startswith("gemma") and not any(x in n for x in ("embed", "vision", "-vl", "base"))


# ---------------------------------------------------------------- steps

def step_python():
    head(1, "Python")
    ok("Python %s at %s" % (platform.python_version(), sys.executable))
    if SYSTEM == "Windows" and "WindowsApps" in sys.executable:
        warn("this is the Microsoft Store alias; if something fails, install Python from python.org")


def step_folder():
    head(2, "llmlab folder")
    if not (LAB / "llmlab" / "__init__.py").exists():
        fail("no llmlab package found at %s" % LAB)
        info("Keep this script in the folder that contains `llmlab/` (the unpacked V7 folder).")
        sys.exit(1)
    version = "?"
    for line in (LAB / "llmlab" / "__init__.py").read_text(encoding="utf-8").splitlines():
        if line.startswith("__version__"):
            version = line.split("=", 1)[1].strip().strip("\"'")
    ok("llmlab %s at %s" % (version, LAB))
    tasks = LAB / "llmlab" / "tasks" / "student_emails" / "inputs"
    n = len(list(tasks.glob("*.txt"))) if tasks.exists() else 0
    if n == 7:
        ok("task folder student_emails complete (7 emails)")
    else:
        fail("task folder student_emails incomplete (%d of 7 emails) — unpack the archive again" % n)
        issues.append((2, "task folder incomplete"))


def step_ollama(args):
    head(3, "Ollama (model service)")
    if args.simulated:
        warn("skipped (--simulated): the exercises will run in simulated mode")
        notes.append("Simulated mode: results are produced by llmlab and marked as simulated.")
        return None
    models = ollama_models()
    if models is not None:
        ok("service reachable at %s" % OLLAMA_URL)
        return models
    binary = ollama_binary()
    if not binary:
        fail("Ollama is not installed")
        if install_ollama(args):
            binary = ollama_binary()
            models = ollama_models()
            if models is not None:
                ok("Ollama installed and running")
                return models
        if not binary:
            issues.append((3, "Ollama not installed — the exercises run in simulated mode until it is"))
            return None
    ok("Ollama installed: %s" % binary)
    fail("service not reachable at %s" % OLLAMA_URL)
    if start_ollama(binary, args):
        ok("service started")
        return ollama_models()
    issues.append((3, "Ollama service not running — start the Ollama app or run `ollama serve`"))
    return None


def step_model(models, args):
    head(4, "Model")
    if models is None:
        warn("no model service, so no model to check")
        return
    text_models = [m for m in models if "embed" not in m.lower()]
    wanted = args.model
    if wanted in models or wanted + ":latest" in models:
        ok("%s is installed" % wanted)
        return
    gemmas = [m for m in text_models if is_text_gemma(m)]
    if gemmas:
        warn("%s is not installed; llmlab would use another Gemma model (%s)" % (wanted, ", ".join(gemmas)))
    elif text_models:
        warn("%s is not installed and no Gemma model is present; llmlab would use the smallest text model" % wanted)
    else:
        fail("no model installed")
    size = MODEL_SIZE_GB.get(wanted)
    if size:
        free = shutil.disk_usage(str(pathlib.Path.home())).free / 1e9
        info("download size of %s: about %.1f GB; free disk space: %.0f GB" % (wanted, size, free))
        if free < size + 1:
            fail("not enough free disk space for %s" % wanted)
            issues.append((4, "free disk space before downloading %s" % wanted))
            return
    default = not gemmas and not text_models
    if ask("Download %s now (ollama pull %s)?" % (wanted, wanted), default, args):
        binary = ollama_binary() or "ollama"
        if run([binary, "pull", wanted]) == 0:
            ok("%s downloaded" % wanted)
            return
        fail("download failed")
    if not gemmas and not text_models:
        issues.append((4, "no model installed — run `ollama pull %s`" % wanted))
    else:
        notes.append("To use %s later: `ollama pull %s`, or add `--model <name>` to any command." % (wanted, wanted))


def step_install(args):
    head(5, "Install as a command (optional)")
    info("Not required: `python run.py` and `python -m llmlab ...` work from the folder.")
    venv = LAB / ".venv"
    py = venv / ("Scripts/python.exe" if SYSTEM == "Windows" else "bin/python")
    if py.exists():
        ok("virtual environment exists: %s" % venv)
        return
    if not ask("Create a virtual environment in llmlab/.venv and install the `llmlab` command?",
               args.install, args):
        warn("skipped")
        return
    if run([sys.executable, "-m", "venv", str(venv)]) != 0:
        fail("could not create the virtual environment")
        issues.append((5, "virtual environment not created"))
        return
    leftovers = [LAB / "build", LAB / "llmlab.egg-info"]
    existed = {d: d.exists() for d in leftovers}
    code = run([py, "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "."], cwd=str(LAB))
    for d in leftovers:  # build artefacts pip leaves in the source folder
        if d.exists() and not existed[d]:
            shutil.rmtree(str(d), ignore_errors=True)
    if code != 0:
        fail("pip install failed (it needs a network connection for setuptools)")
        issues.append((5, "`pip install .` failed — use `python run.py` instead"))
        return
    ok("installed")
    if SYSTEM == "Windows":
        notes.append("Activate the command with: llmlab\\.venv\\Scripts\\activate  then  llmlab check")
    else:
        notes.append("Activate the command with: source llmlab/.venv/bin/activate  then  llmlab check")


def step_verify(args):
    head(6, "Verification")
    env = dict(os.environ)
    cmd = [sys.executable, "-m", "llmlab", "check"]
    if args.model:
        env["LLMLAB_MODEL"] = args.model
    if args.simulated:
        cmd += ["--backend", "simulated"]
    if run(cmd, cwd=str(LAB), env=env) != 0:
        fail("`python -m llmlab check` failed")
        issues.append((6, "llmlab check failed"))
    else:
        ok("llmlab check completed")
    if args.test or ask("Run the test suite (no model needed, about half a minute)?", False, args):
        if run([sys.executable, "scripts/run_tests.py"], cwd=str(LAB)) == 0:
            ok("tests passed")
        else:
            fail("tests failed")
            issues.append((6, "test suite failed"))


def step_start(args):
    head(7, "Start")
    if args.check:
        info("--check: not starting anything")
        return
    if args.start or ask("Open the browser interface now (python run.py)?", False, args):
        info("stop it with Ctrl+C")
        cmd = [sys.executable, "run.py"]
        if args.simulated:
            cmd += ["--backend", "simulated"]
        run(cmd, cwd=str(LAB))


# ---------------------------------------------------------------- main

def main():
    p = argparse.ArgumentParser(
        description="Guided setup for llmlab (Workshop 4 — AI in Teaching, v7).")
    p.add_argument("--check", action="store_true", help="report only; change nothing")
    p.add_argument("--yes", "-y", action="store_true", help="accept the recommended answers")
    p.add_argument("--model", default=DEFAULT_MODEL, help="model for the exercises (default %(default)s)")
    p.add_argument("--simulated", action="store_true", help="skip Ollama; use simulated mode")
    p.add_argument("--install", action="store_true", help="install llmlab as a command in llmlab/.venv")
    p.add_argument("--test", action="store_true", help="run the test suite")
    p.add_argument("--start", action="store_true", help="open the browser interface at the end")
    args = p.parse_args()

    print("=" * WIDTH)
    print(" llmlab setup · Workshop 4 — AI in Teaching · version 7")
    print(" %s %s · %s" % (SYSTEM, platform.release(), "report only" if args.check else "guided"))
    print("=" * WIDTH)

    step_python()
    step_folder()
    models = step_ollama(args)
    step_model(models, args)
    step_install(args)
    step_verify(args)

    print()
    print("=" * WIDTH)
    if issues:
        print(" Still open:")
        for n, text in issues:
            print("   step %d  %s" % (n, text))
    else:
        print(" Setup complete.")
    for text in notes:
        print("   " + text)
    print()
    print(" Next, in the folder %s:" % LAB)
    print("   python run.py                  browser interface")
    print("   python -m llmlab all           all seven exercises in the terminal")
    print("   python -m llmlab lab context   one exercise")
    print("=" * WIDTH)

    step_start(args)
    return 1 if issues else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n  stopped")
        sys.exit(130)
