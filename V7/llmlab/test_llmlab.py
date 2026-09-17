"""Headless validation for llmlab.  Run:  python test_llmlab.py

Starts a mock Ollama service on a free port, points llmlab at it, and runs
every lab through the library, the command line and the HTTP interface. Runs
everything again on the simulated route, and runs the harness through stages
three to five.
"""

import io
import json
import os
import pathlib
import re
import shutil
import socket
import sys
import tempfile
import threading
import urllib.error
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
        print("  FAIL  %s  %s" % (name, str(detail)[:300]))
        FAILS.append(name)


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# ---------------------------------------------------------------- mock Ollama

CALLS = []

COMPLIANT = ("Dear student,\n\nExtensions of the portfolio deadline are decided by the "
             "examination office (pruefungsamt@example.edu).\n\nKind regards,\nEDU-204 module team")
NONCOMPLIANT = "Dear student,\n\nWe will extend your deadline to 22 January 2027."


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
        prompt, system = req.get("prompt", ""), req.get("system", "")
        opts = req.get("options", {})
        ctx = opts.get("num_ctx", 8192)
        temp = opts.get("temperature", 0.0)
        seed = opts.get("seed")

        # crude token model: one token per whitespace-separated word, window keeps the end
        words = prompt.split()
        visible = " ".join(words[-ctx:] if len(words) > ctx else words)
        if "by which date must the portfolio" in prompt:
            text = "15 January 2027" if "15 January 2027" in visible else "31 January 2027"
        elif "Classify the email" in prompt:
            text = "extension" if "extend" in prompt.split("Email:")[-1] else "information"
        elif "did not pass these checks" in prompt or "Lessons recorded from earlier runs" in system:
            text = COMPLIANT
        elif "Write the reply" in prompt or prompt.startswith("Answer this email"):
            text = NONCOMPLIANT
        elif temp and temp > 0:
            text = "mock answer variant %d" % len(CALLS)
        elif seed is not None:
            text = "mock deterministic answer (seed %s)" % seed
        else:
            text = "mock answer"
        self._json(200, {
            "response": text,
            # three tokens of chat template, unless the template is off
            "prompt_eval_count": len(words) + (0 if req.get("raw") else 3),
            "eval_count": len(text.split()),
            "done": True,
        })


def start_mock():
    port = free_port()
    srv = ThreadingHTTPServer(("127.0.0.1", port), MockOllama)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, "http://127.0.0.1:%d" % port


srv, endpoint = start_mock()
os.environ["LLMLAB_OLLAMA"] = endpoint
os.environ["LLMLAB_MODEL"] = "gemma:latest"

from llmlab import backend as be  # noqa: E402
from llmlab import checks, labs, tasks  # noqa: E402
from llmlab.cli import main  # noqa: E402
from llmlab.harness import run_harness  # noqa: E402

be.DEFAULT_OLLAMA = endpoint
TMP = pathlib.Path(tempfile.mkdtemp(prefix="llmlab_test_"))

print("\n== backend detection ==")
b = be.detect()
check("detects Ollama", b.name == "ollama", b.name)
check("picks a model that exists", b.model == "gemma:latest", b.model)
check("survey reports up", be.survey()["ollama"]["up"] is True)
sim = be.detect(prefer="simulated")
check("simulated on request", sim.simulated is True)

print("\n== every lab, live route ==")
for name in labs.ORDER:
    res = labs.run(name, b, {"emails": 2, "rounds": 2} if name == "ladder" else None)
    ok = all(res.get(k) for k in ("title", "aim", "background", "procedure", "runs", "reading", "block"))
    check("lab %s returns a full result" % name, ok, list(res))
    check("lab %s has no facilitator prompt" % name, "ask" not in res)
    check("lab %s json-serialisable" % name, bool(json.dumps(res)))
    if name != "route":
        check("lab %s lists its materials" % name, len(res["materials"]) >= 1)
        sent = [r for r in res["runs"] if r.get("prompt")]
        check("lab %s records the prompts as sent" % name,
              name == "ladder" or len(sent) == len(res["runs"]), [r["label"] for r in res["runs"]])

print("\n== describe needs no model ==")
before = len(CALLS)
for name in labs.ORDER:
    d = labs.describe(name, backend=b)
    check("describe %s" % name, d["aim"] and d["procedure"] and "runs" not in d)
check("describe sends no request", len(CALLS) == before, len(CALLS) - before)

print("\n== the effects each lab measures ==")
ctx = labs.run("context", b, {"num_ctx": 60, "sections": 30})
wide, narrow = ctx["runs"]
check("context: the planted date is in § 1", "15 January 2027" in labs.context_document(3).split("§ 2")[0])
check("context: wide window finds the date", wide["correct"] is True, wide["text"])
check("context: narrow window misses it", narrow["correct"] is False, narrow["text"])
check("context: both runs send the identical prompt", wide["prompt"] == narrow["prompt"])
check("context: the question is at the end of the prompt", wide["prompt"].endswith(labs.CONTEXT_QUESTION))

vary = labs.run("vary", b, {"n": 3, "temperature": 0.9})
cold = [r for r in vary["runs"] if r["settings"]["temperature"] == 0.0]
hot = [r for r in vary["runs"] if r["settings"]["temperature"] > 0]
check("vary: temperature 0 is stable", len({r["text"] for r in cold}) == 1)
check("vary: temperature above 0 varies", len({r["text"] for r in hot}) > 1)

tok = labs.run("tokens", b, {"text": "one two three four five"})
check("tokens: count comes from the server", tok["runs"][0]["prompt_tokens"] == 5)
check("tokens: template tokens counted separately", tok["runs"][0].get("wrapper_tokens") == 3)
tok2 = labs.run("tokens", b)
check("tokens: default text counts both sentences separately", len(tok2["runs"]) == 3)

steer = labs.run("steer", b)
check("steer: run C sends a system prompt", steer["runs"][2]["system"] == labs.STEER_SPEC)
check("steer: runs A and B send none", not steer["runs"][0]["system"] and not steer["runs"][1]["system"])
check("steer: every run is checked", all(len(r["checks"]) == 5 for r in steer["runs"]))

g = labs.run("ground", b)
check("ground: run B carries the source", labs.GROUND_SOURCE in g["runs"][1]["prompt"])
check("ground: run A does not", labs.GROUND_SOURCE not in g["runs"][0]["prompt"])

route = labs.run("route", b)
check("route names the endpoint", endpoint in route["runs"][0]["text"])
check("route shows the request format", "options" in route["materials"][0]["text"])
check("route lists Art. 4 and Annex III", all(any(k in n for n in route["runs"][0]["notes"])
                                             for k in ("Art. 4", "Annex III")))

print("\n== ladder: five stages on the email task ==")
lad = labs.run("ladder", b, {"emails": 2, "rounds": 3})
labels = [r["label"] for r in lad["runs"]]
check("five stages in order", [l.split(" · ")[1] for l in labels] ==
      ["prompt", "skill prompt", "harness", "loop", "wiki"], labels)
s1, s2, s3, s4, s5 = lad["runs"]
check("stage 1 sends no system prompt", not s1["system"] and s1["prompt"].startswith("Answer this email"))
check("stage 2 sends specification and module information",
      "Specification" in s2["system"] and "Portfolio submission deadline" in s2["system"])
check("stage 3 is executed, not described", len(s3["table"]["rows"]) == 2 and s3["items"])
check("stage 3 shows the classification prompt",
      any(b_["label"].startswith("Step 1") for b_ in s3["items"][0]["blocks"]))
check("stage 4 revises a failing draft",
      any(" → " in row[2] for row in s4["table"]["rows"]), s4["table"]["rows"])
check("stage 4 shows the revision prompt",
      any("revision prompt" in b_["label"] for it in s4["items"] for b_ in it["blocks"]))
check("stage 5 reads the lessons", "Lessons recorded from earlier runs" in s5["system"])
check("stage 5 shows the wiki file", any("Lessons from failed checks" in f["text"] for f in s5["files"]))
check("stage 5 inserts the approved answer", "Approved answers" in s5["system"])
only = labs.run("ladder", b, {"stage": "wiki", "emails": 1, "rounds": 2})
check("a single stage can be run on its own", [r["label"] for r in only["runs"]] == ["Stage 5 · wiki"])

print("\n== checks ==")
good = ('The phrase "quite good" is vague: it gives no measure.\n\n'
        "What result did the hypothesis predict, and by how much did the data differ?")
bad = ("**Strengths:**\n* Concise.\n* Clear.\n**Weaknesses:**\n* Vague.\n"
       "Instead, the writer could say 'the results agreed with the model'.")
check("feedback: a compliant comment passes all five", all(c["ok"] for c in checks.check_feedback(good)))
check("feedback: a rewriting, five-point comment fails at least three",
      sum(not c["ok"] for c in checks.check_feedback(bad)) >= 3)

task = tasks.load_task("student_emails")
check("task loads seven emails", len(task.inputs) == 7, [n for n, _ in task.inputs])
email = task.input("02_extension.txt")
src = task.context_text


def em(reply, refer=True):
    return {c["id"]: c for c in checks.check_email(reply, email, src, refer, task.signature_pattern, 150)}


r = em(COMPLIANT)
check("email: compliant reply passes all nine", len(r) == 9 and all(c["ok"] for c in r.values()), r)

# cases observed with gemma3:12b: wrong question answered, translated folder name, English closing
slides = task.input("03_slides.txt")
de_mail = task.input("04_literaturliste.txt")
wrong_topic = ('Dear Chen Wei,\n\nReadings are provided on the learning platform in the course '
               '"EDU-204 2026/27". The reading list is in the folder "Week 0".\n\nKind regards,\nEDU-204 module team')
german_mixed = ('Sehr geehrte Frau Schmidt,\n\ndie Literaturliste finden Sie auf der Lernplattform im Kurs '
                '"EDU-204 2026/27" im Ordner "Woche 0". Die Sprechstunde ist dienstags.\n\nKind regards,\nEDU-204 module team')
german_ok = german_mixed.replace('"Woche 0"', '"Week 0"').replace("Kind regards,", "Mit freundlichen Grüßen")


def em_for(reply, mail, refer=False, open_q=False):
    return {c["id"]: c for c in checks.check_email(reply, mail, src, refer, task.signature_pattern, 150, open_q)}


check("email: answer to a different question fails the topic check",
      not em_for(wrong_topic, slides)["topic"]["ok"])
check("email: open-question sentence is exempt from the topic check",
      em_for("Dear Chen Wei,\n\nThe module team will confirm this separately.\n\nKind regards,\nEDU-204 module team",
             slides, open_q=True)["topic"]["ok"])
sample = task.input("07_sample_size.txt")
ack = ("Dear Noah Fischer,\n\nThank you for your email. A member of the module team will reply "
       "personally.\n\nKind regards,\nEDU-204 module team")
check("email: topic check is not applied to categories reviewed by a person",
      tasks.run_checks(task, ack, sample, "other")[2]["applies"] is False
      and all(c["ok"] for c in tasks.run_checks(task, ack, sample, "other")))
check("email: topic check is applied to automatic categories",
      not {c["id"]: c for c in tasks.run_checks(task, ack, sample, "information")}["topic"]["ok"])
check("email: translated folder name fails the quoted check",
      '"Woche 0"' in em_for(german_mixed, de_mail)["quoted"]["detail"])
check("email: English closing under a German reply fails the frame check",
      not em_for(german_mixed, de_mail)["frame"]["ok"])
check("email: corrected German reply passes", all(c["ok"] for c in em_for(german_ok, de_mail).values()),
      em_for(german_ok, de_mail))
r = em(NONCOMPLIANT)
check("email: promise is detected", not r["decision"]["ok"])
check("email: invented date is detected", not r["dates"]["ok"] and "22 January" in r["dates"]["detail"])
check("email: missing referral is detected", not r["referral"]["ok"])
check("email: missing signature is detected", not r["frame"]["ok"])
check("email: a negated decision is not flagged",
      em("Dear Amira,\n\nWe cannot extend the deadline; only the examination office can.\n\nKind regards,\nEDU-204 module team")["decision"]["ok"])
check("email: date from the email itself is allowed",
      em("Dear Amira,\n\nYou are signed off until 12 January. Please contact the examination office.\n\nKind regards,\nEDU-204 module team")["dates"]["ok"])
check("email: German dates are recognised", (15, 1) in checks.dates_in("bis zum 15. Januar 2027"))
check("email: times are not read as dates", not checks.dates_in("von 10.00 bis 12.00 Uhr."))
check("email: matriculation number is detected", not em(COMPLIANT + " 231077")["identifiers"]["ok"])
check("email: language detection", checks.language(task.input("04_literaturliste.txt")) == "de"
      and checks.language(email) == "en")
check("classification parsing tolerates spacing", tasks.parse_category(task, "Third party.") == "third_party")
check("classification falls back to other", tasks.parse_category(task, "no idea") == "other")
check("open question sentence is recognised",
      tasks.has_open_question(task, "Dear Chen,\n\nThe module team will confirm this separately."))
check("a person-reviewed category is never ready",
      tasks.route(task, "third_party", [], "x", True)[0] == "review")

print("\n== simulated route ==")
for name in labs.ORDER:
    res = labs.run(name, sim)
    check("simulated %s is labelled" % name, res["simulated"] is True)
sctx = labs.run("context", sim, {"num_ctx": 60, "sections": 40})
check("simulated context: wide finds it", sctx["runs"][0]["correct"] is True)
check("simulated context: narrow misses it", sctx["runs"][1]["correct"] is False)
slad = labs.run("ladder", sim)
check("simulated ladder: loop improves the drafts",
      any(" → " in row[2] for row in slad["runs"][3]["table"]["rows"]))
check("simulated ladder: approved answer changes a route",
      any(row[4] == "review" and row[5] == "ready" for row in slad["runs"][4]["table"]["rows"]),
      slad["runs"][4]["table"]["rows"])

print("\n== harness ==")
out = TMP / "out3"
recs = run_harness(sim, "student_emails", str(out))
check("stage 3: one file per email", len(list(out.glob("*/*.reply.md"))) == 7)
check("stage 3: the log is written", (out / "log.md").exists())
head = pathlib.Path(recs[0]["file"]).read_text()
for field in ("input", "category", "route", "checks", "model", "temperature", "simulated", "produced"):
    check("provenance header carries %s" % field, re.search(r"^\s+%s\s" % field, head, re.M), head[:500])
check("stage 3: routing ignores checks", "not used for routing" in head)
check("stage 3: person-reviewed categories go to review",
      (out / "review" / "06_flatmate.reply.md").exists() and (out / "review" / "07_sample_size.reply.md").exists())

out4 = TMP / "out4"
recs4 = run_harness(sim, "student_emails", str(out4), loop=3)
check("stage 4: the header records rounds",
      "rounds)" in (out4 / "ready" / "02_extension.reply.md").read_text())
check("stage 4: open question goes to review", (out4 / "review" / "03_slides.reply.md").exists())

out5, wiki = TMP / "out5", TMP / "wiki.md"
log1 = []
run_harness(sim, "student_emails", str(out5), loop=3, wiki_path=str(wiki), log=log1)
w = tasks.read_wiki(wiki)
check("stage 5: lessons written", len(w["Lessons from failed checks"]) >= 1, w)
check("stage 5: open question written", any("03_slides" in e for e in w["Open questions"]), w)
check("stage 5: approved answers untouched", w["Approved answers"] == [])
text = wiki.read_text().replace("## Approved answers\n", "## Approved answers\n\n- " + task.approved_example + "\n")
wiki.write_text(text)
log2 = []
run_harness(sim, "student_emails", str(out5), loop=3, wiki_path=str(wiki), log=log2)
check("stage 5: second run reads lessons and approved answer", "1 approved answers read" in log2[-1], log2[-1])
check("stage 5: approved answer moves the slides email to ready",
      (out5 / "ready" / "03_slides.reply.md").exists() and not (out5 / "review" / "03_slides.reply.md").exists())
check("stage 5: nothing written twice", log2[-1].endswith("0 lessons and 0 open questions added"), log2[-1])
check("stage 5: approved answer kept", tasks.read_wiki(wiki)["Approved answers"] == [task.approved_example])

print("\n== CLI ==")
for argv in (["check"], ["lab", "tokens", "--text", "hello there"],
             ["lab", "context", "--set", "num_ctx=20"], ["lab", "ladder", "--set", "emails=1", "--brief"],
             ["all", "--backend", "simulated"], ["lab", "route", "--json"],
             ["harness", "--backend", "simulated", "--out", str(TMP / "cli"), "--limit", "2", "--loop", "2"]):
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            rc = main(argv)
        check("cli %s" % " ".join(argv[:4]), rc == 0 and len(buf.getvalue()) > 50, buf.getvalue()[-300:])
    except SystemExit as e:
        check("cli %s" % " ".join(argv[:4]), e.code == 0)
    except Exception as e:
        check("cli %s" % " ".join(argv[:4]), False, repr(e))

buf = io.StringIO()
with redirect_stdout(buf):
    main(["lab", "context", "--backend", "simulated"])
o = buf.getvalue()
check("cli prints background, procedure, materials and prompt",
      all(k in o for k in ("Background", "Procedure", "Materials", "user message:", "§ 1 Submission")))
check("cli simulated mode says so", "SIMULATED MODE" in o)
check("cli has no facilitator prompt", "Ask the room" not in o)
buf = io.StringIO()
with redirect_stdout(buf):
    main(["lab", "route", "--json"])
check("cli --json emits valid json", bool(json.loads(buf.getvalue())))
buf = io.StringIO()
with redirect_stdout(buf):
    rc = main(["copy-task", "student_emails", str(TMP / "copy")])
check("copy-task copies the folder", rc == 0 and (TMP / "copy" / "task.json").exists())
check("a copied task folder loads", len(tasks.load_task(str(TMP / "copy")).inputs) == 7)

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
check("no facilitator prompt in the page", "Ask the room" not in html)

s = json.loads(urllib.request.urlopen(base + "/api/survey").read().decode())
check("survey exposes the active route", s["active"]["backend"] == "ollama")
check("survey lists seven labs with titles", len(s["labs"]) == 7 and all(l["title"] for l in s["labs"]))
d = json.loads(urllib.request.urlopen(base + "/api/describe?lab=ladder").read().decode())
check("describe endpoint returns materials", any("Inbox" in m["label"] for m in d["materials"]))


def post(obj):
    req = urllib.request.Request(base + "/api/lab", method="POST", data=json.dumps(obj).encode(),
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read().decode())


check("api runs a lab", post({"lab": "tokens", "params": {"text": "a b c"}})["runs"][0]["prompt_tokens"] == 3)
check("api keeps default text for an empty field",
      post({"lab": "steer", "params": {"task": ""}})["runs"][0]["prompt"] == labs.STEER_TASK)
try:
    post({"lab": "nonsense"})
    check("unknown lab returns an error", False)
except urllib.error.HTTPError as e:
    body = json.loads(e.read().decode())
    check("unknown lab returns an error with a hint", e.code == 400 and "hint" in body)
check("api honours the simulated route", post({"lab": "tokens", "backend": "simulated"})["simulated"] is True)

print("\n== failure when nothing is running ==")
be.DEFAULT_OLLAMA = "http://127.0.0.1:1"
be.DEFAULT_OPENAI = "http://127.0.0.1:2"
check("falls back to simulated", be.detect().simulated is True)
try:
    be.detect(prefer="ollama")
    check("explicit ollama fails loudly", False)
except RuntimeError:
    check("explicit ollama fails loudly", True)
be.DEFAULT_OLLAMA = endpoint

print("\n== model choice when the default is missing ==")
names = ["nomic-embed-text:latest", "mistral-small3.1:24b", "qwen3-vl:8b",
         "gemma3:12b", "llama3.1:8b", "gemma4:latest"]
check("never picks an embedding model",
      be._fallback_model(["nomic-embed-text:latest", "phi3:latest"], "gemma3:4b") == "phi3:latest")
check("prefers the default's family", be._fallback_model(names, "gemma3:4b") == "gemma3:12b")
check("otherwise the smallest text model",
      be._fallback_model(names[:3] + ["llama3.1:8b"], "gemma3:4b") == "llama3.1:8b")

shutil.rmtree(TMP, ignore_errors=True)
print("\n%s" % ("-" * 60))
print("%d checks failed" % len(FAILS))
for f in FAILS:
    print("   - %s" % f)
sys.exit(1 if FAILS else 0)
