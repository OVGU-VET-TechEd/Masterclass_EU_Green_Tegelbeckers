# Workshop 4 — what changed between v3 and v4

September 2026. EduGreenLabs / OvGU Magdeburg — WP2 Training Lab, EU GREEN Alliance.

Three things were asked for: fold the Fokusgruppe reading list into the session,
add a bibliography, and use the HETAICF structure so participants can see where a
practice places them. All three are done. This file says where each insert landed
and what it costs in minutes, because the session was already over its stated
ninety.

---

## Files

| File | Status |
| --- | --- |
| `masterclass_ai_in_teaching_v4.html` | **new** — v3 plus 12 inserts and two appendices. 90 KB → 172 KB. |
| `workshop4_ai_in_teaching_v4.md` | **new** — LiaScript course. The straight-line version, 12 native quizzes, the router as collapsible blocks. |
| `REFERENCES.md` | **new** — the bibliography standalone, for sending to people. |
| `CHANGELOG_v3_to_v4.md` | this file. |
| `RUN_OF_SHOW.md` | **rewritten in v4.1** for Option A — see the last section. |
| `llmlab/` | **1.1.0 in v4.1** — no lab was added, but four were corrected. See the last section. |
| `pages/` | **new in v4.1** — the three take-home pages the contract promises. |

Counts: disclosure cards 35 → 47, quiz items 13 → 15 (HTML) plus 12 in LiaScript,
sections 6 → 8. Still zero external network calls, zero storage APIs, still prints.

---

## Where each insert landed

### Block 1 — Competences

| § | Insert | Source |
| --- | --- | --- |
| 1.1 | **AI GO!** framework card | Npuls (2025) |
| 1.1 | **Reference Framework 2.0** card | Npuls (2025) |
| 1.1 | **Wissenschaftsrat** card — intellectual sovereignty | Drs. 3319-26, July 2026 |
| 1.1 | *The gap* card rewritten | AI GO! genuinely narrows it. Said so. |
| 1.2 | HETAICF panel now points forward to Appendix A | — |
| 1.3 | **Sycophancy** failure card | Chandra et al. (2026), arXiv:2602.19141 |
| 1.3 | **Learning stall** failure card | Tagide (2026) |
| 1.3 | **Borrowed values** failure card | Golem (2026) |
| 1.3 | Deskilling card extended | Ferdman (2026), *AI & Society* |

Two of these change an argument rather than adding an example, and both are worth
defending in review:

- **The gap card.** v3 claimed no published framework addresses the higher
  education teaching role. AI GO! is addressed to education professionals in
  research universities, so the claim as stated was too strong. It now says the
  residue is *national* — examination regulations, legal frame, supervision — and
  that this residue is small enough to write down. This strengthens the argument
  for local adaptation rather than weakening it, because it makes adaptation
  cheap instead of heroic.
- **Deskilling.** v3's response was "decide in advance and in writing what you
  will keep doing by hand". Ferdman's *capacity-hostile environments* shows why a
  written personal intention is not enough: the environment does the work.
  The card now ends on **write the environment, not the intention**, and Block 4
  question one was rewritten to match. This is the most substantive change in v4.

### Block 2 — Tools

| § | Insert |
| --- | --- |
| 2.7 | **Typology, not a tool list** card (ZML/KIT didactic chatbot types) |
| 2.7 | **Somebody else's written policy** card (UC Berkeley Law; edu-sharing legal FAQ) |
| 2.7 | **Where to send people** card (DigiStudi, Elements of AI, twillo OER, KI:Expertisezentrum.nrw) |
| new | **The resource question this session under-covers** panel |
| new | **Feedback: the choice between two failures** panel (Krommer 2026) |
| new | **Agents change what an online test measures** panel (HFD 2026; Moodle field notes) |

The resource panel exists because this is a green-alliance workshop that had
nothing on energy. It is deliberately framed as an admission with three concrete
actions rather than as a section, because Foundation level is all it reaches and
padding it would be dishonest.

### Block 3 — Strategies

| § | Insert |
| --- | --- |
| 3.5 | **AI as a reflection instrument** card (FH Aachen) |
| 3.5 | **The misunderstanding that blocks the work** card (Wampfler 2026) |
| 3.5 | **A book that is its own case study** card (Lehrwende, with the Fokusgruppe's own observation attached) |
| new | **Verification tooling, and the loop it creates** panel (BibFox, CheckIfExist, Forschung & Lehre) |

### Block 4 — Reflection

- **The name for what question one is asking** — Wissenschaftsrat's intellectual
  sovereignty read against Ferdman. Ties the two national/theoretical additions
  into the reflection the session already ran.
- **Turning the reflection into two competence identifiers** — routes to Appendix A.

### Block 5 — Commitment

- *Further reading* replaced by a pointer to Appendix B and a named three-item
  starting set.

---

## Appendix A — the placement map

The part that needed a design decision. HETAICF v0.11 is unpublished and under
review, and the standing rule in this course has been ninety seconds and do not
cite it. Using it as the spine of an appendix looks like a reversal, so here is
the reasoning.

**What is used:** the structure only — four domains, three obligations in
Stratum X, three levels, five objects, and the dual reading. **What is not used:**
any claim that a numbered competence is authoritative. The warning panel is the
first thing in the appendix, it is red, and it says the identifiers will change.

**Why do it at all:** because "which specific thing can you not yet do" was
already the stated purpose of Block 1, and v3 never answered it for anybody. A
vocabulary makes the answer sayable. If OvGU adopts a different framework next
year the exercise survives; only the labels change. That is the same argument the
session makes about local adaptation, applied to itself.

**What is in it:**

1. The structure, as a table and an SVG.
2. **The router** — 12 practices, from *I paste student work into a commercial
   assistant* to *I do not use AI at all*. Each shows the competences you are
   exercising with the level, the ones you needed first, the legal floor engaged,
   where in the session it is treated, and what to read. Vanilla JS, no storage.
3. **The coverage table** — all 22 competences, the level this course honestly
   reaches, where, and what is missing. Four are marked *not reached*.
4. **The self-study route** — the five ASSET LiaScript modules mapped to the
   competences they cover, so you have something to send the people who did not
   come.
5. Two quiz items.

The two router entries most likely to start an argument in the room are
**detectors** (which returns "this is a decision, not a level") and **I do not
use AI at all** (which returns that reasoned non-use is itself a competence, and
that three obligations apply anyway). Both are deliberate.

---

## Appendix B — references

53 items in seven groups: frameworks, policy, law, how the systems fail, teaching
practice, open offers, and this workshop series. Everything cited anywhere is in
it. Items with no stable link say so.

Four were verified against the source rather than taken from the reading list as
given: the Wissenschaftsrat drawing number and DOI, the Ferdman article and its
volume, the Chandra et al. arXiv identifier and its two negative results, and the
addressee of AI GO!. The rest are cited by title and URL as circulated.

---

## Timing — read this before you next deliver it

v3 was a ninety-minute session with an honest runtime nearer 100–105. **v4 adds
roughly 11 minutes of material to the blocks**, which makes the honest runtime
about 115 and the stated ninety a fiction.

Two ways to handle it, and you have to pick one:

**Option A — keep ninety minutes.** Treat everything marked *new in v4* as
reading, with three exceptions worth the floor time:

- the **sycophancy** card (90 s) — it is the only new item that changes what
  someone does on Monday, because it removes "I checked it with the AI";
- the **Ferdman** sentence in the deskilling card (30 s) — it changes the answer
  to Block 4's first question, which is a load-bearing moment;
- **Appendix A's router**, run live for two practices only (4 min), between
  0:24 and 0:27 where Lab 5 currently sits, or in place of the Block 1 HETAICF
  minute.

That is six minutes. Take them from the cut list already in `RUN_OF_SHOW.md`:
items 2 and 3 (labs `ground` and `route`) release six minutes exactly, and both
are already marked as cuttable.

**Option B — make it 120 minutes** and run the router properly, with the show of
hands, at 1:22 in place of the CPD plan page. The plan then comes out of the
router's amber column, which is better than the generic version and is the reason
the appendix exists.

**Do not** try to keep everything and finish on time. The four never-cut items
are unchanged: lab 2 (`context`), the legal panel, the deskilling card, and the
Block 4 statement that Create is not reachable.

---

## Open questions for you

1. **The gap claim.** Are you comfortable conceding AI GO!? It is the honest
   position and it makes Block 1 shorter, but it costs the rhetorical punch of
   "none of them was written for you."
2. **HETAICF exposure.** Appendix A gives the draft far more surface than the
   ninety seconds the design principle allows, even hedged. If the working group
   would rather it stayed at ninety seconds, the appendix can be relabelled with
   generic domain names (Engage / Create / Manage / Shape are AILit's, not
   HETAICF's) and the identifiers dropped — about an hour's work, and the router
   still functions.
3. **The energy section** is thin, and the coverage table says so. If EU GREEN
   reporting needs more than an admission, that is a block, not a panel.
4. **Language.** Both deliverables are English. Roughly a third of the new
   sources are German. A German edition is a real piece of work rather than a
   translation pass, because the legal panel and the framework cards would need
   different examples, not different words.

---

## v4.1 — fixes from a run-through against a live model

10 September 2026. Every lab was run against Ollama on the facilitator's machine
(Gemma 3 12B, Llama 3.1 8B), and every file the run of show names was opened. The
problems found were of one kind: places where the course said something that the
screen in front of the participant then contradicted. For a session whose argument
is *ask which numbers on a screen are real*, that is the failure that matters most.
Decisions taken: build the missing pages; apply **Option A** (keep ninety minutes).

### llmlab 1.0.0 → 1.1.0

- **The zip was stale.** `llmlab.zip` (3 Sep) predated the 4 Sep model-selection
  fix and, on a machine with an embedding model installed, picked it and failed on
  every lab (`does not support generate`). Rebuilt from the current folder.
- **Readings are built from the numbers.** In v1.0 the `ground`, `steer` and
  `ladder` readings, and part of `context`, were fixed text. With Llama 3.1 the
  `ground` reading said "both answers read the same way" beneath an ungrounded
  answer that plainly declined. Each reading now reports what happened, and says
  "this run does not show the claim" when it does not.
- **`tokens` overstated the count.** Ollama's count includes the chat template
  (23 tokens reported for a 13-token sentence; 43 for 14 on Qwen, which adds a
  default system prompt). The lab now counts the text in raw mode, subtracts the
  start marker, and reports the template tokens separately — which turns out to
  be the more interesting number. The approximation sentence and the equity claim
  are now measured rather than asserted.
- **`steer` did not test its claim.** It compared no instruction with an
  instruction. It now adds the control — the same rules pasted into the request —
  and scores all three. On both models tested, pasted and standing scored the
  same, so the claim is restated honestly: a standing instruction is worth more
  *because it stays, not because it writes better*.
- **Five rule checks** (`check_feedback` in `labs.py`) score the output of `steer`
  and `ladder` against the written rules. They are deliberately crude, a line or
  two each, and the page now points participants at them: this is the course's one
  moment of reading code, and it is the rung-three/rung-four distinction in
  miniature. In the first run they caught rung three rewriting the student's text
  despite "Do not rewrite", and rung two claiming to keep a quotation it dropped.
- **`ground`** now names the EU AI Act in the question (Gemma had answered about
  DORA) and its source carries the verified dates.
- **Model choice.** Default is `gemma3:4b`; if absent, any installed Gemma is
  preferred, then the smallest text model. Embedding models are never picked.
- Tests: 67 → 79 checks, all passing.

### Pages — new

`pages/p1_self_check.html`, `pages/p2_tool_triage.html`, `pages/p4_cpd_plan.html`,
built to the spec in the v2 generation prompt, which had never been produced. The
contract promised three artefacts that had no instrument. Each page is one
self-contained file: no network, no storage, Markdown export, Copy and Print
fallbacks for machines that block downloads. The self-check emits a `W4-PROFILE`
line that seeds the plan; the triage page will not export until the legal
questions its job family triggers are answered, and forces *Decline* on emotion
inference; the plan enforces two areas and exports a calendar file. The file
numbering skips p3 because the original token page became `llmlab`.

### The page and the LiaScript course

- The contract links the three pages, says the decision record is finished within
  the week, and says truthfully how the seven checks are run.
- "The narrow window … tells you which section it found the answer in" described
  the simulated backend, not a model. Replaced with what real models did.
- The ladder caption no longer claims the rungs do not differ in quality; the lab
  measures that they can.
- Labs 4 & 6 now run `ladder` as well as `steer` — `ladder` was never invoked
  anywhere in v4.
- Lab 5 is titled *can* read the same, and says what a declining model means.
- The typo at the HETAICF warning in the LiaScript course is fixed.

### RUN_OF_SHOW.md — rewritten for Option A

File names corrected (`masterclass.html` and `pages/` pointed at nothing). New
minutes: sycophancy and Ferdman at 0:20–0:26, the router at 0:26–0:30, page 2 at
0:34, `ladder` + `harness` at 1:02. `ground` and `route` go home as
`python -m llmlab all`, and the follow-up e-mail says so, which is what keeps
"seven claims checked on your own machine" true. The 0:52 line no longer quotes
simulated output.

### Verified, not changed

Regulation (EU) 2026/1744: published 24 July 2026, in force 27 July; standalone
Annex III to 2 December 2027, Annex I to 2 August 2028; Arts. 4, 5 and 50 not
deferred. The legal panel is correct. Sources:
[Cooley](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/),
[Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/),
[CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/).

### Still open

- `gemma3:4b`, now the recommended pull, was not tested; the labs were tested on
  12B and 8B. Run the day-before checks on it before recommending it to a room.
- The rule checks are heuristics. They will misjudge some outputs. That is stated
  on screen, and it is the invitation to read them, but do not quote their scores
  as measurements.
- Under Option A only four labs run in the room. If the contract's "seven" matters
  more than the router, Option B restores `ground` and `route` to the floor.
