# llmlab

Seven exercises that put claims from **Workshop 4 — AI in Teaching: Tools,
Strategies and Reflection** in front of a model running on the participant's
own machine.

The session asserts a number of things: that a token is not a word, that
material outside the context window is silently absent, that fluency is not
evidence of grounding, that the rung of the prompting ladder you work at
decides what survives the term. Those are checkable claims. This tool makes
each of them checkable in about ninety seconds — and when a run does not show
the claim, it says so rather than asserting it anyway.

No third-party packages. Python 3.9 or later. Windows, macOS and Linux.
Nothing is sent anywhere: llmlab talks to a model service on the loopback
address, or to nothing at all.

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

Workshop 3 already installed Ollama and pulled a Gemma model, so most
participants need nothing further. llmlab looks for `gemma3:4b` first and, if
that is not there, uses whichever Gemma model is installed — `gemma:2b`,
`gemma3:12b`, `gemma4` all work. With no Gemma at all it takes the smallest
text model it finds, and never a vision or embedding model.

```bash
ollama pull gemma3:4b         # only if you have no Gemma yet; runs on an 8 GB machine
python -m llmlab check        # the last line says which model will be used
```

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
| 4 | `llmlab lab steer` | A standing instruction beats a better-worded request — because it stays, not because it writes better | 3.2 |
| 5 | `llmlab lab ground` | A grounded and an ungrounded answer can read the same | 1 |
| 6 | `llmlab lab ladder` | The rung decides what you still have next term | 3.2, 3.4 |
| 7 | `llmlab lab route` | Local hosting answers one obligation and not the others | 2 |

Run all seven back to back with `llmlab all`. Add `--json` to any lab to get
the raw result for your own materials.

Every lab prints three things beyond the output: the claim under test, a
reading of what the numbers mean, and the question to put to the room while
the result is on screen. The reading is built from the numbers. If the narrow
window happens to find the code word, or the model declines to answer without
its source, the reading says the run did not show the claim and what to try
next.

Three details worth knowing before you run them:

- **Lab 1 counts two things.** The tokens in your text, as the model's own
  tokenizer counts them, and the tokens the chat template wraps around it —
  role markers and, on some models, a whole default system prompt. On a short
  sentence the wrapper can be more than half of what the model receives.
- **Lab 4 runs three versions:** the bare request, the same rules pasted into
  the request, and the rules as a standing instruction. The second is the
  control. If it scores like the third, the words did the work and the
  standing instruction's advantage is that it stays.
- **Labs 4 and 6 check the output against the written rules** — quotes the
  words at issue, two points at most, ends with one question, does not rewrite
  the text, addresses the writing and not the writer.

### The checks are the part worth reading

The five checks live in `llmlab/labs.py`, in a function called
`check_feedback`. Each is a line or two, and they are crude on purpose: a
regular expression that looks for a quotation mark, one that counts bullet
points, one that looks for "could say" or "revised version". Open the file,
read one, and argue with it. Then change one and run the lab again.

That is the whole difference between rung three and rung four. At rung three
the rules are written down, so a person can check them. At rung four the
checks are written down too, so anyone can run them, disagree with them in
public, and improve them.

### Rung four, as an actual command

```bash
llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out
```

One written specification, one folder of inputs, one output file per input,
each carrying a header that records the input, the specification, the model,
the temperature, the seed and the time. Nothing about it is sophisticated.
That is the argument: the difference between rung one and rung four is not
cleverness, it is that this leaves a trail somebody else can audit.

Change one rule in `examples/feedback_spec.md`, run it again into a second
folder, and compare the two outputs file by file.

---

## Parameters worth changing live

```bash
llmlab lab context --set num_ctx=128 --set filler_repeats=60
llmlab lab vary --set n=5 --set temperature=1.0
llmlab lab tokens --text "Ihre Prüfungsleistung wurde bewertet."
llmlab lab ground --model gemma3:12b
```

The context lab is the one to tune before the session. Raise
`filler_repeats` or lower `num_ctx` until the narrow window fails on your
model. The failure is the demonstration; a run where both windows answer
correctly teaches nothing, and the lab will tell you so.

---

## What it deliberately does not do

- It does not store anything. Close the browser and the session is gone.
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
