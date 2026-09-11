"""Headless validation for llmlab.  Run:  python test_llmlab.py

Spins up a mock Ollama service on a spare port, points llmlab at it, and
exercises every lab through both the CLI and the HTTP interface. Also runs
everything again in simulated mode, since that is the path a participant hits
when their service is not up.
"""

import io
import json
import os
import pathlib
import shutil
import socket
import sys
import threading
import urllib.request
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print("  ok    %s" % name)
    else:
        print("  FAIL  %s  %s" % (name, detail))
        FAILS.append(name)


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ---------------------------------------------------------------- mock Ollama

CALLS = []


class MockOllama(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path == "/api/tags":
            self._json(200, {"models": [{"name": "gemma:latest"}, {"name": "gemma:2b"}]})
        else:
            self._json(404, {})

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        req = json.loads(self.rfile.read(n) or b"{}")
        CALLS.append(req)
        prompt = req.get("prompt", "")
        opts = req.get("options", {})
        ctx = opts.get("num_ctx", 8192)
        temp = opts.get("temperature", 0.0)
        seed = opts.get("seed")

        # crude token model: one token per whitespace-separated word
        words = prompt.split()
        visible = words[-ctx:] if len(words) > ctx else words
        text = "mock answer"
        if "code word" in prompt.lower():
            joined = " ".join(visible)
            if "BASALT" in joined:
                text = "BASALT"
            else:
                text = "MERIDIAN"
        elif temp and temp > 0:
            text = "mock answer variant %d" % len(CALLS)
        elif seed is not None:
            text = "mock deterministic answer (seed %s)" % seed
        self._json(
            200,
            {
                "response": text,
                # three tokens of chat template, unless the template is off
                "prompt_eval_count": len(words) + (0 if req.get("raw") else 3),
                "eval_count": len(text.split()),
                "done": True,
            },
        )


def start_mock():
    port = free_port()
    srv = ThreadingHTTPServer(("127.0.0.1", port), MockOllama)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, "http://127.0.0.1:%d" % port


srv, endpoint = start_mock()
os.environ["LLMLAB_OLLAMA"] = endpoint
os.environ["LLMLAB_MODEL"] = "gemma:latest"

from llmlab import backend as be  # noqa: E402
from llmlab import labs  # noqa: E402
from llmlab.cli import main  # noqa: E402
from llmlab.harness import run_harness  # noqa: E402

be.DEFAULT_OLLAMA = endpoint

print("\n== backend detection ==")
b = be.detect()
check("detects Ollama", b.name == "ollama", b.name)
check("picks a model that exists", b.model == "gemma:latest", b.model)
check("survey reports up", be.survey()["ollama"]["up"] is True)
sim = be.detect(prefer="simulated")
check("simulated on request", sim.simulated is True)

print("\n== every lab, live route ==")
for name in labs.ORDER:
    res = labs.run(name, b)
    ok = (
        isinstance(res.get("runs"), list)
        and len(res["runs"]) >= 1
        and res.get("reading")
        and res.get("ask")
        and res.get("claim")
        and res.get("block")
    )
    check("lab %s returns a full result" % name, ok)
    check("lab %s json-serialisable" % name, bool(json.dumps(res)))

print("\n== the claims each lab is supposed to demonstrate ==")
ctx = labs.run("context", b, {"num_ctx": 20, "filler_repeats": 30})
wide, narrow = ctx["runs"][0], ctx["runs"][1]
check("wide window finds the code word", wide["correct"] is True)
check("narrow window misses it", narrow["correct"] is False)
check("narrow answer does not flag the loss",
      "missing" not in narrow["text"].lower() and "cannot" not in narrow["text"].lower())

vary = labs.run("vary", b, {"n": 3, "temperature": 0.9})
cold = [r for r in vary["runs"] if "0.0" in r["label"]]
hot = [r for r in vary["runs"] if "0.0" not in r["label"]]
check("temperature 0 is stable", len({r["text"] for r in cold}) == 1)
check("temperature above 0 varies", len({r["text"] for r in hot}) > 1)

tok = labs.run("tokens", b, {"text": "one two three four five"})
check("token count comes from the server", tok["runs"][0]["prompt_tokens"] == 5)
check("template tokens are counted separately", tok["runs"][0].get("wrapper_tokens") == 3,
      tok["runs"][0].get("wrapper_tokens"))
check("approximation is reported separately", "chips" in tok["runs"][0])

steer = labs.run("steer", b)
check("steer sends a system prompt", any("system" in c for c in CALLS))

ladder = labs.run("ladder", b)
labels = [r["label"] for r in ladder["runs"]]
check("ladder has four rungs", len(labels) == 4, labels)
check("harness rung points at the command line",
      "python -m llmlab harness" in ladder["runs"][3]["text"])
check("ladder checks rungs one to three against the rules",
      all("checks" in r for r in ladder["runs"][:3]))
check("steer runs the pasted-rules control", len(steer["runs"]) == 3)
check("steer reports a score for each run",
      all(len(r["checks"]) == 5 for r in steer["runs"]))

print("\n== the checks behind the readings ==")
good = ('The phrase "quite good" is vague: it gives no measure.\n\n'
        "What result did you expect, and by how much did you miss it?")
bad = ("**Strengths:**\n* Concise.\n* Clear.\n**Weaknesses:**\n* Vague.\n"
       "Instead, the writer could say 'the results agreed with the model'.")
cg, cb = labs.check_feedback(good), labs.check_feedback(bad)
check("a compliant comment meets all five rules", all(c["ok"] for c in cg), cg)
check("a rewriting, five-point comment misses at least three",
      sum(not c["ok"] for c in cb) >= 3, cb)
check("a declining answer is recognised",
      labs.abstained("I don't have the specific information on when these apply."))
check("a disclaimer at the end is not mistaken for declining",
      not labs.abstained("The obligations apply from 2 August 2026. I cannot "
                         "give legal advice, so consult your legal office."))
g = labs.run("ground", b)
check("ground reading does not claim both read the same when one declined",
      "declined" not in g["reading"] or "does not show the claim" in g["reading"])

print("\n== model choice when the default is missing ==")
names = ["nomic-embed-text:latest", "mistral-small3.1:24b", "qwen3-vl:8b",
         "gemma3:12b", "llama3.1:8b", "gemma4:latest"]
check("never picks an embedding model",
      be._fallback_model(["nomic-embed-text:latest", "phi3:latest"], "gemma3:4b") == "phi3:latest")
check("prefers the default's family",
      be._fallback_model(names, "gemma3:4b") == "gemma3:12b")
check("otherwise the smallest text model",
      be._fallback_model(names[:3] + ["llama3.1:8b"], "gemma3:4b") == "llama3.1:8b")

route = labs.run("route", b)
check("route names the endpoint", endpoint in route["runs"][0]["text"])
check("route lists Art. 4", any("Art. 4" in n for n in route["runs"][0]["notes"]))
check("route does not claim local removes Annex III",
      any("Annex III" in n for n in route["runs"][0]["notes"]))

print("\n== simulated route ==")
for name in labs.ORDER:
    res = labs.run(name, sim)
    check("simulated %s is labelled" % name, res["simulated"] is True)
sctx = labs.run("context", sim, {"num_ctx": 30, "filler_repeats": 40})
check("simulated context: wide finds it", sctx["runs"][0]["correct"] is True)
check("simulated context: narrow misses it", sctx["runs"][1]["correct"] is False)
svary = labs.run("vary", sim, {"n": 3, "temperature": 0.9})
scold = [r for r in svary["runs"] if "0.0" in r["label"]]
check("simulated temperature 0 is stable", len({r["text"] for r in scold}) == 1)
check("simulated results carry the disclaimer",
      any("No model was called" in n for n in svary["runs"][0]["notes"]))

print("\n== harness ==")
out = pathlib.Path("/tmp/llmlab_out")
if out.exists():
    shutil.rmtree(out)
written = run_harness(b, str(ROOT / "examples/feedback_spec.md"),
                      str(ROOT / "examples/inputs"), str(out))
check("one output per input", len(written) == 3, written)
first = pathlib.Path(written[0]).read_text()
for field in ("input:", "spec:", "model:", "temperature:", "seed:", "produced:", "simulated:"):
    check("provenance header carries %s" % field, field in first)

print("\n== CLI ==")
for argv in (["check"], ["lab", "tokens", "--text", "hello there"], ["lab", "context",
             "--set", "num_ctx=20"], ["all"], ["lab", "route", "--json"]):
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            rc = main(argv)
        check("cli %s" % " ".join(argv), rc == 0 and len(buf.getvalue()) > 50)
    except SystemExit as e:
        check("cli %s" % " ".join(argv), e.code == 0)
    except Exception as e:
        check("cli %s" % " ".join(argv), False, repr(e))

buf = io.StringIO()
with redirect_stdout(buf):
    main(["lab", "route", "--json"])
check("cli --json emits valid json", bool(json.loads(buf.getvalue())))

buf = io.StringIO()
with redirect_stdout(buf):
    main(["lab", "tokens", "--backend", "simulated"])
check("cli simulated mode says so", "SIMULATED MODE" in buf.getvalue())

print("\n== http interface ==")
from llmlab import server as sv  # noqa: E402

port = free_port()
sv.Handler.backend_pref = "auto"
sv.Handler.model = None
httpd = ThreadingHTTPServer(("127.0.0.1", port), sv.Handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
base = "http://127.0.0.1:%d" % port

html = urllib.request.urlopen(base + "/").read().decode()
check("serves the interface", "<title>llmlab" in html)
check("no external network references in the page",
      not any(s in html for s in ("http://", "https://", "cdn", "fonts.g")))
check("no browser storage in the page",
      not any(s in html for s in ("localStorage", "sessionStorage", "indexedDB")))

s = json.loads(urllib.request.urlopen(base + "/api/survey").read().decode())
check("survey exposes the active route", s["active"]["backend"] == "ollama")
check("survey lists seven labs", len(s["labs"]) == 7)

req = urllib.request.Request(base + "/api/lab", method="POST",
                             data=json.dumps({"lab": "tokens",
                                              "params": {"text": "a b c"}}).encode(),
                             headers={"Content-Type": "application/json"})
r = json.loads(urllib.request.urlopen(req).read().decode())
check("api runs a lab", r["runs"][0]["prompt_tokens"] == 3)

req = urllib.request.Request(base + "/api/lab", method="POST",
                             data=json.dumps({"lab": "nonsense"}).encode(),
                             headers={"Content-Type": "application/json"})
try:
    urllib.request.urlopen(req)
    check("unknown lab returns an error", False)
except urllib.error.HTTPError as e:
    body = json.loads(e.read().decode())
    check("unknown lab returns an error with a hint", e.code == 400 and "hint" in body)

req = urllib.request.Request(base + "/api/lab", method="POST",
                             data=json.dumps({"lab": "tokens",
                                              "backend": "simulated"}).encode(),
                             headers={"Content-Type": "application/json"})
r = json.loads(urllib.request.urlopen(req).read().decode())
check("api honours the simulated route", r["simulated"] is True)

print("\n== failure when nothing is running ==")
be.DEFAULT_OLLAMA = "http://127.0.0.1:1"
be.DEFAULT_OPENAI = "http://127.0.0.1:2"
fb = be.detect()
check("falls back to simulated", fb.simulated is True)
try:
    be.detect(prefer="ollama")
    check("explicit ollama fails loudly", False)
except RuntimeError:
    check("explicit ollama fails loudly", True)
be.DEFAULT_OLLAMA = endpoint

print("\n%s" % ("-" * 60))
print("%d checks failed" % len(FAILS))
if FAILS:
    for f in FAILS:
        print("   - %s" % f)
sys.exit(1 if FAILS else 0)
