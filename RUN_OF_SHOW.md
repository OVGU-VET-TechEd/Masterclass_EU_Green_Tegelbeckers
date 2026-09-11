# Run of show — AI in Teaching: Tools, Strategies and Reflection · v4

90 minutes, run as **Option A** from `V4/CHANGELOG_v3_to_v4.md`: everything marked
*new in v4* is reading, except three items that get floor time — the sycophancy
card, the Ferdman sentence in the deskilling card, and four minutes of the
Appendix A router. The six minutes come from labs `ground` and `route`, which
leave the floor and go home with the participants.

Two things on the screen and nothing else: **`V4/masterclass_ai_in_teaching_v4.html`**
in a browser, and **a terminal** in the unzipped `llmlab` folder. The three
take-home pages open from links in the page. This file says which one is up at
which minute, and what to do when the room or the network disagrees with the plan.

---

## The switching rule, in one line

**The page carries the argument. The lab settles a dispute.**

Everything on the page is a claim someone in the room could reasonably doubt.
Seven of those claims are checkable in under three minutes on the participant's own
machine; four of them are checked in the room, and the other three go home as one
command. Everywhere else, switching to a terminal costs you attention and buys you
nothing.

| Switch to the lab when… | Stay on the page when… |
| --- | --- |
| The claim is about what the system *does* — tokens, windows, temperature, rules | The claim is about law, policy, equity or pedagogy |
| Somebody has said "surely it just…" out loud | Somebody has asked for your opinion |
| The demonstration is a **failure** you want them to watch happen | The demonstration would only confirm what they already accept |
| You have ≥ 3 minutes and are on schedule | You are more than 4 minutes behind (see the cut list) |

---

## Before the day

**One week ahead — to participants.** One email, three lines: bring a laptop; if you
attended Workshop 3 you already have what you need (llmlab finds any Gemma model
Ollama has); if not, install Ollama and run `ollama pull gemma3:4b` before you come.
Say explicitly that the session works without it, so nobody skips the session over a
failed install. Attach `llmlab.zip`.

**One day ahead — yourself.** Do this properly; it is the only preparation that
matters.

```bash
python -m llmlab check                        # confirm your own machine is live
python -m llmlab lab context --set num_ctx=256
python -m llmlab lab ladder
```

Tune the second one until **the narrow window gets the answer wrong**. Raise
`filler_repeats`, or lower `num_ctx`, until it fails on your model. A run where both
windows answer correctly is a run that teaches nothing, and you will not have time to
tune it live. The lab now says so itself if it happens, but write the working
numbers on a sticky note anyway.

Run the third once and note how many of the five rules rung three met on your
model, so the room's result does not surprise you. If `check` picks a model you did
not expect, name one on every command with `--model`, or set `LLMLAB_MODEL` for
the session.

Open the three pages in `V4/pages/` in the browser you will project from, and
export once from each. Managed laptops sometimes block downloads; if yours does,
**Copy** and **Print** still work, and you will want to know before the room does.

**Fifteen minutes ahead — the room.** Browser at `V4/masterclass_ai_in_teaching_v4.html`,
zoom to ~125% for projection, **Facilitator notes off** if you are projecting to the
room and on if you are on a second screen. Terminal open in the `llmlab` folder, font
size up, window placed so you can switch with one keystroke. Both windows on the same
display: alt-tab is faster and less error-prone than dragging between screens.

---

## The 90 minutes

Times are elapsed, not clock. The **screen** column is the only one you need at a
glance.

| Time | Screen | What you are doing | Say this |
| --- | --- | --- | --- |
| 0:00–0:03 | Page · Block 0 | The three-word diagram. Read the three red boxes aloud, do not elaborate. | "Each pair without the third fails in a way you will recognise." |
| 0:03–0:05 | Page · Block 0 | Open the two concept cards: who this is for, the contract. | "This is what you leave with. Hold me to it at 1:25." |
| 0:05–0:07 | **Terminal** | Everyone runs `python -m llmlab check`. Amber output is fine and expected for some. | "Green means a model. Amber means the tool writes the text itself and says so every time. Both work today." |
| 0:07–0:10 | **Page 1** | `pages/p1_self_check.html`, from the link under the lab box. Eight statements, in silence. Tell them to press **Copy** or **Download** before closing: nothing is saved. | "This is UNESCO's own Acquire-level activity. Nobody sees it but you. Keep the last line — the plan at the end is seeded from it." |
| 0:10–0:16 | Page · Block 1 | The framework cards. **Open two, not seven.** UNESCO AI CFT and AILit are enough to make the point. | "The grammar is shared. The addressee is not." |
| 0:16–0:18 | Page · Block 1 | The level-alignment diagram, then the gap card. | "AI GO! is the closest thing written for your role. What it leaves out is national, and small enough to write down." |
| 0:18–0:20 | Page · Block 1 | HETAICF. **Ninety seconds, then move.** | "Unpublished, in review, numbering will change. It is the vocabulary of Appendix A, not a source. Do not cite it." |
| 0:20–0:26 | Page · Block 1 | The failure cards. Open **sycophancy** (90 s) and **deskilling** last; read the Ferdman sentence and leave the card open. Everything else new here is reading. | "'I checked it with the AI' is not a check — the effect survives a warning." Then: "Write the environment, not the intention." |
| 0:26–0:30 | Page · Appendix A | The router, live, **two practices only**: *I paste student work into a commercial assistant*, then one the room volunteers. | "Read the amber column. That is what you needed first." |
| 0:30–0:34 | Page · Block 2 | The four-family diagram. Point at the ordering. | "Ordered by what a mistake costs the student, not by how often you do it." |
| 0:34–0:39 | Page · Block 2, then **Page 2** | Open **administration** and **evaluation**. Then 60 seconds on `pages/p2_tool_triage.html`: pick *Evaluation* and let the room watch the blocking questions appear. | "The decision record starts here and is finished this week. Send it to whoever will hold you to the review date." |
| 0:39–0:44 | Page · Block 2 | The legal panel. Read the five provisions, then the deferral paragraph. | "Sixteen extra months to build the process. Not sixteen months in which the question does not apply." |
| 0:44–0:47 | Page · Block 2 | Detectors, then the equity panel, then the copyright panel. Do not linger. | "The objection survives any accuracy rate, which is why I will not quote you one." |
| 0:47–0:52 | Page · Block 3 | The terminology table. Read the **third column only** — they can read the first two. | "Every row is here because not having it produces a specific error you can make without noticing." |
| 0:52–0:58 | **Terminal** | Labs 1, 2, 3 back to back. **Lab 2 is the centrepiece of the session.** In lab 1, point at the template tokens. | "It did not say it could not see it. It gave a wrong answer with the same confidence as the right one." |
| 0:58–1:02 | Page · Block 3 | The ladder diagram and the four rung cards. | "The rungs are not mainly a quality ladder. They differ in what survives the session, and in whether the output can be checked against anything written down." |
| 1:02–1:06 | **Terminal** | `lab ladder`, then the `harness` command. Point at rung three's `checks:` line. Open one file in `out/`. | "Rung three is the only one with its rules written down, so it is the only one we can check. If it missed one, that is the point: the miss is visible, and fixable in one place." |
| 1:06–1:12 | Page · Block 3.4 | The worked example. Open the two-literacies table; read the three pedagogical decisions. | "Nothing here is specific to construction. Name the thing your students cannot currently practise." |
| 1:12–1:18 | Page · Block 4 | The Acquire/Deepen/Create diagram, then the three reflection questions. **Silence for two minutes.** | "One task you will keep doing by hand — and the change to the environment that protects it. A resolution does not survive a workload model." |
| 1:18–1:22 | Page · Block 4 | The level-mapping table. Read the third column aloud, including the red cells. | "This session does not reach Create, and I am not going to pretend otherwise." |
| 1:22–1:25 | **Page 3** | `pages/p4_cpd_plan.html`. Paste the self-check line from 0:07; two areas; enforce the two. Download the calendar file. | "Five areas is a plan you abandon in week three, and then blame yourself for arithmetic." |
| 1:25–1:29 | Page · Block 5 | Closing quiz, four items, out loud, hands up. | — |
| 1:29–1:30 | Page · Block 5 | The commitment sentence. Everyone writes one. | "By a date, I will do a thing, so that a named person can do something." |

---

## The cut list

You will be behind. Labs `ground` and `route` are already off the floor under
Option A. Cut further in this order and nothing above is damaged:

1. **Block 1's HETAICF minute** (−2). It is the vocabulary of Appendix A, which the
   router already shows.
2. **The router down to one practice** (−2).
3. **Block 3.4, the worked example** (−6). Painful, but it is an illustration of rung
   four rather than an argument for it. Say "there is a worked example on the page,
   read it on the train."
4. **Two of the four closing quiz items** (−2).

**Never cut:** lab 2 (`context`), the legal panel, the deskilling card with the
Ferdman sentence, and the Block 4 statement that Create is not reachable. Those four
are the session's load-bearing walls — one is the demonstration, one is the
liability, one is the argument, and one is the honesty. Of the new material, the
sycophancy card goes last: it is the only v4 item that changes what someone does on
Monday.

---

## When things go wrong

| What happens | What you do |
| --- | --- |
| Someone's `check` shows amber | Nothing. It is designed for this. Point at the amber banner and say the tool will tell them on every screen. |
| Half the room shows amber | Run the labs yourself on the projector and have them watch. You lose the hands-on and keep the demonstration. |
| `check` picks a model you did not expect | Add `--model <name>` to each command. The labs were tested on Gemma 3 12B and Llama 3.1 8B; smaller models are slower to follow rules, which the ladder lab will show. |
| The narrow context window answers correctly | The lab says so. Say it out loud too, raise `filler_repeats` to 80, run again. A visible retune is better than a demonstration that quietly fails. |
| Rung three meets all five rules | Say so. The point was never that it fails; it is that, unlike rungs one and two, it can be checked. |
| A model takes 40 seconds to answer | Talk over it. Say what you expect to come back and why — the prediction makes the result land harder. |
| A page will not download | Managed machines and embedded frames block downloads. **Copy** works everywhere, and so does **Print** to PDF. Nothing is lost until the tab is closed. |
| Someone asks for detector accuracy figures | Decline, and explain the refusal. It is in the facilitator notes on the page. |
| Someone asks whether HETAICF is official | "No. Unpublished, in review, and its numbers will change. Do not cite it. The mechanism is the transferable part." |
| No network, no projector, nothing works | The page prints. Use **Open everything** then **Print**: every disclosure expands and the facilitator notes come with it. The three take-home pages print too. |

---

## What each file is for

| File | Use it |
| --- | --- |
| `V4/masterclass_ai_in_teaching_v4.html` | Live, on the projector. Self-contained; works offline; no storage. |
| `V4/pages/p1_self_check.html` | Readiness self-check, at 0:07. Exports Markdown; its last line seeds the plan. |
| `V4/pages/p2_tool_triage.html` | Tool triage and decision record, at 0:34. Will not export until the legal questions for the chosen family are answered. |
| `V4/pages/p4_cpd_plan.html` | 90-day plan, at 1:22. Exports Markdown and a calendar file. (The numbering is from the original design; its page 3, a token lab, became `llmlab`.) |
| `llmlab/` · `llmlab.zip` | In a terminal beside the browser, at the marked moments. The zip is what participants get. |
| `llmlab/README.md` | Send to participants afterwards; it is written for them, not for you. |
| `V4/workshop4_ai_in_teaching_v4.md` | The LiaScript course, with the three pages embedded. For self-study and for republishing as OER. |
| `V4/REFERENCES.md` | The bibliography, for sending to people. |
| This file | Yours. Not participant-facing. |

---

## Afterwards

Send four things within 24 hours, while the commitment sentence is still true:

1. The link to the page, the three pages and the lab folder.
2. The three claims that did not get floor time, as one command:
   `python -m llmlab all` runs all seven, including `steer`, `ground` and `route`.
   That is what makes "seven claims checked on your own machine" true for everyone.
3. One line naming the two people who said they would mentor someone, by name, with
   their permission. Public commitment is the cheapest follow-through mechanism there
   is. Remind everyone that the decision record is due this week.
4. The date of Workshop 5, if it exists yet. If it does not, say when it will.

Then re-run `python -m llmlab lab context` yourself a week later with different
numbers, and see whether you can still explain what it is doing. If you cannot, that
is the deskilling card arriving on schedule, and the response is the one on the page:
not a resolution to try harder, but a change to the environment — put the re-run in
your calendar now.

---

CC BY 4.0 · EduGreenLabs / OvGU Magdeburg — WP2 Training Lab · EU GREEN Alliance.
