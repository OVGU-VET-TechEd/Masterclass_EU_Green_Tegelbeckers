# llmlab

Seven exercises on the behaviour of language models, run against a model on
the participant's own computer. The exercises accompany **Workshop 4 — AI in
Teaching: Tools, Strategies and Reflection** (EU GREEN, WP2 Training Lab).

Each exercise states its aim, gives the technical background, describes the
procedure and lists the texts it sends to the model. The results record every
system prompt and user message as sent, the settings used and the output. The
interpretation is composed from the measured figures; if a run does not show
the expected effect, the interpretation says so.

Requirements: Python 3.9 or later, no third-party packages; Windows, macOS or
Linux. Requests go to a model service on the same computer (loopback address),
or, in simulated mode, to no service at all.

---

## Quick setup

`setup_llmlab.py` in the folder above (`V7/`) runs the installation steps below
one after another: it checks Python, finds or starts Ollama, offers to download
the model, verifies the result with `python -m llmlab check` and can open the
browser interface. It asks before it changes anything.

```bash
cd path/to/V7
python setup_llmlab.py            # guided setup
python setup_llmlab.py --check    # report only, change nothing
python setup_llmlab.py --help     # options: --model, --simulated, --install, --test, --start
```

On macOS and Linux the command may be `python3`.

## Installation

1. Check the Python version: `python --version`.
2. For model output, install Ollama from <https://ollama.com> and download one
   small model (about 3 GB):

   ```bash
   ollama pull gemma3:4b
   ```

3. Download the repository
   <https://github.com/OVGU-VET-TechEd/Masterclass_EU_Green_Tegelbeckers> as a
   ZIP file, unpack it and open the folder `V7/llmlab`. Alternatively, unpack
   `V7/llmlab_v7_backup.zip` (the lab folder with the setup script).

Run without installation:

```bash
python run.py                    # browser interface
python -m llmlab check           # installed and reachable services
```

Or install as a command:

```bash
pip install .
llmlab check
llmlab serve
```

In VS Code, open the folder and press <kbd>F5</kbd>; three run configurations
are defined in `.vscode/launch.json`.

## Model selection

llmlab uses the first service that responds:

| Route | Address | Setting |
| --- | --- | --- |
| Ollama | `http://127.0.0.1:11434` | `LLMLAB_OLLAMA` |
| OpenAI-compatible server (llama.cpp, LM Studio, vLLM) | `http://127.0.0.1:8080/v1` | `LLMLAB_OPENAI` |
| Simulated | no service | `--backend simulated` |

The default model is `gemma3:4b`. If it is not installed, llmlab selects
another Gemma model, otherwise the smallest instruction-tuned text model; vision,
embedding and base models are excluded. `--model <name>` or `LLMLAB_MODEL`
selects a model explicitly. The exercises were tested with Gemma 3 12B and
Llama 3.1 8B; results differ between models.

**Simulated mode.** Without a model service, llmlab produces the texts itself.
Every result is marked as simulated. The procedure and the figures derived
from it (for example, whether a date lies inside the context window, or whether
temperature 0 yields identical outputs) are real; the wording is not model
output.

---

## The seven exercises

| # | Command | Aim | Block |
| --- | --- | --- | --- |
| 1 | `llmlab lab tokens` | Token count of a text; English and German compared; chat-template overhead | 3.1 |
| 2 | `llmlab lab context` | Answer to a question whose source passage lies outside the context window | 3.1 |
| 3 | `llmlab lab vary` | Distinct outputs at temperature 0 with seed versus higher temperature | 2D, 1 |
| 4 | `llmlab lab steer` | Rules absent, in the user message, or in the system prompt | 3, stage 2 |
| 5 | `llmlab lab ground` | Answer with and without a supplied source text | 1 |
| 6 | `llmlab lab ladder` | The five stages of prompting applied to replies to student emails | 3, stages 1–5 |
| 7 | `llmlab lab route` | Processing location and the legal obligations that depend on it | 2 |

`llmlab all` runs all seven in sequence. Options for `lab` and `all`:

- `--full` prints prompts and materials without abridgement,
- `--brief` omits background, procedure and materials,
- `--json` (for `lab`) returns the complete result as JSON,
- `--set key=value` changes a parameter, e.g. `--set num_ctx=2048`.

### Materials used by the exercises

- **Lab 1:** an English sentence and its German translation (*Assessment criteria
  are agreed at programme level.*), or any text given with `--text`.
- **Lab 2:** fictitious examination regulations. § 1 states the portfolio
  deadline (15 January 2027); § 2 onwards contain regulation text without dates.
  The question at the end asks for the deadline. The prompt is sent with an
  8,192-token window and with a narrow window (default 1,024 tokens; 120 sections, about 4,200 tokens in total). Ollama 0.34 does not apply windows much smaller than about 1,024 tokens, so smaller values do not shorten the prompt.
- **Lab 3:** a request for one sentence of feedback on a student paragraph about
  formative assessment, sent four times at temperature 0 with seed 42 and four
  times at temperature 0.8 without seed.
- **Lab 4:** five feedback rules and one sentence from a first-year lab report.
- **Lab 5:** a source text on Regulation (EU) 2026/1744 and a question on the
  application dates of the AI Act.
- **Lab 6:** the task folder `llmlab/tasks/student_emails` (see below).
- **Lab 7:** the request format of the active backend.

---

## Lab 6 and the harness: replies to student emails

### The task

The module team of a fictitious module, *EDU-204 Research Methods in
Education*, receives student emails. The task folder contains:

| File | Content |
| --- | --- |
| `spec.md` | Specification: ten rules for replies (sources only, sentence for open questions, no decisions on extensions or grades, no information about other students, no identifiers, language of the email, salutation and signature, 150 words, answer the question asked, names copied exactly) |
| `context/module_information.md` | Reference document: contact, dates, extension and grade procedures, materials, data protection |
| `task.json` | Five categories with description, handling rule and routing (automatic or person) |
| `inputs/` | Seven emails: exam date, extension due to illness, slides (not covered by the reference document), reading list and office hours (German), grade complaint, request about a flatmate, question on sample size |
| `example_approved_answer.md` | An approved answer on slides, used by lab 6 at stage 5 |

### The five stages

| Stage | Procedure in llmlab | Artefact |
| --- | --- | --- |
| 1 · Prompt | Email 02 sent with "Answer this email:"; no system prompt | none |
| 2 · Skill prompt | Same email; system prompt = specification + reference document | stored instruction |
| 3 · Harness | For each email: classification request, drafting request with the category's handling rule; reply written to `ready/` or `review/` by category, with provenance header | reply files, `log.md` |
| 4 · Loop | Nine automatic checks per reply; failed checks returned with a revision request, up to N rounds; `ready/` only if all checks pass, the category is automatic and no open question remains | log of every round |
| 5 · Wiki | `wiki.md` read before the run and extended after it: lessons from failed checks, open questions; people add approved answers, which later runs use as a source | wiki file |

### Commands

```bash
# stage 3
llmlab harness --task student_emails --out out

# stage 4: check and revise, three rounds at most
llmlab harness --task student_emails --out out --loop 3

# stage 5: with a wiki
llmlab harness --task student_emails --out out --loop 3 --wiki wiki.md
```

After the first stage-5 run, `wiki.md` lists the email on slides under *Open
questions*. Add a line under *Approved answers*, for example the text of
`example_approved_answer.md`, delete the open question and run the command
again. The reply on slides is then answered from the approved answer and, if
all checks pass, placed in `ready/`.

To modify the task, copy it first:

```bash
llmlab copy-task student_emails my_task
llmlab harness --task my_task --out out --loop 3 --wiki my_task/wiki.md
```

### The automatic checks

The checks are defined in `llmlab/checks.py` (`check_email`):

| Check | Implementation |
| --- | --- |
| salutation, signature, closing | first line starts with a salutation; signature and a closing in the reply's language (*Kind regards* / *Mit freundlichen Grüßen*) in the last three lines |
| word limit | word count ≤ `max_words` |
| topic | at least one content word of the subject line (e.g. *slides*) occurs in the reply; required only for automatic categories and not for the open-question sentence |
| dates | every date in the reply occurs in the reference document, an approved answer or the email |
| quoted names | every passage in quotation marks (course, folder, room) occurs verbatim in the sources or the email |
| no decision | no sentence with *I/we* and *grant, extend, approve, change, raise* without negation |
| examination office named | required for the categories *extension* and *grade* |
| language | frequent German and English function words in email and reply |
| no identifiers | no number with six to eight digits |

The topic, quoted-name and closing checks were added after a run with `gemma3:12b` in which all replies passed the original seven checks although one reply answered a different question (readings instead of slides) and one translated a folder name ("Woche 0") and used an English closing under a German reply. A second run showed that the topic check must not apply to categories reviewed by a person: there it led the model to invent a policy ("The module team does not provide guidance on sample sizes"). The revision instruction for a failed topic check therefore asks for the open-question sentence when the sources contain no answer. Checks that are too lenient let errors through; checks that are too strict make the loop produce new errors.

The checks are text-pattern tests and do not interpret content. A reply that
passes them can still be incorrect; a correct reply can fail them. The loop and
the routing inherit these limitations. The five feedback checks used in lab 4
(`check_feedback`) follow the same principle.

---

## Parameters

```bash
llmlab lab tokens --text "Ihre Prüfungsleistung wurde bewertet."
llmlab lab context --set num_ctx=1024 --set sections=200
llmlab lab vary --set n=5 --set temperature=1.0
llmlab lab ground --model llama3.1:8b
llmlab lab ladder --set stage=loop --set emails=7 --set rounds=2
```

Lab 2 depends on the model and the server version. If the narrow window still
returns the correct date, increase `sections` or reduce `num_ctx`. Lab 6 sends
several dozen requests with the default settings; on a laptop without a
dedicated GPU this takes several minutes.

---

## Running the exercises from the terminal

Open a terminal (macOS: *Terminal*; Windows: *PowerShell*; Linux: any shell)
and change to the folder `V7/llmlab`:

```bash
cd path/to/Masterclass_EU_Green_Tegelbeckers/V7/llmlab
python --version                 # 3.9 or later; on macOS and Linux possibly `python3`
python -m llmlab check           # which model service and model will be used
```

### One script per exercise

The folder `scripts/` contains one script per exercise. Each prints its result
in the terminal; `--out FILE` also writes it to a file (`.json`: complete data
with all prompts, settings, outputs and checks; any other extension: the
terminal text).

| Script | Exercise |
| --- | --- |
| `scripts/lab1_tokens.py` | 1 · Tokens |
| `scripts/lab2_context.py` | 2 · Context window |
| `scripts/lab3_vary.py` | 3 · Temperature and seed |
| `scripts/lab4_steer.py` | 4 · Rules in the request or in the system prompt |
| `scripts/lab5_ground.py` | 5 · Grounding |
| `scripts/lab6_ladder.py` | 6 · Five stages of prompting |
| `scripts/lab7_route.py` | 7 · Deployment route |
| `scripts/run_all_labs.py` | all seven exercises |
| `scripts/run_harness.py` | stages 3 to 5 on all seven emails, with reply files and wiki |
| `scripts/run_tests.py` | automated test suite (no model needed) |
| `scripts/build_labs_html.py` | builds `../masterclass_ai_in_teaching_v6_labs.html` from saved results |

```bash
python scripts/lab2_context.py                              # output in the terminal
python scripts/lab2_context.py --out results/lab2.txt       # also as text file
python scripts/lab6_ladder.py --set emails=7 --out results/lab6.json
python scripts/lab4_steer.py --model llama3.1:8b            # choose a model
python scripts/lab3_vary.py --backend simulated             # without a model service
python scripts/lab6_ladder.py --help                        # options and default parameters
```

Common options: `--model NAME`, `--backend auto|ollama|openai|simulated`,
`--set key=value` (lab parameters, see `--help`), `--out FILE`, `--full`
(prompts unabridged), `--brief` (without background and materials).

### All exercises, the harness and the tests

```bash
python scripts/run_all_labs.py --out-dir results            # results/labN_name.json and .txt, summary.txt
python scripts/run_harness.py --stage 5 --out-dir results/harness
python scripts/run_tests.py --out results/tests.txt
```

### Results page for the masterclass

`build_labs_html.py` copies `masterclass_ai_in_teaching_v6.html`, embeds the
saved JSON results and adds an interactive result panel below each lab
description (buttons that reveal the model output, tabs, drop-down lists for
the settings, stages and emails, step-by-step view of revisions). Simulated
results are refused unless `--allow-simulated` is given.

**Note for version 7.** `masterclass_ai_in_teaching_v7_labs.html` was derived
from the v6 results page and shortened by hand (key points with *Read more*,
no quizzes). The script still builds the v6 layout; it needs
`../masterclass_ai_in_teaching_v6.html`, which is in the `V6` folder, not in `V7`.

```bash
python scripts/run_all_labs.py --model gemma3:12b --out-dir results/gemma3-12b
python scripts/lab6_ladder.py --model gemma3:12b --set emails=7 --out results/gemma3-12b/lab6_ladder.json
python scripts/build_labs_html.py --results results/gemma3-12b
```

`run_harness.py` writes `ready/`, `review/`, `log.md`, `run.json` and, at stage
5, `wiki.md` to the output folder. To see the wiki take effect, add an entry
under *Approved answers* in `results/harness/wiki.md` and run the same command
again.

With `gemma3:12b` on a laptop, `run_all_labs.py` takes a few minutes; lab 6 with
all seven emails took about 1.5 minutes in our test.

---

## Scope

- llmlab writes only the files named on the command line (`--out`, `--wiki`,
  `copy-task`). The browser interface stores nothing.
- The browser page loads no external resources; a Content-Security-Policy
  header enforces this, and the test suite checks it.
- The checks evaluate model output. No data about the person using the tool is
  collected.
- Lab 7 lists legal obligations by deployment route. It is not legal advice.

Tests: `python scripts/run_tests.py` or `python test_llmlab.py` (mock model
service, simulated route, harness, command line and HTTP interface).

## Licence

CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab · EU GREEN
Alliance. Funded by the European Union.
