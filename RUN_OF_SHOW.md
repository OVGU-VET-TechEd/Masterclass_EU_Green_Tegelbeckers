# Run of show — AI in Teaching: Tools, Strategies and Reflection · v7

90 minutes, six blocks. Two things on the screen and nothing else:
**`V7/masterclass_ai_in_teaching_v7_labs.html`** in a browser, and **a terminal**
in `V7/llmlab`. The three take-home pages open from links in the page. This file
says which one is up at which minute, and what to do when the room or the
network disagrees with the plan.

What changed for the facilitator in v7:

- The page shows **key points only**. The full text sits behind *Read more* —
  open it only when someone asks. Your talking points are the bullets.
- There is **no placement map and no draft framework** any more (HETAICF was
  removed), so Block 1 is shorter on the floor.
- There are **no quizzes on the page**. Quizzes, the final quiz and the long
  explanations live in the LiaScript course
  (`V7/workshop4_ai_in_teaching_v7.md`), which participants get afterwards.
- Every lab has a **pre-recorded result panel** on the page (gemma3:12b,
  15 September 2026). If a live run fails, you switch to the panel and lose
  nothing but the suspense.

---

## The switching rule, in one line

**The page carries the argument. The lab settles a dispute.**

| Switch to the terminal when… | Stay on the page when… |
| --- | --- |
| The claim is about what the system *does* — tokens, windows, temperature, rules | The claim is about law, policy, equity or pedagogy |
| Somebody has said "surely it just…" out loud | Somebody has asked for your opinion |
| The demonstration is a **failure** you want them to watch happen | The demonstration would only confirm what they already accept |
| You have ≥ 3 minutes and are on schedule | You are more than 4 minutes behind — use the result panel instead |

---

## Before the day

**One week ahead — to participants.** One email, four lines: bring a laptop;
unpack the attached `llmlab_v7_backup.zip`; run `python setup_llmlab.py` in the
unpacked folder and answer its questions (it installs or starts Ollama and
downloads `gemma3:4b` if nothing suitable is there); if anything stays open, come
anyway — the session works in simulated mode, and every result on the page is
pre-recorded as well. Add the LiaScript link for those who want to prepare:
<https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Masterclass_EU_Green_Tegelbeckers/refs/heads/main/V7/workshop4_ai_in_teaching_v7.md>

**One day ahead — yourself.** Do this properly; it is the only preparation that
matters.

```bash
cd V7
python setup_llmlab.py --check --test         # machine, model and test suite in one report
cd llmlab
python -m llmlab lab context                  # the centrepiece: must FAIL in the narrow window
python -m llmlab lab ladder                   # the longest run; note the time it takes
```

Tune `context` until **the narrow window gets the date wrong**. If it still
answers *15 January 2027*, add `--set sections=200` (more regulation text before
the question). Windows much smaller than 1,024 tokens are ignored by current
Ollama versions, so lengthen the document rather than shrinking the window.
Write the working command on a sticky note.

Run `ladder` once and note how many of the nine checks stage 1 and stage 2 pass
on your model, so the room's result does not surprise you. If `check` picks a
model you did not expect, add `--model <name>` to every command or set
`LLMLAB_MODEL` for the session.

Open the three pages in `V7/pages/` in the browser you will project from and
export once from each. Managed laptops sometimes block downloads; if yours does,
**Copy** and **Print** still work, and you will want to know before the room does.

**Fifteen minutes ahead — the room.** Browser at
`V7/masterclass_ai_in_teaching_v7_labs.html`, zoom to ~125 % for projection, all
*Read more* closed (reload the page if in doubt). Terminal open in `V7/llmlab`,
font size up, both windows on the same display so you can switch with one
keystroke.

---

## The 90 minutes

Times are elapsed, not clock. The **screen** column is the only one you need at a
glance.

| Time | Screen | What you are doing | Say this |
| --- | --- | --- | --- |
| 0:00–0:03 | Page · Block 0 | The three bullets and the diagram. Read the three grey boxes aloud; do not elaborate. | "Each pair without the third fails in a way you will recognise." |
| 0:03–0:05 | Page · Block 0 | Open *Outcomes*: the four things they leave with. | "Hold me to these at 1:25." |
| 0:05–0:07 | **Terminal** | Everyone runs `python -m llmlab check` in `V7/llmlab`. Simulated mode is fine for some. | "A model name means a model. *Simulated* means the tool writes the text itself and says so every time. Both work today." |
| 0:07–0:10 | **Page 1** | `pages/p1_self_check.html` from the green box. Eight statements, in silence. Tell them to **Copy** or **Download** before closing: nothing is saved. | "Nobody sees this but you. Keep the last line — the plan at the end is built from it." |
| 0:10–0:15 | Page · Block 1 | The three bullets, then open **two** framework cards: UNESCO AI CFT and AI GO!. Then the level diagram. | "The level structure is shared. The target group is not." |
| 0:15–0:17 | Page · Block 1 | Open *The gap*. | "What is missing for our role is national, and small enough to write down. Adapt; don't reinvent." |
| 0:17–0:24 | Page · Block 1 | The two lead bullets of *Limits of trust*, then open **Sycophancy** and **Deskilling**. Everything else is reading. | "'I checked it with the AI' is not a check — the effect survives a warning." Then: "Change the environment, not your intentions." |
| 0:24–0:27 | **Terminal** or panel | `python -m llmlab lab ground` — or open *Show both answers* in the Lab 5 panel. Let them guess which answer had the source before you reveal it. | "Same confidence, no source named. Only comparison with the source tells you which is which." |
| 0:27–0:31 | Page · Block 2 | The four-area diagram. Point at the ordering. | "Ordered by what a mistake costs the student, not by how often you do it." |
| 0:31–0:35 | Page · Block 2 | Open **Administration** and **Evaluation**. Then the bullets of *Publicly available tools* — read the three triage questions aloud. | "A personal account means no agreement. Everything else follows from that." |
| 0:35–0:38 | Lab 7 panel | Show the *Active route* and tick two obligations with the room. Live run only if you are ahead. | "Local removes the processor relationship. Nothing on the AI Act side." |
| 0:38–0:42 | Page · Block 2 | The legal panel: read the six bullets. Then **Page 2**, `pages/p2_tool_triage.html`: pick *Evaluation* and let the room watch the legal questions appear. | "Sixteen extra months to build the process — not sixteen months in which the question does not apply." |
| 0:42–0:47 | Page · Block 2 | Detectors (lead bullets only), then the copyright panel. Equity, resources, feedback and agents are reading. | "The objection survives any accuracy rate, which is why I will not quote you one." Then: "Anonymisation does not touch copyright." |
| 0:47–0:51 | Page · Block 3 | The short terms table. Read the **right column only**. | "Every row is here because ignoring it produces an error you can make without noticing." |
| 0:51–0:57 | **Terminal** | Labs 1, 2, 3 back to back (`lab tokens`, `lab context`, `lab vary`). **Lab 2 is the centrepiece of the session.** In lab 1, point at the template tokens. | "It did not say text was missing. It answered from what it had, with the same confidence." |
| 0:57–1:02 | Page · Block 3 | The five-stage diagram, the email example bullets, then open **Stage 2** and **Stage 4**. | "The stages are not a quality ladder. They differ in what is kept, what runs without you, and what you have to review." |
| 1:02–1:06 | Lab 6 panel, then **terminal** | In the Lab 6 panel, show stage 1 vs stage 2 checks, then stage 3's table: two replies in `ready/` that fail a check. If ahead: `python -m llmlab harness --task student_emails --out out --loop 3` and open one file in `out/`. | "Stage 3 routed a broken reply as ready. Stage 4 caught it — with text patterns, not understanding." |
| 1:06–1:12 | Page · Block 3.4 | The simulation panel bullets, *Purpose and maintenance*, *Legal classification*. | "Name the thing your students cannot currently practise. And who maintains it after you." |
| 1:12–1:15 | Page · Block 4 | The Acquire / Deepen / Create diagram and the levels table. | "This session does not reach Create, and I am not going to pretend otherwise." |
| 1:15–1:20 | Page · Block 4 | The three reflection cards. **Silence for three minutes**; they write. | "One task you keep doing yourself — and where in the module that is fixed. A resolution does not survive a workload model." |
| 1:20–1:25 | **Page 3** | `pages/p3_cpd_plan.html`. Paste the self-check line from 0:07; two areas; enforce the two. Download the calendar file. | "Five areas is a plan you abandon in week three, and then blame yourself for arithmetic." |
| 1:25–1:28 | Page · Block 5 | The four option cards; the commitment sentence. Everyone writes one. | "By a date, I will do a thing, so that a named person can do something." |
| 1:28–1:30 | Page · Block 5 | The summary bullets, then the self-study link. | "The quizzes and the long version are in the course. Do the Block 2 quiz this week." |

---

## The cut list

You will be behind. Cut in this order and nothing essential is damaged:

1. **Live Lab 5 run** (−2). Use the result panel.
2. **Live harness run at 1:02** (−3). The Lab 6 panel shows the same routing.
3. **Block 3.4, the construction example** (−5). It illustrates stage 2 rather
   than arguing for it. Say "it's on the page, read it on the train."
4. **Page 2 at 0:38** (−1). Mention it; they fill it in this week.

**Never cut:** lab 2 (`context`), the legal panel, the deskilling card, and the
Block 4 statement that Create is not reachable. One is the demonstration, one is
the liability, one is the argument, and one is the honesty.

---

## When things go wrong

| What happens | What you do |
| --- | --- |
| Someone's `check` shows simulated mode | Nothing. It is designed for this; the tool says so on every screen. Later: `python setup_llmlab.py` in `V7`. |
| Half the room is in simulated mode | Run the labs yourself on the projector, or use the result panels on the page. You lose the hands-on and keep the demonstration. |
| `check` picks a model you did not expect | Add `--model <name>` to each command. The labs were tested on Gemma 3 12B and Llama 3.1 8B; small models follow rules less reliably, which Lab 6 will show. |
| The narrow context window answers correctly | Say so out loud, run again with `--set sections=200`. If there is no time, open the Lab 2 panel: the recorded run failed as intended. |
| Stage 1 in Lab 6 passes most checks | Say so. The point is not that it fails; it is that from stage 4 onward the failures are caught and logged. |
| A model takes 40 seconds to answer | Talk over it. Say what you expect to come back and why — the prediction makes the result land harder. |
| Ollama is installed but not running | `python setup_llmlab.py` offers to start it; on macOS open the Ollama app. |
| A page will not download | Managed machines block downloads. **Copy** works everywhere, and so does **Print** to PDF. Nothing is lost until the tab is closed. |
| Someone asks for the quiz | It is in the LiaScript course, one quiz per block plus a final quiz. |
| Someone asks for detector accuracy figures | Decline, and explain the refusal: the objection is disproof and unequal errors, not the rate. |
| No network, no projector, nothing works | The page is self-contained and prints. Use **Open everything**, then **Print**: every *Read more* expands. The three take-home pages print too. |

---

## What each file is for

| File | Use it |
| --- | --- |
| `V7/masterclass_ai_in_teaching_v7_labs.html` | Live, on the projector. Self-contained; works offline; no storage. Contains the recorded lab results. |
| `V7/pages/p1_self_check.html` | Readiness self-check, at 0:07. Exports Markdown; its last line seeds the plan. |
| `V7/pages/p2_tool_triage.html` | Tool triage and decision record, at 0:38. Will not export until the legal questions for the chosen area are answered. |
| `V7/pages/p3_cpd_plan.html` | 90-day plan, at 1:20. Exports Markdown and a calendar file. |
| `V7/llmlab/` | In a terminal beside the browser, at the marked moments. |
| `V7/setup_llmlab.py` | Guided setup; `--check` for a report without changes. |
| `V7/llmlab_v7_backup.zip` | The lab and the setup script. What participants get; also your backup. |
| `V7/Masterclass_AI_in_Teaching_v7_complete.zip` | Everything in `V7`, for offline use or a spare laptop. |
| `V7/llmlab/README.md` | Send to participants afterwards; it is written for them. |
| `V7/workshop4_ai_in_teaching_v7.md` | The LiaScript course: full text, reference results, quizzes. For self-study and OER re-publication. |
| `V7/REFERENCES.md` | The bibliography, for sending to people. |
| This file | Yours. Not participant-facing. |

---

## Afterwards

Send four things within 24 hours, while the commitment sentence is still true:

1. The link to the page, the LiaScript course and `llmlab_v7_backup.zip`.
2. One command for the labs that were shown from panels only:
   `python -m llmlab all` runs all seven on their own machine.
3. One line naming the people who said they would mentor someone, with their
   permission. Remind everyone that the decision record is due this week.
4. The date of the next workshop, if it exists yet. If it does not, say when it
   will.

Then re-run `python -m llmlab lab context` yourself a week later with different
numbers, and see whether you can still explain what it is doing. If you cannot,
that is the deskilling card arriving on schedule — put the re-run in your
calendar now.

---

CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab · EU GREEN Alliance.
