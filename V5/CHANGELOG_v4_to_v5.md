# Workshop 4 — what changed between v4 and v5

September 2026. EduGreenLabs / OvGU Magdeburg — WP2 Training Lab, EU GREEN Alliance.

Three corrections were asked for, and all three are made in this folder. V4 is
left untouched, together with the `llmlab/` and `RUN_OF_SHOW.md` at the repository
root that belong to it; V5 carries its own copies of both.

---

## Files

| File | Status |
| --- | --- |
| `masterclass_ai_in_teaching_v5.html` | v4 plus the corrections below. |
| `workshop4_ai_in_teaching_v5.md` | The LiaScript course, same corrections. Embedded pages now load from GitHub Pages. |
| `pages/p1_self_check.html`, `pages/p2_tool_triage.html` | Copied from v4. |
| `pages/p3_cpd_plan.html` | Was `p4_cpd_plan.html`. Renamed so the file number matches "page 3 of 3". |
| `llmlab/` | 1.2.0 — the ladder lab has five stages; the harness gains `--loop` and `--wiki`. |
| `RUN_OF_SHOW.md` | Rewritten for v5, still Option A. |
| `REFERENCES.md` | New groups for the tools and for the prompting evolution; the workshop-series group removed. |
| `Link.md` | The online LiaScript link, pointing at V5. |

---

## 1 · Tools were predominantly German

Block 2's administration card named GWDG, HAWKI and local models: two German
services and a runtime. It now sorts tools by **route** and gives examples from
several systems:

- **Institutional and national platforms** — SURF's EduGenAI (Netherlands; national
  pilot, general availability planned around the end of 2026, explicitly not for
  assessment or fraud detection), GWDG Chat AI (Germany), and self-hosted open
  front ends: Open WebUI (international) and HAWKI (Germany).
- **Licensed education editions** — Microsoft 365 Copilot Chat with enterprise data
  protection, Gemini for Education and NotebookLM in Workspace for Education,
  ChatGPT Edu, Claude for Education — with the faults named: non-EU providers,
  terms that move faster than review, exit cost.
- **European and open models** — Mistral (France), Apertus (Switzerland; ETH, EPFL,
  CSCS; Apache 2.0), EuroLLM (EU-funded; all 24 official languages).
- **Local models** — Ollama or LM Studio.

A new panel, **"Public tools anyone can open — and the warning each one needs"**,
covers the tools people use on personal accounts: NotebookLM (now also marketed by
Google as Gemini Notebook), the free tiers of the large assistants, Perplexity,
Elicit/Consensus/Scite, and image and slide generators. Each row gives what the tool
is good for and the specific warning. The general warning heads the panel: on a
personal account no institutional agreement exists.

NotebookLM, EduGenAI, Apertus and EuroLLM were checked against their own pages in
September 2026. The statement that the licensed education editions exclude
training on your data follows the providers' public announcements; the contract
your institution actually signed is what counts, so confirm it there. The
NotebookLM row distinguishes the two cases carefully: under an institution's
Workspace for Education account it is a core service with no human review and no
training on data; on a personal account none of that is the institution's to rely on.

"Where to send people" is international too: Elements of AI, DigiStudi, the UNESCO
frameworks, AI GO! (Npuls), twillo in German; nationally SURF/Npuls, Jisc's National
Centre for AI, KI:Expertisezentrum.nrw as one German example.

## 2 · The session depended on other workshops

The lab setup said "if Workshop 3 left you with Ollama and Gemma, this will find
them". The workshops are standalone, so that never happens. Every dependency and
forward reference is gone:

- The lab setup now gives the full installation: Python, Ollama, `ollama pull
  gemma3:4b`, about 3 GB, before the day — "nothing is assumed from any other
  session". The same text is in the LiaScript course, the llmlab README and the
  e-mail in RUN_OF_SHOW.
- "Workshop 3's stack" → "the route this session's lab uses".
- Four pointers to "Workshop 5" (assessment, agents, the worked example, the
  Wampfler card) and two to "Workshop 2" now say what they mean without sending
  anyone elsewhere.
- The references group "This workshop series" is now "This session".
- The LiaScript introduction says the course stands on its own.
- The RUN_OF_SHOW follow-up no longer promises a Workshop 5 date.

The session keeps its own name, *Workshop 4*, as a label.

## 3 · The prompting ladder had the wrong order

v4's ladder was prompt → loop → skill → harness, where "loop" meant correcting a
chat by hand. That reflects neither how prompting has evolved nor how the agent
tools work. v5 describes **five stages**:

| Stage | What it is | What it leaves behind |
| --- | --- | --- |
| 1 · Prompt | one request — or a chat you correct by hand | nothing reusable |
| 2 · Skill prompt | an instruction written once, saved, loaded when the task comes up | a readable instruction |
| 3 · Harness prompt (for agents) | the specification an agent works inside | a specification and a trail |
| 4 · Loop prompt | act, check, revise — until a stop condition | a log of every round |
| 5 · Wiki for a self-learning setup | the system writes what it learned into pages it reads next time | a knowledge base to govern |

What changed in the page: the diagram (redrawn for five stages), five stage cards,
the Labs 4 & 6 call, the terminology row on training versus inference (which now
points at stage five), the quiz item, the take-aways, the Block 4 table, the
coverage table and four router entries. Chat correction moved into stage one, where
it belongs. The argument is extended rather than replaced: stages still differ in
what survives the session, and now also in how much the system does without you and
what you therefore have to govern.

Sources, in the references: Anthropic's Agent Skills (`SKILL.md`, open standard,
December 2025) for stage two; *Building effective agents* and *Effective context
engineering* for stages three and four; Karpathy's `llm-wiki` gist (April 2026)
for stage five.

### And in the lab (llmlab 1.1 → 1.2)

- **`lab ladder`** walks all five stages on one paragraph. Stage four is a real loop:
  it checks the stage-two draft, asks the model to revise what failed, and stops
  when all five checks pass or after three rounds, logging every round. Stage five is
  a real wiki: the rules stage two missed become lesson lines, the same model reads
  them, and the reading reports the score before and after — "nothing about the
  model changed; a few lines of text did".
- **`harness --loop N`** revises each output until it passes the checks and records
  every round in the header. **`harness --wiki FILE`** writes lessons to a plain
  markdown file and reads it on every run; the header records how many lessons were
  read. Run it twice and the second run reads what the first wrote. Delete a line and
  it forgets.
- The README's "stores nothing" now says precisely what is written: only the files
  named on the command line.
- Tests cover the five stages, the loop's stop condition, the wiki being written,
  read back and not duplicated.

---

## Also fixed

- **Block 4 and page 3 contradicted each other.** Block 4 said the plan came from
  the router's amber column; page 3 seeded it from the self-check, and could not
  accept router identifiers. Now the self-check is the source, the router gives
  optional labels you add as your own tasks, and the page-3 panel sits in Block 4 at
  1:22 where RUN_OF_SHOW uses it, instead of in Block 5.
- **The online LiaScript version showed page source.** The embedded pages were
  loaded from raw.githubusercontent.com, which serves HTML as plain text. They now
  point at GitHub Pages, with a plain link under each as a fallback.
  **This needs GitHub Pages enabled once for the repository** (Settings → Pages →
  deploy from `main`). Until then the embeds show a 404 and the fallback links fail
  too; the HTML page and a local LiaScript preview are unaffected.

## Still open

- Enable GitHub Pages for the repository (see above).
- `gemma3:4b`, the recommended pull, was not tested; the labs were tested on Gemma 3
  12B and Llama 3.1 8B.
- The loop and the wiki run on the five feedback checks, so they fit feedback
  specifications and not arbitrary ones. The page says so.
- 1:02–1:06 is tight with the stage-five run in it. RUN_OF_SHOW has the first run
  done the day before, and the cut list drops the live run first.
- The router in Appendix A has no entries yet for stages four and five ("I let an
  agent loop"; "I use an assistant's memory"). Adding them means placing them against
  the draft HETAICF competences, which should be done with the working group.
- Four of the new reference sites (OpenAI, Jisc, Perplexity, Scite) block automated
  link checks; they were confirmed by search instead.
