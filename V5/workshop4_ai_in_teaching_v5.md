<!--
author:   Hannes Tegelbeckers · EduGreenLabs / OvGU Magdeburg
email:    hannes.tegelbeckers@ovgu.de
version:  5.0.0
language: en
narrator: UK English Male
comment:  Workshop 4 of the EU GREEN WP2 Training Lab. AI in higher education
          teaching — tools, strategies and reflection — with a placement map
          against a higher-education AI competence framework.
license:  CC BY 4.0

-->

# AI in Teaching: Tools, Strategies and Reflection

--{{0}}--
Welcome. This is the self-study version of the EU GREEN Training Lab session on
AI in teaching. It stands on its own — nothing from any other session is
assumed — and it carries the same argument as the live session, in a straighter
line, and it adds a placement map so you can see which competences you are
already exercising and which ones you needed first.

<div style="background:linear-gradient(118deg,#e7eefa 0%,#eef2f8 55%,#f1ebf9 100%);border-bottom:2px solid #1a4a88;padding:22px 20px;border-radius:10px;">
<div style="color:#45566a;font-size:0.82em;">EU GREEN · Transformative Teaching and Learning · WP2 Training Lab · Workshop 4 · <strong>version 5</strong></div>
<h2 style="margin:8px 0 4px;color:#1a4a88;">Tools, Strategies and <span style="color:#6b4a9e;">Reflection</span></h2>
<div style="color:#45566a;">For teaching staff in higher education. Mixed disciplines, no coding assumed.</div>
</div>

**The title is not a list of three topics. It is a sequence, and each pair
without the third fails in a way you will recognise.**

| | leads to | | leads to | |
| --- | :---: | --- | :---: | --- |
| **Tools** | → | **Strategies** | → | **Reflection** |
| what exists, and what it costs | | how to steer and when to stop | | what you will still do by hand |

- Tools without strategies is **shopping**.
- Strategies without reflection is **compliance theatre**.
- Reflection without tools **changes nothing on Monday**.

Ninety minutes buys you the first two properly and the beginning of the third.
It does not buy you a transformed module. Anyone who promises that is selling
something.

<div style="border-left:4px solid #7b8b9c;background:#f7f9fb;border-radius:0 8px 8px 0;padding:10px 15px;margin:13px 0;font-size:0.92em;color:#45566a;">
<strong>Facilitator:</strong> Read the three red lines aloud and do not elaborate. They do the work.
</div>

## How to use this course

--{{0}}--
Three ways in, depending on why you are here. Pick one and ignore the others.

**If you are teaching from it.** The live version is `masterclass_ai_in_teaching_v5.html`
with `RUN_OF_SHOW.md` beside it. This file is the self-study and re-publication
version. Everything is CC BY 4.0.

**If you are working through it alone.** Allow about two hours, and run the lab
exercises rather than reading them. Seven of the claims in this course are
checkable on your own machine in about ninety seconds each, and a checked claim
survives the week in a way a read one does not.

**If you want to know where you stand.** Go to
[the placement map](#appendix-a--the-placement-map), pick the practice you
actually do most, and read the amber column. That is your development plan, and
it took ninety seconds rather than a workshop.

### What you need for the labs

The lab is a small Python package called `llmlab`. No third-party packages,
Python 3.9 or later, Windows, macOS or Linux. Nothing is sent anywhere.

```bash
python -m llmlab check          # what is installed and reachable
python run.py                   # or: the browser interface
```

For a live model, install **Ollama** (free, from ollama.com) and one small model
before you start — the download is about 3 GB:

```bash
ollama pull gemma3:4b
```

If nothing answers, the tool assembles the text itself and says so on every
screen — so a broken laptop does not remove you from the exercise.

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB setup &middot; Start it now so downloads happen while you read</div>
<div style="color:#45566a;margin-top:5px;">Green means a live model. Amber means simulated mode, which still works and is labelled everywhere.</div>
</div>

## 0 · Who this is for, and the contract

--{{0}}--
The contract is stated in advance so you can hold the session to it at the end.

You are not being trained as a developer, and this course does not assume you
want to be. It assumes you make decisions — about a tool, an assessment, a
module handbook — that are now technical decisions whether or not you experience
them that way. The competence being built is the competence to make those
decisions and defend them.

**What you leave with:**

1. A readiness profile you filled in yourself, not a score somebody gave you —
   [the self-check page](pages/p1_self_check.html).
2. A decision record for one tool, started in the session and finished within
   the week, in a form your head of programme can read —
   [the tool triage page](pages/p2_tool_triage.html).
3. Seven claims you can check on your own machine rather than take on trust. The
   live session runs some of them in the room; `python -m llmlab all` runs all
   seven.
4. A dated 90-day plan with two areas on it, and no more than two —
   [the plan page](pages/p3_cpd_plan.html).

> **UNESCO AI CFT, Aspect 5.1 — Acquire.** Awareness of teachers' rights and
> obligations in the AI era. Every block in this course carries a tag like this.
> Professional development is not the last item on the agenda; it is what the
> other blocks are for.

### Readiness self-check

Eight statements. For each, pick where you actually are — **Not yet**,
**Acquire**, **Deepen** or **Create** — not where a strategy paper says you
should be. You get a profile back with your two largest gaps named, and the
90-day plan in Block 5 is seeded from it. Nothing you choose is sent anywhere or
saved; export it before you close the page.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p1_self_check.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load here, [open the self-check in its own tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p1_self_check.html).

--------------------------------------------------------------------------------

# 1 · Competences — which frameworks exist, and why you need one

--{{0}}--
A framework is not a compliance document. It is a way of finding out which
specific thing you cannot yet do, so that the next ninety days have a subject.

> **Aspect 5.1 — Acquire.** Self-assessment of readiness for teaching in the AI era.

## 1.1 · Six frameworks, and who each was written for

| Framework | Addressee | What it gives you |
| --- | --- | --- |
| **UNESCO AI CFT** (2024) | school teachers | 5 aspects × 3 levels. Aspect 5 is the spine of this course. |
| **AILit** (2026, OECD/EC) | primary and secondary **learners** | What arriving students will have been taught. |
| **DigCompEdu** (2017) | educators, EU-wide | The 22 competences your institution probably already maps to. Predates generative systems. |
| **DigComp 2.2** (2022) | citizens | Added examples concerning AI systems. |
| **ICT-CFT** (2018) | teachers | The three-level grammar everything else reuses. |
| **AI GO!** (2025, Npuls) | education professionals in **higher education** | The closest published thing to a framework for your role. |

{{1}}
**The grammar is shared. The addressee is not.** Read across a row and you are
comparing levels. Read down a column and you are comparing professions.

{{1}}
| | first level | second level | third level |
| --- | --- | --- | --- |
| ICT-CFT 2018 | acquisition | deepening | creation |
| UNESCO AI CFT 2024 | **Acquire** | **Deepen** | **Create** |
| DigCompEdu 2017 | A1 · A2 | B1 · B2 | C1 · C2 |
| HETAICF v0.11 (draft) | Foundation | Applied | Advanced |

### The gap, and its honest size

The higher education teaching role — with its research obligations, its
examination regulations, its academic freedom and its doctoral supervision —
sits between the addressees above. That gap is the argument for local
adaptation.

**One qualification.** AI GO! narrows it considerably: it is addressed to
education professionals in vocational colleges, universities of applied sciences
and research universities, and it is published. What remains is national —
examination regulations, the legal frame, the supervision relationship. That
residue is small enough to write down, which is the argument for *adapting* a
framework and against writing a new one.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>HETAICF v0.11 — unpublished, in review.</strong><br>A working group at this university is drafting a higher-education-facing framework. Its numbering will change and its identifiers carry no authority. It appears in this course for its <em>structure</em> only — see Appendix A. Do not cite a competence identifier from it.
</div>

### The national frame, if you work in Germany

The Wissenschaftsrat published its recommendations in July 2026 under the
guiding idea of **intellectual sovereignty**: the capacity to judge
independently, critically and with reasons in an algorithmically shaped world.

The sentence to carry into a faculty meeting: the central question is not how
higher education is designed *with* generative AI, but how good higher education
is designed in a world shaped by it.

## 1.2 · Why "AI competence" is not a fourth skill

--{{0}}--
Three layers, and the top one is the thinnest.

| Layer | What it is |
| --- | --- |
| **AI-specific competence** | what the system does, what it cannot be asked, who is accountable |
| **Digital competence** | files, platforms, accessibility, data protection |
| **Pedagogical judgement** | what the assessment is for, what the student has to be able to do |

Almost every hard question in this course turns out to be an old question — is
this assessment measuring what I think it measures, who holds this data, can I
justify this decision to the person affected — asked under conditions that make
it harder to answer. That is why the course is not organised around the
technology.

## 1.3 · Why the outputs cannot simply be trusted

--{{0}}--
Seven failure modes. One is famous and easy to catch. The others survive
checking, because they act on you rather than on the text.

### Fabrication — the easy one

A generated reference list can be checked in five minutes, and everyone now
knows to check it. This failure is architectural rather than a bug to be
patched: the system produces text that fits, and fitting is not the same
relation as being true.

The number of false AI-generated references in research papers is now reported
as rising, and a small industry of checkers has appeared to catch them. Use
them — and then notice the shape of what you have done. You have answered a
tool's failure with another tool, which has its own false-positive rate, its own
data route, and its own obligation to be explained under Art. 4.

### Homogenisation

Thirty essays that are each acceptable and share a structure, a register and a
choice of example. And your own module descriptions, after a term of drafting
them the same way.

### Illusion of consensus

A fluent synthesis of a live disagreement. The disagreement is not reported as
absent. It is simply not reported.

### Automation complacency

Verification effort decays with each output that turns out to be fine. The
failure rate has not changed; your sampling of it has.

### Sycophancy — and why a warning does not help

These systems are measurably biased towards validating what the user has already
said. Put a hypothesis to one and you will be told it is interesting; put the
opposite hypothesis an hour later and you will be told the same.

Chandra and colleagues (2026) model a conversation between a chatbot and an
*ideal Bayesian* user — a hypothetical person who updates perfectly rationally
and should therefore be immune. Even that user spirals into unwarranted
confidence, and the effect survives two obvious fixes: removing the system's
false claims, and telling the user in advance that it is sycophantic.

For teaching, the consequence is narrow and sharp. "I checked it with the AI" is
not a check. And a colleague who has been warned is not thereby protected —
which is why the response has to be procedural, not attitudinal: a second
reader, a disconfirming prompt, a source.

### The learning stall

A student who never reaches the point of productive difficulty never gets the
thing that difficulty produces. The work arrives finished, the confidence
arrives with it, and the capability does not.

### Deskilling — the one that compounds

The judgement you stop exercising is the judgement you need in order to evaluate
the output. The competence that lets you audit the tool is the same competence
the tool relieves you of using, and nothing warns you when it goes.

**And it is structural.** Ferdman (2026) names the mechanism: a
*capacity-hostile environment* is one in which the mediation of a system blocks
the slow cultivation of a capacity. A private resolution to keep marking by hand
does not survive a workload model, a deadline and a tool that is already in the
VLE.

What survives is a change to the environment: a task not routed through the
tool, a review step a person has to sign, a module design in which the
difficulty is the point. **Write the environment, not the intention.**

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 5 &middot; Grounded and ungrounded answers can read the same</div>
<div style="color:#45566a;margin-top:5px;">The same legal question asked twice — once with the source text supplied and once without. Compare the register of the two answers, not their content. Some models decline when they have no source — the good case, and one you cannot count on. The lab says so when it happens; run it again with <code>--model</code> and a second model to see the other case.</div>
</div>

```bash
python -m llmlab lab ground
```

**Ask yourself:** which of these would you have forwarded to a colleague without
checking?

## 1.4 · Check yourself — Block 1

Why does the higher-education gap between the frameworks matter practically?

    [( )] The frameworks contradict each other, so no single one can be followed.
    [(X)] The addressee of each is a different profession, so local adaptation is required rather than optional.
    [( )] Higher education is exempt from the EU AI Act, so a different framework is needed.
    [( )] The frameworks are too old to describe generative systems at all.
    *******************************************************************
    They agree far more than they conflict, and their shared three-level
    grammar is the evidence. What differs is who each was written for.
    UNESCO treats adaptation to context as the implementation route, which
    makes the local step a designed feature rather than a gap in the
    literature.
    *******************************************************************

Of the failure modes above, which is the reason the other six matter?

    [( )] Fabrication, because a false citation can be published.
    [( )] Illusion of consensus, because it misrepresents a field.
    [( )] Homogenisation, because it makes marking harder.
    [(X)] Deskilling, because it removes the capacity you would notice the others with.
    *******************************************************************
    The others are detectable by someone with intact judgement in the
    domain. Deskilling erodes the instrument you would detect them with,
    which is why it compounds — and why the response has to be written into
    an environment rather than held as an intention.
    *******************************************************************

A colleague says: "I always warn my students that the chatbot agrees with
everything, so they are fine." What does the evidence say?

    [( )] Correct — a warned user corrects for sycophancy.
    [(X)] The modelled effect persists even when users are warned and even when the system states no falsehoods.
    [( )] Correct, provided the students are postgraduates.
    [( )] The effect only appears in users who already hold unusual beliefs.
    *******************************************************************
    That is the finding that makes the paper worth citing. Neither removing
    hallucination nor warning the user closed the gap in the model. The
    mitigations that remain are procedural: a disconfirming prompt, a second
    reader, a source outside the conversation.
    *******************************************************************

--------------------------------------------------------------------------------

# 2 · Tools — four job families, and what each one costs you

--{{0}}--
Sorted by the job, not by the vendor. The four families differ in exactly one
way that matters: how much a mistake costs the student.

> **Aspect 5.1 → 5.2 — Acquire to Deepen.** The move happens here, when you stop
> asking what a tool can do and start asking what it obliges you to do.

| Family | What it covers | Stakes |
| --- | --- | --- |
| **Administration** | minutes, agendas, translations, forms — nobody is graded by it | low |
| **Preparation** | slides, reading lists, task variants — you check before it ships | low |
| **In-class** | captioning, translation, polling — students are present and cannot opt out | **Art. 5(1)(f)** nearby |
| **Evaluation** | feedback, marking support, detection — the output lands on a record | **Annex III §3 · GDPR Art. 22** |

Ordered by consequence, not by frequency. **Most of your week is in the top two
bands. Most of your exposure is in the bottom two.**

## 2.1 · The tools, and their faults

### Administration — start institutional

- **Institutional and national platforms.** Several countries now run their own
  front ends for higher education: **SURF's EduGenAI** in the Netherlands, a
  national pilot with open-source and commercial models, due for general
  availability around the end of 2026 and explicitly not for assessment or fraud
  detection; **GWDG's Chat AI** in Germany; and self-hosted open-source front ends
  such as **Open WebUI** or **HAWKI**. Their virtue is the agreement and the
  retention rules, not the model. Their fault: the model catalogue changes, and
  somebody has to run the service.
- **Licensed education editions of the large assistants.** Microsoft 365 Copilot
  Chat with enterprise data protection, Gemini for Education and NotebookLM in
  Google Workspace for Education, ChatGPT Edu, Claude for Education. Where your
  institution has signed, these exclude training on your data. Their faults: the
  providers sit outside the EU, so data residency settles where data is stored
  and not every question about who can reach it; terms move faster than your
  institution's review; and exit costs grow with every module built on one.
- **European and open models.** Mistral (France), Apertus (Switzerland; fully
  open, Apache 2.0, more than a thousand languages) and EuroLLM (EU-funded, all
  24 official EU languages). You can see what they are; the open ones trail the
  frontier on hard tasks, and somebody still has to host them.
- **Local models via Ollama or LM Studio** — the route this course's lab uses.
  Nothing leaves the machine. Its faults are real: smaller models are
  meaningfully weaker at long documents and at languages other than English.

### Preparation — largest gain, smallest risk

You are the reviewer before anything reaches a student, which is what makes this
family safe. **The trap is volume.** Producing four versions of a task is easy;
deciding which one to use is the work, and it did not get easier.

### In-class — one hard stop

Live captioning and translation are the clearest accessibility gains available,
and they degrade in exactly the situation where they matter most: a noisy room,
an unfamiliar accent, technical vocabulary. Announce them as an aid, never as a
record.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>The hard stop</strong><br>Anything that infers emotion from faces, voices or posture in an educational setting. This is not a matter of taste or local policy — it is Art. 5(1)(f), and consent does not cure a prohibition.
</div>

### Evaluation — where the law arrives

Rubric drafting is the safe end: you are writing the instrument, not applying
it. Marking support is the end where a grade is a decision about a person, and
the two questions that follow are whether a human is genuinely in the loop and
whether the student can contest it.

**On feedback specifically**, Krommer (2026) frames the choice as a passage
between two hazards. Feedback general enough to be safely generated is too
general to change what a student does. Feedback specific enough to change what a
student does is specific enough that you must be able to defend every sentence —
which means reading the work, which was the part you were trying to avoid.

The gain is in **drafting** against a skill prompt — a standing instruction —
that you wrote and can defend, never in the last step before it reaches the
student.

### Public tools anyone can open — and the warning each one needs

Your students and colleagues already use these, usually on a personal account.
**On a personal account none of them comes with an agreement your institution
has signed:** no processor contract, no administrator control over what is kept,
no notice when the terms change. Reasonable for your own preparation with public
material; the wrong place for student work, personal data, unpublished research
or anything that reaches a mark.

| Tool | Good for | The warning |
| --- | --- | --- |
| **NotebookLM** (Google; now also marketed as Gemini Notebook) | answers only from sources you upload, with citations; study guides; audio and video overviews | **Grounded is not verified**: a citation can point to the right document and the wrong claim. The audio overview adds emphasis your sources did not contain. Under an institution's Workspace for Education account it is a core service — no human review, no training; on a personal account that protection is not your institution's to rely on. No student work, no copyrighted material. |
| **Free tiers** of ChatGPT, Gemini, Claude, Copilot, Le Chat | drafting, explaining, rephrasing | Free and personal plans may use conversations to improve the models unless you switch that off; settings differ and change. The strongest versions are paid — see the equity section. |
| **Perplexity** and other AI search | web answers with links | A link is not a check: the source may be weak or may not support the sentence it is attached to. |
| **Elicit, Consensus, Scite** | finding and summarising papers | Partial coverage, leaning to open-access English literature; summaries flatten live disagreement. |
| **Image and slide generators** (Canva, Gamma and others) | quick visual material | Unsettled licence position for OER; if students meet generated content as generated, Art. 50 says tell them. |

The test for every row is the tool triage question: *where does the text go, who
has agreed to what, and what happens when it is wrong?*

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 7 &middot; Where the bytes went — and what that does not fix</div>
<div style="color:#45566a;margin-top:5px;">The lab reports its own endpoint and lists which obligations that route triggers. The result most people do not expect is how short the list of removed obligations is.</div>
</div>

```bash
python -m llmlab lab route
```

## 2.2 · The legal panel

--{{0}}--
Five provisions and one date that moved.

- **Art. 4 — AI literacy.** The duty falls on the deploying organisation, which
  for teaching purposes is your institution. It is discharged by staff who can
  explain the tools they use, not by a procurement decision. In application since
  February 2025, **not deferred**.
- **Art. 5(1)(f) — prohibited practice.** Inferring emotions from a person in the
  workplace or in education, outside narrow medical and safety exceptions. A
  prohibition, in application since February 2025.
- **Art. 50 — transparency.** People must be told when they are interacting with
  an AI system or when content is artificially generated. In application since
  2 August 2026.
- **Art. 14 — human oversight.** Attaches to high-risk systems. Oversight must be
  real, informed, and capable of overriding the output. "A human clicked approve"
  is not the test.
- **Annex III §3 — education.** Admission and assignment, evaluating learning
  outcomes, assessing the appropriate level of education, and monitoring
  prohibited behaviour during tests. Grading is squarely among them.

**The date that moved.** Regulation (EU) 2026/1744, the Digital Omnibus on AI,
was published on 24 July 2026 and entered into force on 27 July. It defers
obligations attaching to standalone Annex III high-risk systems from
2 August 2026 to **2 December 2027**, and Annex I embedded systems to
2 August 2028. The stated reason is the late arrival of harmonised standards,
not a change of view about the risk. **Articles 4, 5 and 50 were not deferred.**

Read the deferral as sixteen extra months to build the process, not as sixteen
months in which the question does not apply.

### GDPR Art. 22, in one sentence for a colleague

A person has the right not to be subject to a decision based solely on automated
processing which produces legal effects or similarly significantly affects them —
and a mark is the standard example anyone will reach for. Meaningful human
involvement is the condition, and it has to be involvement by someone with the
authority and the information to reach a different conclusion.

### Tool triage and decision record

Pick one tool you use, or are being asked to use. The job family decides which
legal questions appear: evaluation raises Annex III §3, GDPR Art. 22 and Art. 14
as questions that must be answered before the record exports, and emotion
inference in class stops the record at *decline*. Start it here, finish it this
week, and send it to whoever will hold you to the review date.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p2_tool_triage.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load here, [open the tool triage page in its own tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p2_tool_triage.html).

## 2.3 · Detectors

--{{0}}--
The case against them is not that they are inaccurate. It is that they are
unfalsifiable in use, and that their errors fall unevenly.

**Asymmetric harm.** A missed case costs a mark that should have been lower. A
false accusation costs a student a disciplinary process, a relationship with
their department, and in some cases a visa.

**Unfalsifiability.** Ask what evidence a student could bring that would settle
the matter in their favour. Version history helps and is worth requiring, but it
is also producible by anyone who anticipated the accusation. A procedure in
which the accused cannot construct a disproof is not an academic-integrity
procedure, whatever it is called.

**Uneven errors.** Detector scores respond to features that correlate with
writing that is fluent but unadventurous: shorter clauses, conventional
collocations, low lexical surprise. Those are also features of competent
academic writing by someone working in their second, third or fourth language.
An instrument whose false positives are systematically distributed by first
language is not a weak instrument; it is a different instrument from the one it
claims to be.

<div style="border-left:4px solid #7b8b9c;background:#f7f9fb;border-radius:0 8px 8px 0;padding:10px 15px;margin:13px 0;font-size:0.92em;color:#45566a;">
<strong>Facilitator:</strong> If someone asks for accuracy figures, decline and say why. Quoting a percentage concedes that the question is empirical and invites a rebuttal with a better percentage next term. The objection survives any accuracy rate.
</div>

## 2.4 · Equity, copyright, and the direction nobody checks

**Equity.** The strongest general models are, at present, the paid ones. If a
task can be done better with a subscription than without, the assessment is
measuring disposable income alongside whatever it was meant to measure — and the
effect is invisible in the marks. You cannot require a tool your institution
does not provide.

**Copyright in students' work.** Copyright in a student's examination script,
term paper or thesis belongs to the student. Pasting it into a general
commercial assistant is a use of someone else's protected work, made by you,
usually without their knowledge. This is separate from the data-protection
question and is **not** resolved by anonymising the file, because the work itself
is the protected thing.

> **Practical position:** student work goes to the institutional or local option,
> or it does not go. If you intend to use any external service on submitted work,
> say so in the module handbook before submission, not in the feedback
> afterwards.

## 2.5 · The resource question

--{{0}}--
This is an EU GREEN course, so the thinness of this section should be named
rather than smoothed over.

Every inference has an energy, water and hardware cost, and it is paid whether or
not the output was useful. The framework in Appendix A has a competence for this
and **this course reaches only its Foundation level**.

What you can do this term, honestly:

- prefer the smallest model that passes your test cases rather than the largest available;
- batch rather than re-run;
- do not put a hosted call inside a teaching artefact that a cohort will trigger a thousand times when a cached answer would do.

Lab 7 prints the route, and the route is where the cost lives.

## 2.6 · Agents change what an online test measures

A tool that browses, reads a course page, opens a PDF and submits a form does
not just answer a question faster — it dissolves the assumption that an
unproctored online test measures the person sitting at the keyboard.
Practitioner field notes describe this arriving in ordinary classrooms rather
than in a lab.

Two responses that do not work: detection, and a longer honour code. The
response that does work is a format in which the process is the evidence — a
design question that needs more than a paragraph, and more than this course.

## 2.7 · Two things to take to a departmental meeting

**A typology, not a tool list.** Colleagues arrive with product names. A
typology of didactic chatbot types moves the conversation to what the thing is
*for* — a tutor, a sparring partner, a simulated interlocutor, a first-line
answering service — and each of those has a different failure mode and a
different disclosure obligation. Make people name the type before they name the
vendor. The vendor changes every eighteen months; the type does not.

**Somebody else's written policy.** The UC Berkeley School of Law policy is
worth reading not because it is right for you but because it is the right
*size*: a single faculty, written for its own assessment types, specific enough
to be applied by a marker at 11pm.

**Where to send people.** Students: Elements of AI (University of Helsinki; free,
many languages), or DigiStudi (iMooX, Austria) for German-speaking first-years.
Staff: the UNESCO frameworks read as a checklist, AI GO! from Npuls for the
higher-education role, and in German the twillo OER materials. Nationally: SURF
and Npuls in the Netherlands, Jisc's National Centre for AI in the United
Kingdom, KI:Expertisezentrum.nrw in one German state — find yours before you
build anything.

## 2.8 · Check yourself — Block 2

A supplier offers a lecture-hall system that flags students who appear
disengaged. What is the correct response?

    [( )] Run a data protection impact assessment and proceed if it passes.
    [( )] Use it only with explicit student consent.
    [(X)] Decline: inferring emotions in education is prohibited under Art. 5(1)(f), and consent does not cure a prohibition.
    [( )] Wait until December 2027, when the high-risk obligations apply.
    *******************************************************************
    Article 5 sets prohibited practices, which are not conditions to be
    satisfied. The December 2027 deferral concerns Annex III high-risk
    obligations, not the Article 5 prohibitions, which have applied since
    February 2025.
    *******************************************************************

You want to draft feedback on submitted essays using a commercial assistant.
Anonymising the files handles which problem?

    [( )] Both the data protection question and the copyright question.
    [(X)] Part of the data protection question, and none of the copyright question.
    [( )] The copyright question, since an anonymous work has no author.
    [( )] Neither, because feedback is always a high-risk use.
    *******************************************************************
    Removing the name addresses identifiability. It does nothing about
    copyright, because the protected thing is the work, not the name attached
    to it. Drafting feedback is also not automatically the Annex III
    situation; applying a mark is.
    *******************************************************************

Which of these does running the model on your own laptop actually remove?
(Select all that apply.)

    [[X]] The processor relationship and the transfer of text to a third party.
    [[ ]] The Annex III classification when the output contributes to a grade.
    [[ ]] The Article 50 duty to tell people they are interacting with an AI system.
    [[ ]] The Article 4 literacy duty.
    *******************************************************************
    Hosting answers the transfer question and nothing else. If the output
    feeds a grade it is the same Annex III situation wherever it runs, the
    transparency duty attaches to what the learner is told, and the literacy
    duty falls on the deploying organisation regardless of route.
    *******************************************************************

--------------------------------------------------------------------------------

# 3 · Strategies — the words are the strategy

--{{0}}--
This is not a glossary. Every term below is here because not having it produces
a specific professional error — one you can make without ever noticing.

> **Aspect 5.2 — Deepen.** Autonomous upskilling and peer coaching. This is the
> block that transfers: what you learn here you can teach a colleague on Thursday.

## 3.1 · Six terms, and the decision each one protects

| Term | What it means | What goes wrong without it |
| --- | --- | --- |
| **Token** | the unit the system processes — roughly a word fragment | You budget in pages and are wrong. The same sentence in German or Polish costs more than in English, which is a cost fact and an equity fact. |
| **Context window** | the maximum text available to one call; a hard boundary | You paste a 90-page thesis, get a confident summary, and believe the whole thing was read. What fell outside was not flagged as missing. |
| **Training vs inference** | weights are fixed when you use it; your session does not change them | You believe it "learns from" your corrections, so you correct repeatedly instead of writing the instruction down. You also fear the wrong risk. When a tool does seem to remember, it is reading back text it wrote earlier — a memory or a wiki, stage five below. |
| **Grounding** | whether the answer was produced with the source in front of it | You treat a fluent answer as a lookup. Nothing in the register distinguishes the two. |
| **Temperature and seed** | how the next fragment is chosen, and whether that is repeatable | Two identical scripts receive different comments. In an appeal, "I ran it again and got something else" is the end of your position. |
| **Deployment route** | where the text physically goes | You answer the data protection question and assume you answered the others. |

<div style="border-left:4px solid #7b8b9c;background:#f7f9fb;border-radius:0 8px 8px 0;padding:10px 15px;margin:13px 0;font-size:0.92em;color:#45566a;">
<strong>Facilitator:</strong> If a later edit removes the third column, this becomes a glossary and the course loses its argument for why any of this is strategic rather than trivia.
</div>

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 1–3 &middot; Check three of those rows in six minutes</div>
<div style="color:#45566a;margin-top:5px;">Each lab prints the claim it is testing, then the numbers, then the question to put to the room.</div>
</div>

```bash
# row 1 — a token is not a word, and the model reports its own count
python -m llmlab lab tokens --text "Ihre Prüfungsleistung wurde bewertet."

# row 2 — the same question, two window sizes, one code word in line 1
python -m llmlab lab context --set num_ctx=256

# row 5 — the same prompt four times, at temperature 0 and above it
python -m llmlab lab vary --set n=4
```

**The one to watch is the second.** The narrow window does not answer "I cannot
see it". It answers wrongly, with the same confidence as the correct run — on
the models this was tested on, a single wrong word delivered as if it were the
right one. If a run does admit that something is missing, the lab says so; it
is the rare case. And in the first lab, look at the second number: the tokens
the chat template wrapped around your sentence, which you never typed and which
still count against the window.

## 3.2 · The prompting evolution — five stages

--{{0}}--
The stages are not a quality ladder: a single stage-one answer can be as good as
anything above it. They differ in what survives the session, in how much of the
work the system does without you — and in what you now have to govern.

| Stage | What it is | What it leaves behind |
| --- | --- | --- |
| **1 · Prompt** | one request, one answer — or a chat you correct by hand | nothing reusable |
| **2 · Skill prompt** | an instruction written once, saved, loaded when the task comes up | a readable instruction |
| **3 · Harness prompt** (for agents) | the specification an agent works inside: inputs, tools, limits, record | a specification and a trail |
| **4 · Loop prompt** | the agent acts, checks, revises — until a stop condition you wrote | a log of every round |
| **5 · Wiki** for a self-learning setup | the system writes what it learned into pages it reads next time | a knowledge base to govern |

**Stage 1 — Prompt.** Perfectly appropriate for a one-off. Correcting your way
through a chat is still stage one: something usable, nothing reusable. The error
is using it for something you will do forty more times.

**Stage 2 — Skill prompt.** Name the audience, the scope, the count and the
prohibition. The example used in the lab: *address the writing, never the
writer; quote the words at issue; two points maximum; end with one answerable
question; do not rewrite the passage.* "Skill" is now the agent tools' own word
too — a saved instruction file loaded when a task matches it, as in the
`SKILL.md` format published as an open standard in December 2025. Whatever the
format, it is a colleague-readable artefact. **For most teaching staff this is
the stage that pays off this term.**

**Stage 3 — Harness prompt (for agents).** An agent is a model inside a program —
the harness — that lets it read files, call tools and act in several steps. The
harness prompt is the specification that governs it: which inputs, which tools,
what it must write down, when it must stop and ask. In the lab: one
specification, a folder of inputs, one output per input with a provenance
header. The difference from stage one is a trail somebody else can audit.

**Stage 4 — Loop prompt.** The agent drafts, checks the draft against written
rules, revises what failed, and checks again — until the checks pass or a limit
is reached. What makes it safe is the checks and the stop condition, and both are
yours to write. Every round costs another inference; a loop optimises for its
checks, not for the student; and a model checking its own draft brings its own
blind spots to the checking.

**Stage 5 — Wiki for a self-learning setup.** The weights do not change. What
changes is a set of pages the system writes and reads back next time — lessons,
corrections, conventions. Karpathy's *LLM wiki* (2026) made the pattern popular;
the "memory" of commercial assistants is the same idea with the pages hidden.
Whoever can edit the wiki steers every later answer, errors compound, and
student data must never go in. A wiki you can read and version is a governance
object; a memory you cannot read is not.

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 4 & 6 &middot; Walk the five stages, then run the harness</div>
<div style="color:#45566a;margin-top:5px;">Each run is checked against five of the written rules. Open one file in out/ for stage three, and wiki.md after the second stage-five run: that file is everything the system "learned".</div>
</div>

```bash
# stages 1–5 on one paragraph, each checked against the written rules
python -m llmlab lab ladder

# stage 2 — the same rules pasted into a request, or kept as a skill prompt
python -m llmlab lab steer

# stage 3 — one harness specification applied to a folder of inputs
python -m llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out

# stage 4 — the same, looping until the checks pass, three rounds at most
python -m llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out_loop --loop 3

# stage 5 — the same, writing lessons to a wiki it reads next time (run it twice)
python -m llmlab harness --spec examples/feedback_spec.md --inputs examples/inputs --out out_wiki --loop 3 --wiki wiki.md
```

The checks — quotes the words at issue, two points at most, ends with one
question, does not rewrite, addresses the writing — are a line or two each in
`llmlab/labs.py`, crude on purpose. Open the file, read one, and argue with it.
They are also what the stage-four loop runs against, so a crude check makes a
crude loop. Delete a line from `wiki.md`, run again, and watch it forget.

## 3.3 · A worked example from the upper stages

**Circular construction safety and material twin.** A browser-based simulation
for vocational construction teaching. Live regional weather, a fault developing
across eight sensor channels, three role consultations in sequence, and six
material passports the learner routes to reuse, repair, recycle or quarantine —
with retained mass, avoided carbon and avoided replacement cost moving against a
circularity score. The learner's output is a diagnosis, an action and a **written
justification**. It runs from a static web host with no backend and no key.

### Three decisions in it that are pedagogical, not technical

1. **The architecture is the privacy answer.** No login, no accounts, no
   server-side storage: the learner's decisions never leave the browser. There is
   no personal data to protect because the design does not collect any.
2. **The data labelling is a teaching artefact.** Public weather values are
   marked as live external data; the concrete, strain, crane-tilt, dust and
   electrical channels are marked virtual until physical sensors are connected;
   impact figures are marked educational estimates. Most simulations do not tell
   you which of their numbers are real, and learners generalise from that silence.
3. **The output is a decision record.** A diagnosis, an action and a written
   justification: a process artefact, timestamped and attributable.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>The seduction to resist</strong><br>An artefact like this is enjoyable to build, and that is its principal risk. Before the second one, answer in writing: what teaching problem does this solve that a well-run seminar does not; what does it replace rather than add; and who maintains it when the person who specified it is on sabbatical. A repository nobody has opened since the demo is not an OER — it is a hobby with a licence file.
</div>

**The transferable move.** Nothing above is specific to construction. Pick one
thing your students cannot currently practise because the real setting is too
dangerous, too slow, too expensive or too rare; specify it as a system with an
explicit constraint set; build it in small versioned passes you can actually
read; label what is real and what is simulated; make the learner's output a
justification rather than a score.

## 3.4 · Three positions worth holding

**AI as a reflection instrument.** Rather than asking a system to improve a
draft, ask it to interrogate one: name the claim this paragraph makes, list what
would have to be true for it to hold, say which of those the text does not
establish. The student keeps authorship and gets the questions a supervisor
would have asked in week four rather than week eleven. That is a skill
prompt, not a one-off request — which puts it at stage two.

**The misunderstanding that blocks the work.** Wampfler (2026) argues that
teaching development is stuck on a false premise: that academic writing is the
transcription of finished thought, so automating the transcription is either
harmless or fatal depending on your temperament. If writing is instead the
process by which the thought is formed, both positions collapse, and the question
becomes which parts of that formation the student must go through personally.
That question you can answer for your own module.

**A book that is its own case study.** There is now a German-language book on
higher education in the age of generative AI whose companion material — slides,
podcast episodes — is entirely AI-generated. The observation circulating with it
in our own working group is that the companion material demonstrates precisely
the problems such material has, and that concrete recommendations for action
remain scarce. Take that as the honest test for anything produced this term,
including this course: does it tell you what to do on Monday, and can you tell
which parts were generated?

## 3.5 · Check yourself — Block 3

You paste a 90-page thesis into an assistant and receive a fluent three-paragraph
summary. What is the safest assumption?

    [( )] The whole document was processed, since the summary covers the whole argument.
    [(X)] Some of it may not have been available to the answer, and nothing in the answer will tell you which part.
    [( )] Only the first page was processed, since systems read from the top.
    [( )] It depends on the file format rather than the context window.
    *******************************************************************
    The window is a hard boundary and exceeding it is not reported as an
    error. The output remains fluent and complete-seeming, which is exactly
    the failure the context lab reproduces in thirty seconds.
    *******************************************************************

Which of these is a stage-two artefact — a skill prompt?

    [( )] A well-phrased request that produced an unusually good answer.
    [(X)] A saved instruction naming the audience, scope, count and prohibition.
    [( )] A six-turn conversation that arrived at the right output.
    [( )] A folder of outputs generated from one specification.
    *******************************************************************
    Stage two is the skill prompt: written once, readable by a colleague,
    reusable next year. The six-turn conversation is still stage one. The
    last option is stage three, which adds the folder, the provenance
    headers and the version history.
    *******************************************************************

The construction simulation marks its concrete and strain values as virtual.
Why is that labelling pedagogical rather than a technical disclaimer?

    [( )] It protects the authors from liability if a learner acts on a wrong value.
    [( )] It allows real sensor data to be swapped in later without changing the code.
    [(X)] Learners are asked to justify decisions, and a justification is only assessable if the provenance of the evidence is known.
    [( )] The AI Act requires simulated values in educational software to be labelled.
    *******************************************************************
    The assessed output is the justification. A justification built on
    evidence of unknown provenance cannot be marked, and learners who are
    never told which numbers are real generalise from that silence to every
    other simulation they meet.
    *******************************************************************

--------------------------------------------------------------------------------

# 4 · Reflection — and the route to Create

--{{0}}--
What ninety minutes can honestly deliver, and where the line is.

> **Aspect 5.2 → 5.3 — Deepen to Create.** This block hands the work over rather
> than finishing it.

## 4.1 · Three questions

**Question one — what will you keep doing by hand?**
Name one task you will continue to do unassisted *because* you need to stay able
to do it. Not because assistance is forbidden, and not because you are attached
to it. Because the judgement it exercises is the judgement you will use to
evaluate everything else. Write the task and the reason. If you cannot write the
reason, the task is not the right one.

The Wissenschaftsrat has a name for what this question protects: **intellectual
sovereignty**. Read against Ferdman's capacity-hostile environments, the two give
you the whole answer — sovereignty is what you are protecting, and the
environment, not your resolve, is what protects it. So the answer has to be
written into a module, a deadline or a review step, where somebody else can see
it.

**Question two — which decision would you now make differently?**
One decision, already taken, in the last twelve months. Name the article or the
principle that changes your view, so the answer is transferable to your
colleagues rather than a private correction.

**Question three — who else needs to know this?**
Name one person and one thing to tell them. Peer coaching is not a metaphor in
the Aspect 5 framing; it is the named contextual activity for the Deepen level.

## 4.2 · What this course did, and did not do

| Aspect 5 level | What this course did | What it did not do |
| --- | --- | --- |
| **Acquire** (5.1) | Rights and obligations named with articles; a readiness self-assessment; human-directed use checked on your own machine, all seven claims with `python -m llmlab all`. | Nothing outstanding, if you did the [self-check](pages/p1_self_check.html). |
| **Deepen** (5.2) | Started in two places: the tool decision record, and the skill prompt from stage two. | No peer coaching yet, and no use of data about your own practice to direct your development. |
| **Create** (5.3) | Described, with one worked example, and sized honestly at ninety days. | **Not attempted.** It needs a community, a review cycle and a published artefact. |

<div style="border-left:4px solid #7b8b9c;background:#f7f9fb;border-radius:0 8px 8px 0;padding:10px 15px;margin:13px 0;font-size:0.92em;color:#45566a;">
<strong>Facilitator:</strong> Do not soften this table. A course that claims Create teaches participants that the level means less than it does, which makes the framework useless to them the next time they meet it.
</div>

### Your 90-day plan

Paste the last line of your self-check; your two largest gaps become the two
areas, and the page will not let you add a third. Each area gets two dated tasks
at the level you are aiming for. Edit them, add your own, and download the
calendar file so the dates arrive without you having to remember them.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p3_cpd_plan.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load here, [open the plan page in its own tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V5/pages/p3_cpd_plan.html).

If you want the plan in a vocabulary a colleague at another institution can
read, run the practice you do most in the placement map below and copy the two
identifiers from its amber column into the plan as tasks of your own. They come
from an unpublished draft: use them as labels, not as authority.

Why is Create not reachable in a 90-minute session?

    [( )] It requires programming skills that take longer than 90 minutes to acquire.
    [( )] It is reserved for staff with formal educational development roles.
    [( )] It only applies to institutions with an approved AI strategy.
    [(X)] Its contextual activities require other people, a review cycle and a published artefact.
    *******************************************************************
    Hybrid coaching, designing training for others and co-creating with a
    community all involve people beyond the room. The constraint is social
    and temporal, not technical — which is also why ninety days is a
    realistic unit for it.
    *******************************************************************

--------------------------------------------------------------------------------

# 5 · Commitment and close

--{{0}}--
Two areas. Not five.

A plan with five areas on it is a plan that will be abandoned in week three, and
the abandonment will feel like a personal failure rather than an arithmetic one.

**Four things that are actually available to you:**

1. **Run this session** for your own department. Everything is CC BY. Replace the
   tool examples with the ones your faculty uses and the legal panel stays
   correct. One afternoon to adapt, ninety minutes to deliver.
2. **Mentor one colleague.** One person, four conversations across a term. The
   cheapest item on the list and the one most often skipped.
3. **Publish one artefact.** A task specification, a rubric, a decision record, a
   small simulation — somewhere with a commit history and a licence file.
4. **Join or start a practice group.** Three people and a recurring hour. The
   output that matters is a shared set of decisions with dates and reasons
   attached.

### Write it down before you close this file

> *By [date], I will [specific action] so that [named colleague or group] can
> [outcome].*

A commitment without a date is a preference. A commitment without another person
in it is a private intention, and Aspect 5 is not about private intentions.

## Six lines to take away

- A token is not a word, and the context window is a boundary rather than a setting.
- Fluency is not evidence of grounding, and no amount of rereading the output will settle it.
- Hosting answers the transfer question and none of the others.
- Prohibitions are not conditions: Art. 5(1)(f) is a stop, not a risk assessment.
- The stage you work at decides what still exists next term — and what you now have to govern.
- Tools, strategies, reflection — in that order, or the first two do not hold.

--------------------------------------------------------------------------------

# Appendix A — The placement map

--{{0}}--
Where does what you already do put you, and what did you need first?

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>Read this before you use the map</strong><br>The grid below is the structure of HETAICF v0.11, an unpublished draft under review at this university. Its numbering will change and its identifiers carry no authority. Do not cite them. What the draft is good for — and the only thing it is used for here — is a <em>vocabulary</em>: a way of saying which specific thing you are already doing and which specific thing you needed first. If your institution adopts a different framework next year, the exercise transfers and the numbers do not.
</div>

## A.1 · The structure

Four domains, three obligations that sit outside them, three levels, and five
objects the competences apply to.

| Domain | What it covers | Where it lives in this course |
| --- | --- | --- |
| **Engage with AI** (`E1–E7`) | recognise, describe, evaluate, question | Block 1 — everyone needs at least Foundation, because Art. 4 makes it a legal duty |
| **Create with AI** (`C1–C4`) | ideas, prototypes, prompting, authorship | Block 3 |
| **Manage AI** (`M1–M4`) | use or not use, choose, decompose, monitor | Block 2 |
| **Shape AI** (`S1–S4`) | investigate, test, design data flow, improve | the lab |
| **Stratum X** (`X1–X3`) | the law, scholarly practice, your own development | Block 2 and Block 5 |

**Levels** read across every domain: Foundation → Applied → Advanced
(UNESCO Acquire / Deepen / Create · DigCompEdu A / B / C).

**Two readings.** Every competence carries two: what *you* must be able to do,
and what you must *enable students* to do. Most people are a level lower on the
second, and never notice because nobody asks.

**The legal floor is not a competence.** It is a constraint the framework has to
satisfy — which is why it appears as a stratum rather than a domain, and is
operationalised only in `HET-X1`.

## A.2 · The router — pick what you actually do

--{{0}}--
Twelve practices from this course. Open the one you actually do. Nothing is
stored and nothing is scored.

<details style="border:1px solid #d6dee8;border-left:4px solid #a86a12;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I paste student work into a commercial assistant to draft feedback</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#a86a12;margin:6px 0 4px;">Proceed — but with these first</p>
<p style="margin:0 0 12px;color:#16202b;">You are working at Foundation on one competence and below Foundation on three others, two of which are legal.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Direct and iterate with generative AI systems (prompting as a documented practice).</strong> You are directing a generative system and judging whether the output matches your intent.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Decide whether to use AI based on the nature of the academic task, including reasoned non-use.</strong> You have made a decision about which tasks AI supports — even if you have not written it down.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Apply the legal framework for AI in higher education.</strong> Copyright in the script belongs to the student, and anonymising the file does not touch that. If the output feeds a mark, Annex III §3 and GDPR Art. 22 are in play.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Design AI use attentive to data sources, data selection and information flow.</strong> Know which data leaves the institution during use, and under which retention terms.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-C4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Analyse how AI can safeguard or violate authenticity, authorship and intellectual property.</strong> Disclosure: what you say in the module handbook, before submission rather than after.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> A procedure for accepting, revising or rejecting the draft, rather than editing whatever arrives.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> AI Act Art. 50; Annex III §3 (if it reaches a mark); GDPR Arts. 5, 22; copyright in the student's work.<br><strong>In this course:</strong> Block 2 — evaluation family, the copyright panel and the legal panel.<br><strong>Read:</strong> [KI in der Bildung — Rechtliche Orientierung für Bildungseinrichtungen und Lehrkräfte (FAQ)](https://edu-sharing.atlassian.net/wiki/spaces/OIC/pages/1891565573/) · [KI-Feedback. Oder: die Entscheidung zwischen Skylla und Charybdis](https://axelkrommer.com/2026/07/25/ki-feedback-oder-die-entscheidung-zwischen-skylla-und-charybdis/) · [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #0f7a5a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I use the institutional assistant (GWDG, HAWKI) for administrative text</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#0f7a5a;margin:6px 0 4px;">A reasonable place to be</p>
<p style="margin:0 0 12px;color:#16202b;">The safest starting point in the catalogue, and it already covers three competences at Foundation.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Direct and iterate with generative AI systems (prompting as a documented practice).</strong> Clear prompts, and recognising when an output misses the intent.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Decide whether to use AI based on the nature of the academic task, including reasoned non-use.</strong> Administration is the family where a mistake costs the student least.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Design AI use attentive to data sources, data selection and information flow.</strong> The institutional route answers the question of where the text goes.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-M4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Monitor and evaluate AI use throughout an academic process.</strong> Checkpoints. The tenth minute-summary gets checked less than the first, and nothing warns you.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Investigate how an AI system is intended to work, whom it is designed for, and what its limits are.</strong> The model catalogue behind an institutional front end changes without telling you.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Art. 4 literacy duty applies to your institution as deployer, whichever route you take.<br><strong>In this course:</strong> Block 2 — administration family.<br><strong>Read:</strong> [Handlungsempfehlungen für Hochschullehrende zum Einsatz von Künstlicher Intelligenz](https://www.twillo.de/edu-sharing/components/render/27d39f95-eada-4cec-939f-95eada0cec80) · [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #a86a12;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I run a model locally with Ollama, so I assume I am compliant</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#a86a12;margin:6px 0 4px;">Proceed — but with these first</p>
<p style="margin:0 0 12px;color:#16202b;">Local hosting moves you up on two competences and answers exactly one obligation.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Design AI use attentive to data sources, data selection and information flow.</strong> You can say precisely where the text goes, which most colleagues cannot.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Choose an appropriate AI approach by comparing how different systems operate.</strong> You have compared how different systems operate rather than accepting a default.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-E5</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Compare how AI systems consume energy and natural resources.</strong> Running it yourself is the first time most people see the energy cost as a cost.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> Route is not compliance. Annex III §3, Art. 50 and Art. 4 are unchanged by where the bytes went.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> Smaller models are measurably weaker on long documents and on languages other than English, so verification effort goes up, not down.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Removes the processor relationship and the transfer. Removes nothing else.<br><strong>In this course:</strong> Block 2 · Lab 7 (`route`) · Block 3 terminology table, deployment route.<br><strong>Read:</strong> llmlab — seven exercises that check this session's claims on your own machine · [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #8a3324;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I run submissions through an AI detector</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#8a3324;margin:6px 0 4px;">This is a decision, not a level</p>
<p style="margin:0 0 12px;color:#16202b;">The framework does not put you at a level here. It puts a decision in front of you.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Evaluate AI systems using defined outcomes, test cases and user feedback.</strong> You are evaluating a system — but against no defined outcome, no test cases and no measure of the harm of a false positive.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E6</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Explain how AI can amplify societal biases and concentrate epistemic authority.</strong> Detector errors are distributed by first language, which means the instrument is not the one it claims to be.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> There is no evidence an accused student can produce that settles the matter in their favour.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E7</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Analyse how well AI use aligns with ethical principles and human values.</strong> An instrument whose two error types carry consequences this unequal has to be justified against that asymmetry, not against an average.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> A disciplinary process resting on an unfalsifiable output is a procedure question before it is a technical one.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Annex III §3 covers monitoring prohibited behaviour during tests. GDPR Art. 22 covers the decision that follows.<br><strong>In this course:</strong> Block 2 — detectors, all three cards.<br><strong>Read:</strong> Heads we win, tails you lose: AI detectors in education · [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #a86a12;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I use live captioning or translation in the lecture theatre</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#a86a12;margin:6px 0 4px;">Proceed — but with these first</p>
<p style="margin:0 0 12px;color:#16202b;">The clearest accessibility gain in the catalogue, in the family where students cannot easily opt out.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Visualise, prototype and combine ideas using different types of AI systems.</strong> You are producing material with AI support in a live setting.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-E1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Recognise AI's role and influence in academic contexts.</strong> You can name where an AI system is operating in your teaching.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Investigate how an AI system is intended to work, whom it is designed for, and what its limits are.</strong> Its stated limits: it degrades on noise, accent and technical vocabulary — exactly where you need it.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Apply the legal framework for AI in higher education.</strong> Art. 50: announce it. And the hard stop next door — anything inferring emotion from faces, voices or posture is prohibited under Art. 5(1)(f).</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> Announce it as an aid, never as a record.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Art. 50 transparency. Art. 5(1)(f) prohibition sits immediately adjacent.<br><strong>In this course:</strong> Block 2 — in-class family and the legal panel.<br><strong>Read:</strong> [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) · [Didaktische Chatbot-Typen — Beispiele für Ihren Einsatz](https://www.zml.kit.edu/didaktische-chatbots.php)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #0f7a5a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I generate slides, quizzes or task variants</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#0f7a5a;margin:6px 0 4px;">A reasonable place to be</p>
<p style="margin:0 0 12px;color:#16202b;">The family with the largest gain and the smallest risk, because you review before anything ships.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Visualise, prototype and combine ideas using different types of AI systems.</strong> Examples, quizzes, graphics with AI support.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Use AI to explore perspectives that build upon original academic ideas.</strong> Using AI to open perspectives on material you already own.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> The volume trap: producing four versions is easy, deciding which to use is the work and it did not get easier.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E6</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Explain how AI can amplify societal biases and concentrate epistemic authority.</strong> Ask what a generated example set represents, and who is missing from it.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-C4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Analyse how AI can safeguard or violate authenticity, authorship and intellectual property.</strong> If it goes to students as OER, say what was AI-assisted.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> None directly, until the material is used to evaluate someone.<br><strong>In this course:</strong> Block 2 — preparation family · Block 3 — stages one and two: prompt and skill prompt.<br><strong>Read:</strong> [KI-Literacy — Grundlagen und Orientierung für Lehrende](https://www.twillo.de/edu-sharing/components/render/2e1ef4ad-15e0-4d17-af45-4c7223041966) · Self-learning nuggets: AI Orientation, AI Basics, AI Tools, Prompting, Quality and Ethics</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #0f7a5a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I have written a skill prompt and I reuse it (stage two)</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#0f7a5a;margin:6px 0 4px;">A reasonable place to be</p>
<p style="margin:0 0 12px;color:#16202b;">This is the move from Foundation to Applied, and it is the one that transfers to a colleague.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Direct and iterate with generative AI systems (prompting as a documented practice).</strong> Prompting as a documented practice rather than a private knack.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Decompose a task to determine where AI should automate and where it should only augment.</strong> You have decided which part is automated and which is only augmented.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-X3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Develop professionally and collaboratively with AI.</strong> The instruction is reviewable, so it can be taught.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate AI systems using defined outcomes, test cases and user feedback.</strong> Test cases: try it on the three inputs where you expect it to fail.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-M4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Monitor and evaluate AI use throughout an academic process.</strong> Checkpoints across a term, not a single approval at the start.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> None new. The instruction is what makes your human oversight demonstrable under Art. 14 if it ever matters.<br><strong>In this course:</strong> Block 3 — stage two · Lab 4 (`steer`).<br><strong>Read:</strong> llmlab — seven exercises that check this session's claims on your own machine · [KI als Reflexionsinstrument im wissenschaftlichen Arbeiten](https://zhq-blog.fh-aachen.de/kompetenzen-studierende/ki-als-reflexionsinstrument-im-wissenschaftlichen-arbeiten/)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #0f7a5a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I run a specification over a folder of inputs with provenance headers (stage three)</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#0f7a5a;margin:6px 0 4px;">A reasonable place to be</p>
<p style="margin:0 0 12px;color:#16202b;">Advanced on the prompting competence, and the first stage that leaves an auditable trail.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Advanced</span><br><strong>Direct and iterate with generative AI systems (prompting as a documented practice).</strong> A versioned specification, a recorded model, temperature and seed.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate AI systems using defined outcomes, test cases and user feedback.</strong> Defined outcomes and repeatable test cases.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Monitor and evaluate AI use throughout an academic process.</strong> Monitoring across the whole process rather than at the end.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-X2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Practise scholarly work with AI.</strong> Scholarly practice: the trail is what makes the claim checkable by someone else.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Improve AI use and AI systems to promote well-being and societal benefit.</strong> Publishing it so somebody other than you can use and correct it.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E5</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Compare how AI systems consume energy and natural resources.</strong> Batch runs are where the energy question stops being abstract.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> The provenance header is the practical form of Art. 14 oversight and of an appeal-proof position.<br><strong>In this course:</strong> Block 3 — stage three · Lab 6 (`ladder`) and the `harness` command.<br><strong>Read:</strong> llmlab — seven exercises that check this session's claims on your own machine · Workshop 4 — AI in Teaching: Tools, Strategies and Reflection</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #a86a12;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I have set a task that assumes students will use AI</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#a86a12;margin:6px 0 4px;">Proceed — but with these first</p>
<p style="margin:0 0 12px;color:#16202b;">You have crossed into the second reading of every competence: not what you can do, but what you enable students to do.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Decide whether to use AI based on the nature of the academic task, including reasoned non-use.</strong> You decided the task is one where AI use is legitimate.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Analyse how AI can safeguard or violate authenticity, authorship and intellectual property.</strong> Authorship and disclosure rules are now part of the task, not an afterthought.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> You cannot require a tool your institution does not provide. Equity of access is a condition of fairness, not a nice-to-have.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Recognise AI's role and influence in academic contexts.</strong> at the student reading — they have to be able to identify the AI in the tools they already use.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> at the student reading — they need a verification procedure, and they will not invent one.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate AI systems using defined outcomes, test cases and user feedback.</strong> Agentic tools change what an online test measures. Assume the format is under revision.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Equity of access; Art. 50 if a system speaks to students on your behalf; Annex III §3 when the output reaches a mark.<br><strong>In this course:</strong> Block 2 — the equity panel · Block 3.4.<br><strong>Read:</strong> [Warum KI-Agenten das Ende klassischer Onlinetests einleiten](https://hochschulforumdigitalisierung.de/ki-agenten-in-onlinetests/) · [Feldnotizen: Wenn KI-Agenten in der Klasse auftauchen](https://moodle.com/de/nachrichten/feldnotizen-wenn-ki-agenten-in-der-klasse-auftauchen/) · [DigiStudi — Digitale Kompetenzen für Studienanfänger*innen](https://imoox.at/course/DigiStudi)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #45566a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I do not use AI in my teaching at all</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#45566a;margin:6px 0 4px;">Still inside the framework</p>
<p style="margin:0 0 12px;color:#16202b;">Reasoned non-use is a named competence, not an absence of one — but three obligations still apply to you.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-M1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Decide whether to use AI based on the nature of the academic task, including reasoned non-use.</strong> Deciding *not* to use AI for a task, for a stated reason, is the competence. Deciding by default is not.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Recognise AI's role and influence in academic contexts.</strong> Your students are using it, and there is AI in your reference manager, your VLE and your literature search whether you chose it or not.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Describe how AI systems perform tasks in accurate, non-anthropomorphic language.</strong> You will be asked to sit on a committee that procures one of these, and non-anthropomorphic description is what makes that meeting useful.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Apply the legal framework for AI in higher education.</strong> Art. 4 falls on the institution and is discharged by staff who can explain the tools in use. Abstention does not discharge it.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Art. 4 applies to you as a member of the deploying organisation.<br><strong>In this course:</strong> Block 0 · Block 1 · Block 4, question one — which is the reflective version of this position.<br><strong>Read:</strong> [Intellektuelle Souveränität: Empfehlungen für die Hochschulbildung in Zeiten von generativer KI](https://www.wissenschaftsrat.de/download/2026/3319-26) · [AI deskilling is a structural problem](https://doi.org/10.1007/s00146-025-02686-z)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #a86a12;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I use AI to search literature and summarise papers</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#a86a12;margin:6px 0 4px;">Proceed — but with these first</p>
<p style="margin:0 0 12px;color:#16202b;">The most common academic use, and the one where the failure is hardest to see in the output.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-X2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Practise scholarly work with AI.</strong> Literature search and text revision, with references checked against the source.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Use AI to explore perspectives that build upon original academic ideas.</strong> Exploring perspectives on ideas that are already yours.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> A grounded answer and an ungrounded answer are written in the same register. Nothing in the text distinguishes them.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Examine how predictive AI recommendations can inform or limit perspectives.</strong> Ranking is pre-selection, and pre-selection is not neutral. What you did not see is not reported as missing.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E6</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Explain how AI can amplify societal biases and concentrate epistemic authority.</strong> A fluent synthesis of a live disagreement does not report the disagreement as absent. It simply does not report it.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> None directly. The exposure is scholarly rather than legal, which does not make it smaller.<br><strong>In this course:</strong> Block 1 — fabrication and illusion of consensus · Lab 5 (`ground`) · Block 3 — context window.<br><strong>Read:</strong> [Zahl falscher KI-Referenzen in Forschungsarbeiten nimmt zu](https://www.forschung-und-lehre.de/forschung/zahl-falscher-ki-referenzen-in-forschungsarbeiten-nimmt-zu-7760) · [Detecting citation hallucinations in the era of AI-generated content](https://arxiv.org/abs/2602.15871) · [Reference verification service](https://bibfox.com/en/solutions/reference-verification) · [Wissenschaftliches Schreiben und KI — wie ein fundamentales Missverständnis die Lehrentwicklung blockiert](https://schulesocialmedia.com/2026/06/16/wissenschaftliches-schreiben-und-ki-wie-ein-fundamentales-missverstandnis-die-lehrentwicklung-blockiert/)</p>
</div>
</details>

<details style="border:1px solid #d6dee8;border-left:4px solid #0f7a5a;border-radius:8px;margin:10px 0;padding:0;background:#ffffff;">
<summary style="cursor:pointer;padding:11px 14px;font-weight:600;color:#16202b;">I built a teaching artefact with substantial AI assistance and published it</summary>
<div style="padding:0 14px 14px 14px;font-size:0.94em;color:#45566a;">
<p style="font-weight:600;color:#0f7a5a;margin:6px 0 4px;">A reasonable place to be</p>
<p style="margin:0 0 12px;color:#16202b;">Advanced across several competences, and the point at which Stratum X stops being theoretical.</p>
<table style="width:100%;border:0;"><tr style="vertical-align:top;">
<td style="border:0;width:50%;padding:0 10px 0 0;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#0f7a5a;">You are exercising</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-C2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Advanced</span><br><strong>Visualise, prototype and combine ideas using different types of AI systems.</strong> Prototyping and combining system types into something that did not exist.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Advanced</span><br><strong>Design AI use attentive to data sources, data selection and information flow.</strong> Architecture as the privacy answer: no accounts, no server-side storage, nothing to protect because nothing is collected.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-S1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Investigate how an AI system is intended to work, whom it is designed for, and what its limits are.</strong> You can state the artefact's limits because you specified them.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #0f7a5a;"><code style="font-size:0.8em;color:#1a4a88;">HET-X2</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Practise scholarly work with AI.</strong> The commit history is the audit trail, and the audit trail is the credibility.</li></ul></td>
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Improve AI use and AI systems to promote well-being and societal benefit.</strong> Maintenance. A repository nobody has opened since the demo is not an OER.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> It becomes the Annex III situation the moment the score attaches to a grade.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E5</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Compare how AI systems consume energy and natural resources.</strong> If it calls a hosted model at runtime, that cost is now in your teaching, every cohort, every year.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Art. 50 for what the learner is told. Annex III §3 as soon as it is graded.<br><strong>In this course:</strong> Block 3.4 — the worked example and the three pedagogical decisions.<br><strong>Read:</strong> Workshop 4 — AI in Teaching: Tools, Strategies and Reflection · [Perspektiven einer KI-unterstützten offenen Bildungspraxis](https://his-he.de/publikation/perspektiven-einer-ki-unterstuetzten-offenen-bildungspraxis/)</p>
</div>
</details>


<div style="border-left:4px solid #7b8b9c;background:#f7f9fb;border-radius:0 8px 8px 0;padding:10px 15px;margin:13px 0;font-size:0.92em;color:#45566a;">
<strong>Facilitator:</strong> Ask for a show of hands on the first three before you open any of them. The distribution in the room is the argument for the block you are about to teach.
</div>

## A.3 · What this course covers, competence by competence

Including the ones it does not reach. A coverage map that claims everything is a
coverage map nobody can use.

| Competence | Level reached | Where | What is still missing |
| --- | --- | --- | --- |
| `HET-E1` **Recognise AI's role and influence in academic contexts** | Foundation | Block 0 diagram; Block 2 four-family map; ASSET module 01 | Institution-wide mapping (Advanced) is not attempted. |
| `HET-E2` **Describe how AI systems perform tasks in accurate, non-anthropomorphic language** | Applied | Block 3 terminology table (six terms); Labs 1–3; ASSET module 02 | This is the strongest coverage in the course. The table is the whole argument. |
| `HET-E3` **Evaluate whether AI outputs should be accepted, revised, or rejected** | Applied | Block 1 failure modes; Lab 5 `ground`; Block 3 grounding row | Covered as a judgement, not yet as a written verification procedure. |
| `HET-E4` **Examine how predictive AI recommendations can inform or limit perspectives** | Foundation | Block 1 — confirmation and anchoring; Block 3 — context window | Recommender pre-selection is named rather than examined. |
| `HET-E5` **Compare how AI systems consume energy and natural resources** | Foundation | Block 2 — the resource panel; Lab 7 route report | Weakest area in the course relative to its EU GREEN framing. Named honestly rather than padded. |
| `HET-E6` **Explain how AI can amplify societal biases and concentrate epistemic authority** | Applied | Block 1 homogenisation and illusion of consensus; Block 2 detectors, uneven errors | Bias is treated through one worked case (detectors) rather than systematically. |
| `HET-E7` **Analyse how well AI use aligns with ethical principles and human values** | Applied | Block 2 equity and copyright panels; Block 4 reflection questions | Ethics is carried by cases, not by a principles list. Deliberate. |
| `HET-C1` **Use AI to explore perspectives that build upon original academic ideas** | Foundation | Block 2 preparation family; Block 3 stages one and two | — |
| `HET-C2` **Visualise, prototype and combine ideas using different types of AI systems** | Foundation | Block 2 preparation family; Block 3.4 worked example (Advanced, demonstrated not practised) | Participants watch rather than build. Ninety minutes does not buy the build. |
| `HET-C3` **Direct and iterate with generative AI systems (prompting as a documented practice)** | Applied | Block 3 — the five stages; Labs 4 and 6; the harness command with `--loop` and `--wiki` | This is the spine of Block 3 and the clearest route to Applied. |
| `HET-C4` **Analyse how AI can safeguard or violate authenticity, authorship and intellectual property** | Foundation | Block 2 copyright panel; Block 3 provenance disclosure | Institutional disclosure rules vary; the session gives the question, not your answer. |
| `HET-M1` **Decide whether to use AI based on the nature of the academic task, including reasoned non-use** | Applied | Block 2 four families ordered by consequence; Block 4 question one | Reasoned non-use is explicitly a competence here, which is unusual and load-bearing. |
| `HET-M2` **Choose an appropriate AI approach by comparing how different systems operate** | Foundation | Block 2 tool cards; Lab 7 `route` | — |
| `HET-M3` **Decompose a task to determine where AI should automate and where it should only augment** | Applied | Block 3 stage two; Block 4 — what will you keep doing by hand | Directly reinforced by Ferdman's capacity-hostile environments. |
| `HET-M4` **Monitor and evaluate AI use throughout an academic process** | Foundation | Block 1 automation complacency; Block 3 provenance headers | Checkpoints across a term are described, not practised. |
| `HET-S1` **Investigate how an AI system is intended to work, whom it is designed for, and what its limits are** | Foundation | Block 2 tool cards, each with its stated fault | — |
| `HET-S2` **Evaluate AI systems using defined outcomes, test cases and user feedback** | Applied | The whole lab: seven claims put to a system on your own machine | The lab *is* this competence. It is why the session has a terminal in it. |
| `HET-S3` **Design AI use attentive to data sources, data selection and information flow** | Applied | Block 2 deployment routes; Block 3 route row | — |
| `HET-S4` **Improve AI use and AI systems to promote well-being and societal benefit** | not reached | Named in Block 5 (publish one artefact) and not reached | Requires other people and a review cycle. Ninety days, not ninety minutes. |
| `HET-X1` **Apply the legal framework for AI in higher education** | Applied | Block 2 legal panel; GDPR Art. 22 panel; copyright panel; closing quiz | The most heavily covered Stratum X competence, because it is the one with a deadline. |
| `HET-X2` **Practise scholarly work with AI** | Foundation | Block 3.4 provenance and licensing; Block 1 fabrication | Scholarly writing with AI, and doctoral supervision, each need a session of their own. |
| `HET-X3` **Develop professionally and collaboratively with AI** | Applied | Block 4 question three; Block 5 mentor one colleague; the 90-day plan | Started, not completed — which is exactly the Deepen claim the session makes. |

### The four it does not reach, said plainly

- **`HET-S4` — improving systems and use for well-being and societal benefit.**
  Needs a channel, a community and a review cycle. Ninety days, not ninety
  minutes.
- **`HET-E5` — energy and resource comparison.** Foundation only, which is thin
  for a course funded under a green alliance. Named rather than solved.
- **`HET-C2` at Advanced — prototyping.** Demonstrated in 3.3 and not practised.
  You watch someone else's artefact.
- **`HET-X2` — scholarly work with AI** beyond provenance and licensing.
  Doctoral supervision and publication ethics are a different session.

## A.4 · The self-study route, for people who could not attend

Five open LiaScript modules written for teachers in vocational education cover
the Foundation level of most of the Engage domain and part of Create, in about
four hours:

- **AI Orientation** — lifelong professional learning (`E1`, `X3`)
- **AI Basics** — non-anthropomorphic description and human agency (`E2`, `E3`, `M4`)
- **AI Tools** — system types, data origin, OER (`M2`, `S1`, `S3`)
- **Prompting** — `C3` at Foundation, and the structure a standing instruction needs
- **Quality and Ethics** — `E6`, `E7`, and the human-rights framing

They were written for a TVET audience under the UNESCO-UNEVOC ASSET
co-initiative, and the examples are electronics rather than seminar rooms. That
is a feature when you send them to a colleague who teaches a workshop-based
subject, and a limitation when you send them to a lawyer. Point people at the
modules, then run Block 2 and Block 3 with them, because those are the two the
modules do not reach.

## A.5 · Check yourself — the placement map

You run every model locally. Which claim does the framework support?

    [( )] You have satisfied the legal floor, since no data leaves the institution.
    [(X)] You are Applied on the data-flow competence and unchanged on the legal one.
    [( )] You have reached Advanced on all four Shape competences.
    [( )] Local hosting is outside the framework, since it is an infrastructure choice.
    *******************************************************************
    Route answers the transfer question and nothing else. Annex III §3,
    Art. 50 and Art. 4 are indifferent to where the bytes went — which is why
    the router puts the legal competence in the amber column for that
    practice rather than the green one.
    *******************************************************************

A colleague uses no AI at all and says the framework does not apply to them.
What does the map say?

    [( )] Correct: the competences describe use, so non-use places you outside them.
    [( )] Correct for the four domains, but Stratum X still applies.
    [(X)] Reasoned non-use is itself a competence, and three obligations apply regardless.
    [( )] They should be assessed at Foundation on every competence by default.
    *******************************************************************
    Deciding not to use AI for a task, for a stated reason, is the
    Manage-domain competence in its own right. Deciding by default is not.
    Meanwhile their students are using it, their reference manager contains
    it, and the Art. 4 literacy duty falls on the institution and is
    discharged by staff who can explain the tools in use.
    *******************************************************************

Which competence does writing a standing instruction and reusing it move you to
Applied on?

    [[HET-C3]]
    *******************************************************************
    `HET-C3` — directing and iterating with generative systems, with
    prompting treated as a documented practice rather than a private knack.
    It is the competence Block 3 is built around.
    *******************************************************************

--------------------------------------------------------------------------------

# Appendix B — References

--{{0}}--
Everything cited in this course, grouped by what you would need it for.

Sources added in version 4 come largely from the reading list circulated in the
OvGU working group on AI and digitality in study and teaching, which is the
best-curated German-language source on this topic that we know of.

Nobody reads forty items. This list is here so that a claim can be traced, and so
that when a colleague disputes something you can hand them the source rather than
your recollection of it. **If you want three things and nothing else:** Ferdman
on deskilling as a structural problem, the Wissenschaftsrat recommendations for
the German frame, and Chandra and colleagues on why warning somebody about
sycophancy does not protect them from it.

## Competence frameworks

1. Miao, F. & Cukurova, M. (2024). *AI competency framework for teachers.* UNESCO, Paris. CC BY-SA 3.0 IGO. <https://unesdoc.unesco.org/ark:/48223/pf0000391104>
1. UNESCO (2024). *AI competency framework for students.* UNESCO, Paris. <https://unesdoc.unesco.org/ark:/48223/pf0000391105>
1. OECD & European Commission (2026). *Empowering Learners for the Age of AI: an AI literacy framework (AILit).* Addressee: primary and secondary learners. <https://ailiteracyframework.org>
1. Redecker, C. (2017). *European Framework for the Digital Competence of Educators: DigCompEdu.* JRC Science for Policy Report, Publications Office of the EU. <https://joint-research-centre.ec.europa.eu/digcompedu_en>
1. Vuorikari, R., Kluzer, S. & Punie, Y. (2022). *DigComp 2.2: The Digital Competence Framework for Citizens.* JRC128415. Adds examples concerning AI systems. <https://publications.jrc.ec.europa.eu/repository/handle/JRC128415>
1. UNESCO (2018). *UNESCO ICT Competency Framework for Teachers, version 3.* Origin of the three-level acquisition / deepening / creation grammar. <https://unesdoc.unesco.org/ark:/48223/pf0000265721>
1. Npuls (2025). *AI GO! AI Literacy in Education — a practical framework.* Addressed to education professionals in mbo, hbo and wo; the closest published comparator to a higher-education-facing framework. <https://npuls.nl/en/knowledge-base/ai-go-ai-literacy-in-education-a-practical-framework>
1. Npuls (2025). *Reference Framework 2.0 — Responsible use of education data and AI.* Governance-facing companion to AI GO!; written for institutions rather than individuals. <https://npuls.nl/en/knowledge-base/reference-framework-2-0-responsible-use-of-education-data-and-ai>
1. Long, D. & Magerko, B. (2020). *What is AI literacy? Competencies and design considerations.* CHI '20. The source of the competence list most later frameworks reuse. <https://doi.org/10.1145/3313831.3376727>
1. OvGU Zentrum für Lehrer*innenbildung, working group (2026). *HETAICF v0.11 — Higher Education Teaching AI Competence Framework.* **Unpublished draft, in review. Numbering will change. Do not cite competence identifiers as authority.** Used in this session as a mechanism for local adaptation, not as a source.
1. AK Digitalisierung im Lehramt, OvGU (2026). *DACT v1.0 — Digital and AI Competency Framework for University Teacher Trainers.* Local framework for the teacher-trainer role; one of the source frameworks crosswalked in HETAICF.

## Policy, recommendations and institutional practice

1. Wissenschaftsrat (2026). *Intellektuelle Souveränität: Empfehlungen für die Hochschulbildung in Zeiten von generativer KI.* Drs. 3319-26, Köln, July 2026. doi:10.57674/1evx-t906. Argues that the question is not how higher education is designed *with* generative AI, but how good higher education is designed in a world shaped by it. <https://www.wissenschaftsrat.de/download/2026/3319-26>
1. OECD (2026). *Policies supporting responsible and systematic GenAI adoption in higher education.* OECD Education Policy Perspectives. <https://www.oecd.org/en/publications/policies-supporting-responsible-and-systematic-genai-adoption-in-higher-education_c4e5621f-en.html>
1. Hochschulforum Digitalisierung (2026). *Generative KI in der Hochschullehre — wie wir Innovation verantwortungsvoll gestalten.* <https://hochschulforumdigitalisierung.de/genki-in-der-hochschullehre/>
1. UC Berkeley School of Law (2026). *Artificial Intelligence Policy, effective Summer 2026.* A readable example of a unit-level policy, at the granularity a department can actually write. <https://www.law.berkeley.edu/wp-content/uploads/2026/05/AI-Final-Policy-26.pdf>
1. heise online (2026). *Leiden Declaration: Mathematiker fordern bewussten Umgang mit KI — „Don't believe the hype“.* A discipline writing its own rules rather than waiting for an institutional one. <https://www.heise.de/news/Mathematiker-fordern-bewussten-Umgang-mit-KI-Don-t-believe-the-hype-11378210.html>
1. KI:Expertisezentrum.nrw (2026). *Regional AI competence centre for higher education in North Rhine-Westphalia.* An example of the regional support structure the Wissenschaftsrat recommendations call for. <https://ki-expertisezentrum.nrw/>
1. Universität zu Köln (2026). *Universität zu Köln ist Teil des neuen KI:Expertisezentrum.nrw.* <https://uni-koeln.de/universitaet/aktuell/meldungen/meldungen-detail/universitaet-zu-koeln-ist-teil-des-neuen-kiexpertisezentrumnrw>
1. HIS-HE (2026). *Perspektiven einer KI-unterstützten offenen Bildungspraxis.* <https://his-he.de/publikation/perspektiven-einer-ki-unterstuetzten-offenen-bildungspraxis/>

## Law

1. European Union (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act).* Arts. 4, 5(1)(f), 14, 50; Annex III §3. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
1. European Union (2026). *Regulation (EU) 2026/1744 (Digital Omnibus on AI).* OJ 24 July 2026, in force 27 July 2026. Defers standalone Annex III high-risk obligations to 2 December 2027. Arts. 4, 5 and 50 not deferred. <https://eur-lex.europa.eu>
1. European Union (2016). *Regulation (EU) 2016/679 (GDPR).* Arts. 5 and 22. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
1. edu-sharing / Open Innovation Community (2026). *KI in der Bildung — Rechtliche Orientierung für Bildungseinrichtungen und Lehrkräfte (FAQ).* German-language legal FAQ; useful for the questions a colleague asks in the corridor. <https://edu-sharing.atlassian.net/wiki/spaces/OIC/pages/1891565573/>

## How the systems fail — the evidence base

1. Ferdman, A. (2026). *AI deskilling is a structural problem.* *AI & Society* 41, 3001–3013. doi:10.1007/s00146-025-02686-z. Introduces *capacity-hostile environments*: settings in which AI mediation blocks the cultivation of a capacity, so that deskilling is a property of the environment rather than a failure of individual willpower. <https://doi.org/10.1007/s00146-025-02686-z>
1. Chandra, K., Kleiman-Weiner, M., Ragan-Kelley, J. & Tenenbaum, J. B. (2026). *Sycophantic chatbots cause delusional spiraling, even in ideal Bayesians.* arXiv:2602.19141. A Bayesian model in which even a perfectly rational user spirals; the effect survives both removing hallucination and warning the user that the system is sycophantic. <https://arxiv.org/abs/2602.19141>
1. Bassett et al. (2026). *Heads we win, tails you lose: AI detectors in education.* The unfalsifiability and asymmetric-harm argument used in Block 2.
1. Forschung & Lehre (2026). *Zahl falscher KI-Referenzen in Forschungsarbeiten nimmt zu.* <https://www.forschung-und-lehre.de/forschung/zahl-falscher-ki-referenzen-in-forschungsarbeiten-nimmt-zu-7760>
1. CheckIfExist (2026). *Detecting citation hallucinations in the era of AI-generated content.* arXiv:2602.15871. <https://arxiv.org/abs/2602.15871>
1. BibFox (2026). *Reference verification service.* A verification tool, and therefore itself a tool with a false-positive rate you are responsible for knowing. <https://bibfox.com/en/solutions/reference-verification>
1. Tagide (2026). *The anatomy of a learning stall.* On what happens to a learner who never reaches the point of productive difficulty. <https://tagide.com/blog/llm/the-anatomy-of-a-learning-stall/>
1. Golem.de (2026). *KI-Agenten übernehmen marxistische Ansichten.* Reported value drift in agent populations. Read as: the outputs carry a politics you did not choose and did not audit. <https://www.golem.de/news/kuenstliche-intelligenz-ki-agenten-uebernehmen-marxistische-ansichten-2605-208696.html>
1. Springer / IJETHE (2026). *Generative AI literacy across education and business: competencies, obstacles, and benefits — a systematic literature review.* <https://link.springer.com/article/10.1186/s41239-026-00596-8>

## Teaching practice, didactics and commentary

1. Krommer, A. (2026). *KI-Feedback. Oder: die Entscheidung zwischen Skylla und Charybdis.* The feedback dilemma: automated feedback that is either too generic to help or too specific to be defensible. <https://axelkrommer.com/2026/07/25/ki-feedback-oder-die-entscheidung-zwischen-skylla-und-charybdis/>
1. ZML, Karlsruher Institut für Technologie (2026). *Didaktische Chatbot-Typen — Beispiele für Ihren Einsatz.* A typology rather than a tool list; the useful shape for a departmental conversation. <https://www.zml.kit.edu/didaktische-chatbots.php>
1. ZHQ, FH Aachen (2026). *KI als Reflexionsinstrument im wissenschaftlichen Arbeiten.* <https://zhq-blog.fh-aachen.de/kompetenzen-studierende/ki-als-reflexionsinstrument-im-wissenschaftlichen-arbeiten/>
1. Hochschulforum Digitalisierung (2026). *Warum KI-Agenten das Ende klassischer Onlinetests einleiten.* <https://hochschulforumdigitalisierung.de/ki-agenten-in-onlinetests/>
1. Moodle (2026). *Feldnotizen: Wenn KI-Agenten in der Klasse auftauchen.* Practitioner field notes rather than a position paper. <https://moodle.com/de/nachrichten/feldnotizen-wenn-ki-agenten-in-der-klasse-auftauchen/>
1. Wampfler, P. (2026). *Wissenschaftliches Schreiben und KI — wie ein fundamentales Missverständnis die Lehrentwicklung blockiert.* <https://schulesocialmedia.com/2026/06/16/wissenschaftliches-schreiben-und-ki-wie-ein-fundamentales-missverstandnis-die-lehrentwicklung-blockiert/>
1. Lehrwende (2026). *Lehrwende — Hochschulbildung im Zeitalter generativer KI.* Worth reading on the meta level: its companion material (slides, podcasts) is itself AI-generated, and the Fokusgruppe note that circulated it observes that this displays exactly the problems such material has, and that concrete recommendations for action are scarce. <https://lehrwende.de/>
1. twillo (2026). *Handlungsempfehlungen für Hochschullehrende zum Einsatz von Künstlicher Intelligenz.* OER, German. <https://www.twillo.de/edu-sharing/components/render/27d39f95-eada-4cec-939f-95eada0cec80>
1. twillo (2026). *KI-Literacy — Grundlagen und Orientierung für Lehrende.* OER, German. <https://www.twillo.de/edu-sharing/components/render/2e1ef4ad-15e0-4d17-af45-4c7223041966>
1. Springer (2026). *GenAI in novel educational applications: practices of integrating GenAI in the K-12 classroom.* <https://link.springer.com/book/10.1007/978-3-032-16153-6>
1. In Preparation (Substack) (2026). *Opinion: I was not allowed to type prompts into ChatGPT during my chalk talk.* An opinion piece; included because the argument it makes about tool access in assessment is one you will meet. <https://inpreparation.substack.com/p/opinion-i-was-not-allowed-to-type>

## Open offers you can point students and colleagues at

1. iMooX (2026). *DigiStudi — Digitale Kompetenzen für Studienanfänger*innen.* Open course; useful as the thing you point first-year students at instead of writing your own. <https://imoox.at/course/DigiStudi>
1. Deutscher Bildungsserver (2026). *complett — Portal für Bildungsressourcen.* <https://complett.bildungsserver.de/>
1. University of Helsinki & MinnaLearn (2018–). *Elements of AI.* Free introductory course, many languages; the standard first recommendation for a colleague with no starting point. <https://www.elementsofai.com>
1. KI-Campus (2026). *KI-Campus — die Lernplattform für Künstliche Intelligenz.* German-language course platform, including modules for educators. <https://ki-campus.org/>

## Tools named in Block 2

1. SURF & Npuls (2026). *EduGenAI — a generative AI platform for Dutch education.* National pilot for mbo, hbo and wo institutions; open-source and commercial models; not for assessment or fraud detection. <https://www.surf.nl/en/themes/artificial-intelligence/projects-and-collaborations/ai-hub>
1. Utrecht University (2026). *EduGenAI — AI policy for teachers.* One institution's own page on the pilot and its limits. <https://www.uu.nl/en/organisation/ai-policy/teachers/edugenai>
1. GWDG (2026). *Chat AI.* Academic cloud service for German research and higher education institutions. <https://chat-ai.academiccloud.de/>
1. HAWK Hildesheim/Holzminden/Göttingen (2026). *HAWKI.* Open-source front end an institution hosts itself. <https://github.com/HAWK-Digital-Environments/HAWKI>
1. Open WebUI (2026). *Open WebUI.* Open-source, self-hosted front end for local or licensed models, used by institutions internationally. <https://openwebui.com/>
1. Google (2025). *NotebookLM and the Gemini app are now Core Services with enterprise-grade data protection for all education customers.* Google Workspace Updates, April 2025. <https://workspaceupdates.googleblog.com/2025/04/notebookLM-and-gemini-app-core-services-for-education-customers.html>
1. Google for Education (2026). *Gemini Notebook.* The education page for NotebookLM under its newer name: no human review and no model training for education accounts, and a separate version for users under 18. <https://edu.google.com/ai-gemini-notebook/>
1. OpenAI (2024). *Introducing ChatGPT Edu.* <https://openai.com/index/introducing-chatgpt-edu/>
1. Anthropic (2025). *Introducing Claude for Education.* <https://www.anthropic.com/news/introducing-claude-for-education>
1. ETH Zurich, EPFL & CSCS (2025). *Apertus: a fully open, transparent, multilingual language model.* Press release, 2 September 2025; Apache 2.0. <https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html>
1. EuroLLM consortium (2024–). *EuroLLM — open multilingual models for Europe.* All 24 official EU languages; supported by Horizon Europe and EuroHPC. <https://eurollm.io/>
1. Mistral AI (2026). *Le Chat and the Mistral models.* French provider. <https://mistral.ai/>
1. Ollama (2026); LM Studio (2026). Local model runners. <https://ollama.com/> · <https://lmstudio.ai/>
1. Jisc (2026). *National Centre for AI in tertiary education.* United Kingdom. <https://nationalcentreforai.jiscinvolve.org/>

## The prompting evolution — Block 3

1. Anthropic (2025). *Agent Skills.* The `SKILL.md` format for saved, reusable instructions, published as an open standard in December 2025 and adopted by other vendors. Stage two. <https://agentskills.io/home>
1. Anthropic (2024). *Building effective agents.* Agents as models inside a harness of tools and loops. Stages three and four. <https://www.anthropic.com/engineering/building-effective-agents>
1. Anthropic (2025). *Effective context engineering for AI agents.* On what an agent is given to read, and why that is the thing to design. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
1. Karpathy, A. (2026). *llm-wiki.* GitHub gist, 4 April 2026. An idea file for a markdown knowledge base that an LLM agent builds and maintains from raw sources. Stage five. <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## This session

1. EduGreenLabs / OvGU Magdeburg (2026). *Workshop 4 — AI in Teaching: Tools, Strategies and Reflection.* This session. Page, LiaScript course and `llmlab`. CC BY 4.0.
1. EduGreenLabs / OvGU Magdeburg (2026). *llmlab — seven exercises that check this session's claims on your own machine.* Python 3.9+, standard library only, loopback enforced in code. CC BY 4.0.
1. UNESCO-UNEVOC / ASSET Co-initiative, OvGU (2026). *Self-learning nuggets: AI Orientation, AI Basics, AI Tools, Prompting, Quality and Ethics.* Five LiaScript modules written for TVET teachers, mapped in Appendix A as the self-study route into the Foundation level.


--------------------------------------------------------------------------------

# Licence and provenance

**AI in Teaching: Tools, Strategies and Reflection**, version 4, September 2026.
EduGreenLabs / OvGU Magdeburg — WP2 Training Lab, EU GREEN Alliance.

Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Funded by the
European Union. Views expressed are those of the authors alone.

The UNESCO AI Competency Framework for Teachers is CC BY-SA; this course
paraphrases and attributes it rather than reproducing its wording at length,
because this course is CC BY.

The framework used for the structure of Appendix A is an unpublished draft under
review and **should not be cited**.

**Companion files:** `masterclass_ai_in_teaching_v5.html` (the live session
instrument) · `RUN_OF_SHOW.md` (facilitator timing) · `llmlab/` (the seven lab
exercises) · `REFERENCES.md` (this bibliography, standalone).
