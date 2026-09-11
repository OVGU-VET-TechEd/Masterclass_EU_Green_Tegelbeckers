# llmlab

Seven exercises that put claims from **Workshop 4 — AI in Teaching: Tools,
Strategies and Reflection** in front of a model running on the participant's
own machine.

The session asserts a number of things: that a token is not a word, that
material outside the context window is silently absent, that fluency is not
evidence of grounding, that the stage of prompting you work at decides what
survives the term and what you have to govern. Those are checkable claims.
This tool makes each of them checkable in about ninety seconds — and when a
run does not show the claim, it says so rather than asserting it anyway.

No third-party packages. Python 3.9 or later. Windows, macOS and Linux.
Nothing is sent anywhere: llmlab talks to a model service on the loopback
address, or to nothing at all.

The session stands on its own. Nothing here assumes you attended anything
else or installed anything before today, beyond the two steps below.

---

## Before the session

1. **Python 3.9 or later.** Check with `python --version`.
2. **A local model, if you want the live version.** Install Ollama from
   <https://ollama.com>, then pull one small model. The download is about
   3 GB, so do it on a good connection before the day:

   ```bash
   ollama pull gemma3:4b
   ```

Without step 2 everything still runs, in simulated mode, and says so on
every screen.

**Getting the lab.** Download the repository as a ZIP from
<https://github.com/OVGU-VET-TechEd/Masterclass_EU_Green_Tegelbeckers>
(green *Code* button, *Download ZIP*), unzip it, and open `V5/llmlab`.

---

## Install

Pick whichever suits the room.

**Unzip and run** — no installation, no privileges:

```bash
python run.py                    # opens the browser interface
python -m llmlab check           # what is installed and reachable
```

**Install as a command:**

```bash
pip install .                    # or: pip install -e .  while editing
llmlab check
llmlab serve
```

**In VS Code:** open this folder, press <kbd>F5</kbd>, choose *llmlab · open
the browser interface*. Three run configurations are already defined in
`.vscode/launch.json`.

---

## The model

llmlab looks for a model service in this order and uses the first that
answers.

| Route | Where it looks | Set it with |
| --- | --- | --- |
| Ollama | `http://127.0.0.1:11434` | `LLMLAB_OLLAMA` |
| OpenAI-compatible server (llama.cpp, LM Studio, vLLM) | `http://127.0.0.1:8080/v1` | `LLMLAB_OPENAI` |
| Simulated | nothing runs | `--backend simulated` |

It asks for `gemma3:4b` first. If that is not installed it uses whichever
Gemma model is — `gemma:2b`, `gemma3:12b`, `gemma4` all work — and with no
Gemma at all it takes the smallest text model it finds, never a vision or
embedding model. `python -m llmlab check` says on its last line which model
will be used.

To choose a model yourself, add `--model <name>` to any command, or set
`LLMLAB_MODEL` for the session. The labs were tested on Gemma 3 12B and
Llama 3.1 8B. Models differ, and that is part of the point: lab 5 in
particular gives a different result on each, and says which one you got.

**On the simulated route.** If no service answers, llmlab does not stop. It
assembles the text itself and says so on every screen and in every export.
The structure of each result stays true — temperature 0 really is stable, the
narrow window really does lose the code word — but the wording is scaffolding,
not model output. This exists so that one broken laptop does not remove one
participant from the exercise. It is labelled everywhere precisely because
the session teaches people to ask which numbers on a screen are real.

---

## The seven

| # | Command | Claim it tests | Session block |
| --- | --- | --- | --- |
| 1 | `llmlab lab tokens` | A token is not a word, and the gap is measurable | 3.1 |
| 2 | `llmlab lab context` | Material outside the window is absent, and absence is silent | 3.1 |
| 3 | `llmlab lab vary` | Reproducibility is a setting, and the default is not it | 2D, 1 |
| 4 | `llmlab lab steer` | A skill prompt beats a better-worded request — because it stays, not because it writes better | 3, stage 2 |
| 5 | `llmlab lab ground` | A grounded and an ungrounded answer can read the same | 1 |
| 6 | `llmlab lab ladder` | The stage you work at decides what survives — and what you have to govern | 3, stages 1–5 |
| 7 | `llmlab lab route` | Local hosting answers one obligation and not the others | 2 |

Run all seven back to back with `llmlab all`. Add `--json` to any lab to get
the raw result for your own materials.

Every lab prints three things beyond the output: the claim under test, a
reading of what the numbers mean, and the question to put to the room while
the result is on screen. The reading is built from the numbers. If the narrow
window happens to find the code word, or the model declines to answer without
its source, the reading says the run did not show the claim and what to try
next.

---

## The five stages of prompting

The session's Block 3 describes prompting as an evolution in five stages.
Lab 6 walks all five on one paragraph of student writing; the `harness`
command does stages three to five on a folder.

| Stage | What it is | In llmlab |
| --- | --- | --- |
| 1 · Prompt | one request, one answer | `lab ladder`, first run |
| 2 · Skill prompt | an instruction written once and reused | `lab ladder`, `lab steer` |
| 3 · Harness prompt | the specification an agent works inside, with a record | `harness` |
| 4 · Loop prompt | act, check, revise — until a stop condition | `harness --loop 3` |
| 5 · Wiki | the system writes lessons it reads next time | `harness --loop 3 --wiki wiki.md` |

```bash
# stage 3 — one specification, a folder of inputs, one output each with a provenance header
llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out

# stage 4 — the same, revising each output until the five checks pass, three rounds at most
llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out_loop --loop 3

# stage 5 — the same, writing lessons to wiki.md and reading them on the next run; run it twice
llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out_wiki --loop 3 --wiki wiki.md
```

Open one file in the output folder: the header records the input, the
specification, the model, the settings, the time — and with `--loop`, every
round of checks. Then open `wiki.md`. It is a plain markdown file, and it is
everything the system "learned": the model did not change, the file did.
Delete a line and run again, and it forgets.

### The checks are the part worth reading

Labs 4 and 6, and the loop and the wiki, all run on five checks of the written
feedback rules: quotes the words at issue, two points at most, ends with one
question, does not rewrite the text, addresses the writing and not the writer.
They live in `llmlab/labs.py`, in a function called `check_feedback`. Each is a
line or two, and they are crude on purpose: a regular expression that looks for
a quotation mark, one that counts bullet points, one that looks for "could say"
or "revised version". Open the file, read one, and argue with it. Then change
one and run the lab again.

That is the argument of stages four and five in miniature. A loop is only as
good as its checks, and a wiki only as good as whoever reads it. Because the
loop and the wiki use these feedback checks, they fit specifications like
`examples/feedback_spec.md`, not arbitrary ones.

---

## Parameters worth changing live

```bash
llmlab lab context --set num_ctx=128 --set filler_repeats=60
llmlab lab vary --set n=5 --set temperature=1.0
llmlab lab tokens --text "Ihre Prüfungsleistung wurde bewertet."
llmlab lab ground --model gemma3:12b
llmlab lab ladder --set rounds=2
```

The context lab is the one to tune before the session. Raise
`filler_repeats` or lower `num_ctx` until the narrow window fails on your
model. The failure is the demonstration; a run where both windows answer
correctly teaches nothing, and the lab will tell you so.

---

## What it deliberately does not do

- It stores nothing of its own. The only files it writes are the ones you
  name on the command line — the `--out` folder and, at stage five, the
  `--wiki` file — and both are plain text you can open and delete.
- It does not send anything anywhere. The interface loads no fonts, no
  scripts and no styles from outside this process, which is checked in the
  test suite rather than promised in a paragraph.
- It does not evaluate anybody. There is no scoring of people, no profile and
  no progress record, because a tool used in staff development that quietly
  measures staff is the thing the session warns about. The rule checks score
  the model's output, never the person running it.
- It does not tell you a tool is safe. Lab 7 lists which obligations the
  local route removes, which is fewer than people expect.

## Licence

CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab · EU GREEN
Alliance. Funded by the European Union.
