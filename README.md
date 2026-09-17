# AI in Teaching: Tools, Strategies and Reflection

**Workshop 4** of the EU GREEN WP2 Training Lab — a 90-minute masterclass for
teaching staff in higher education, with seven lab exercises that run on a
language model on the participant's own computer.

**Current version: [V7](V7/)** (September 2026). Earlier versions are kept for
reference in `V4/`, `V5/` and `V6/`; the `llmlab/` folder and
`masterclass_ai_in_teaching_v3.html` in the repository root are from version 3
and are no longer maintained.

---

## Version 7 at a glance

| File | What it is | Use it |
| --- | --- | --- |
| [`V7/masterclass_ai_in_teaching_v7_labs.html`](V7/masterclass_ai_in_teaching_v7_labs.html) | Live page: six blocks as key points with *Read more*, and interactive results of all seven labs (gemma3:12b) | On the projector during the session; self-contained, works offline |
| [`V7/workshop4_ai_in_teaching_v7.md`](V7/workshop4_ai_in_teaching_v7.md) | LiaScript self-study course: full text, reference lab results, a quiz per block and a final quiz | Self-study, preparation and follow-up; [open in LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Masterclass_EU_Green_Tegelbeckers/refs/heads/main/V7/workshop4_ai_in_teaching_v7.md) |
| [`V7/pages/`](V7/pages/) | Readiness self-check, tool triage and decision record, 90-day plan | Opened from links in the page and the course |
| [`V7/llmlab/`](V7/llmlab/) | The seven lab exercises (Python 3.9+, no third-party packages) | In a terminal or browser beside the page |
| [`V7/setup_llmlab.py`](V7/setup_llmlab.py) | Guided setup for the lab | Run once before the session |
| `V7/Masterclass_AI_in_Teaching_v7_complete.zip` | Everything in `V7/` in one archive | Download and unpack for offline use |
| `V7/llmlab_v7_backup.zip` | The lab folder and the setup script only | Send to participants; backup of the lab |
| [`V7/REFERENCES.md`](V7/REFERENCES.md) | Bibliography | For sending to people |
| [`RUN_OF_SHOW.md`](RUN_OF_SHOW.md) | Minute-by-minute plan for facilitators | Before and during the session; not participant-facing |

Online (after the repository is published on GitHub Pages):
<https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/masterclass_ai_in_teaching_v7_labs.html>

---

## Lab setup in three commands

Requirements: Python 3.9 or later; for model output, [Ollama](https://ollama.com)
and one small model (about 3 GB). Without Ollama the exercises run in simulated
mode, and every result is marked as simulated.

```bash
cd V7
python setup_llmlab.py          # guided: checks Python, finds or starts Ollama, offers the model download
cd llmlab
python run.py                   # browser interface
```

`python setup_llmlab.py --check` reports without changing anything;
`--help` lists the options (`--model`, `--simulated`, `--install`, `--test`,
`--start`). On macOS and Linux the command may be `python3`.

Manual route, without the setup script:

```bash
ollama pull gemma3:4b
cd V7/llmlab
python -m llmlab check          # which service and model will be used
python -m llmlab all            # all seven exercises in the terminal
```

Details on every exercise, the email task, the automatic checks and the
parameters: [`V7/llmlab/README.md`](V7/llmlab/README.md).

## The seven exercises

| # | Command | What it shows | Block |
| --- | --- | --- | --- |
| 1 | `python -m llmlab lab tokens` | Token count; English and German compared; chat-template overhead | 3 |
| 2 | `python -m llmlab lab context` | Text outside the context window is removed without notice | 3 |
| 3 | `python -m llmlab lab vary` | Temperature and seed decide whether outputs are reproducible | 3 |
| 4 | `python -m llmlab lab steer` | Rules absent, in the request, or in the system prompt | 3 |
| 5 | `python -m llmlab lab ground` | Answers with and without a source read the same | 1 |
| 6 | `python -m llmlab lab ladder` | The five stages of prompting on replies to student emails | 3 |
| 7 | `python -m llmlab lab route` | The deployment route and the obligations that depend on it | 2 |

## Changes in version 7

- The live page shows key points only; the full explanatory text is behind *Read more*.
- The unpublished draft framework (HETAICF v0.11) and the placement map built on it are removed.
- Quick checks and the final check moved from the live page to the LiaScript course, which now carries the full text, a quiz for every block and the reference lab results.
- New: `setup_llmlab.py`, a complete archive and a lab archive.

## Licence

Course material: CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab ·
EU GREEN Alliance. Funded by the European Union. Views expressed are those of
the authors alone. See also [`LICENSE`](LICENSE).
