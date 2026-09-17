<!--
author:   Hannes Tegelbeckers · EduGreenLabs / OvGU Magdeburg
email:    hannes.tegelbeckers@ovgu.de
version:  7.0.0
language: en
narrator: UK English Male
comment:  Workshop 4 of the EU GREEN WP2 Training Lab. Self-study course on AI
          in higher education teaching — tools, strategies and reflection —
          with lab exercises, reference results and quizzes.
license:  CC BY 4.0

-->

# AI in Teaching: Tools, Strategies and Reflection

--{{0}}--
This is the self-study version of the EU GREEN Training Lab session on AI in
teaching. It contains the full content of the session, the lab exercises with
reference results, and a quiz at the end of every block.

<div style="background:linear-gradient(118deg,#e7eefa 0%,#eef2f8 55%,#f1ebf9 100%);border-bottom:2px solid #1a4a88;padding:22px 20px;border-radius:10px;">
<div style="color:#45566a;font-size:0.82em;">EU GREEN · Transformative Teaching and Learning · WP2 Training Lab · Workshop 4 · <strong>version 7</strong></div>
<h2 style="margin:8px 0 4px;color:#1a4a88;">Tools, Strategies and <span style="color:#6b4a9e;">Reflection</span></h2>
<div style="color:#45566a;">For teaching staff in higher education. All disciplines, no programming required.</div>
</div>

The course consists of three parts that build on one another.

| | | | | |
| --- | :---: | --- | :---: | --- |
| **Tools** | → | **Strategies** | → | **Reflection** |
| availability and conditions of use | | directing and checking output | | tasks that remain with the teacher |

- Tools without strategies: selection without rules of use.
- Strategies without reflection: procedures without a stated purpose.
- Reflection without tools: no change in teaching practice.

The 90-minute session covers the first two parts and introduces the third.
Changes to a module require further work; Block 5 outlines a 90-day plan for it.

## Use of this course

--{{0}}--
The course can be used for self-study, alongside the live session, and for
re-publication.

**Self-study.** About two and a half hours, including the lab exercises and the
quizzes. Work through the blocks in order. Every block ends with a quiz; answer
it before moving on. Each lab exercise has a *reference run* that you can open
if you cannot run the lab yourself — try to predict the result first.

**Alongside the live session.** The live version is
`masterclass_ai_in_teaching_v7_labs.html`. It shows key points only, with the
full text behind *Read more*, and contains the interactive lab results. This
course contains the same content in more detail, plus the quizzes.

**Re-publication.** All material is licensed CC BY 4.0.

### How the course is structured

| Block | Topic | UNESCO AI CFT Aspect 5 level |
| --- | --- | --- |
| 0 | Structure, outcomes, lab setup, readiness self-check | Acquire |
| 1 | Competence frameworks; limits of trust in model output | Acquire |
| 2 | Tools, legal framework, detectors, equity, copyright | Acquire → Deepen |
| 3 | Six technical terms; the five stages of prompting | Deepen |
| 4 | Reflection and the route to Create | Deepen → Create |
| 5 | 90-day plan, commitment, summary | Create (preparation) |

### Requirements for the lab

The lab is a Python package, `llmlab` (folder `V7/llmlab`). Python 3.9 or later,
no third-party packages, Windows, macOS or Linux. Requests are processed on the
same computer.

```bash
python -m llmlab check          # reachable services and selected model
python run.py                   # browser interface
```

For model output, install **Ollama** (ollama.com) and download one small model
in advance (about 3 GB):

```bash
ollama pull gemma3:4b
```

Without a model service, llmlab runs in simulated mode. The procedure and the
figures derived from it are real; the wording is produced by llmlab, and every
result is marked as simulated.

Every exercise states its aim, the background and the procedure, lists the
texts sent to the model and shows each system prompt and user message as sent,
with the settings and the output. The interpretation is composed from the
measured values.

**Reference runs.** The reference results quoted in this course were produced
with `gemma3:12b` via Ollama on a local computer on 15 September 2026 (llmlab
2.0.0, not simulated). Other models and versions give different figures; the
direction of the effects is what matters.

## 0 · Structure and outcomes

--{{0}}--
Target group, outcomes and structure of the course.

> **UNESCO AI CFT, Aspect 5.1 — Acquire.** Awareness of teachers' rights and
> obligations in the AI era. Each block of this course is assigned to a level
> of Aspect 5.

### Target group

The course does not train software development. It addresses decisions that
teaching staff make about tools, assessments and module handbooks and that now
have technical preconditions:

- where text is processed,
- how outputs are produced,
- which obligations follow.

The competence addressed is the ability to take such decisions and to justify
them.

### Outcomes

1. A self-assessed readiness profile — [self-check page](pages/p1_self_check.html).
2. A decision record for one tool — [tool triage page](pages/p2_tool_triage.html).
3. Results of seven lab exercises on a local model (`python -m llmlab all`).
4. A dated 90-day plan with two development areas — [plan page](pages/p3_cpd_plan.html).

### The lab

Several statements in this course concern the behaviour of language models:
tokenisation, the context window, sampling, the effect of system prompts,
grounding and multi-step processing. llmlab examines each of them with a defined
procedure, on a model running on your own computer. No account, key or network
connection is required.

| Lab | Statement examined | Block |
| --- | --- | --- |
| 1 `tokens` | Text is divided into tokens; languages differ in token count | 3 |
| 2 `context` | Text beyond the context window is removed without notice | 3 |
| 3 `vary` | Temperature and seed determine whether outputs are reproducible | 3 |
| 4 `steer` | Rules have an effect; their position matters less | 3 |
| 5 `ground` | Sourced and unsourced answers read the same | 1 |
| 6 `ladder` | The five stages of prompting on one task | 3 |
| 7 `route` | The route settles data protection, not the AI Act | 2 |

### Readiness self-check

Eight statements, about three minutes. For each statement, select the level
that describes current practice: **Not yet**, **Acquire**, **Deepen** or
**Create**. The page returns a profile and names the two largest gaps; the
90-day plan in Block 5 is based on them. No data is transmitted or stored; the
result can be exported. In Aspect 5, self-assessment of readiness is the
activity named for the Acquire level.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p1_self_check.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the self-check in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p1_self_check.html).

### Quiz — Block 0

What does the course address?

    [( )] Programming AI applications for teaching.
    [(X)] Decisions about tools, assessments and module handbooks that now have technical preconditions.
    [( )] Choosing the best commercial AI assistant for a department.
    [( )] Detecting AI use in student work.
    *******************************************************************
    The course addresses decisions that teaching staff already take, whose
    preconditions have changed: where text is processed, how outputs are
    produced and which obligations follow.
    *******************************************************************

What happens when llmlab cannot reach a model service?

    [( )] The exercises stop with an error.
    [( )] The exercises silently use an online model instead.
    [(X)] The exercises run in simulated mode, and every result is marked as simulated.
    *******************************************************************
    The procedure and the figures derived from it remain real; only the
    wording is produced by llmlab. The marking prevents simulated text from
    being taken for model output.
    *******************************************************************

--------------------------------------------------------------------------------

# 1 · Competences — frameworks and their target groups

--{{0}}--
A competence framework describes competences at defined levels. Used for
self-assessment, it identifies competences that are not yet developed.

> **Aspect 5.1 — Acquire.** Self-assessment of readiness for teaching in the AI era.

A competence framework describes competences at defined levels. Used for
self-assessment, it identifies **specific competences that are not yet
developed** and thus gives a professional development plan a defined subject.

## 1.1 · Frameworks and their target groups

| Framework | Target group | Content |
| --- | --- | --- |
| **UNESCO AI CFT** (2024) | school teachers | 5 aspects × 3 levels; Aspect 5 structures this course |
| **AILit** (2026, OECD/EC) | primary and secondary **learners** | AI literacy that incoming students can be expected to have |
| **DigCompEdu** (2017) | educators, EU | 22 competences, A1 to C2; predates generative systems |
| **DigComp 2.2** (2022) | citizens | adds examples concerning AI systems |
| **ICT-CFT** (2018, UNESCO) | teachers | origin of the three-level structure |
| **AI GO!** (2025, Npuls) | education professionals including **higher education** | the published framework closest to the higher-education teaching role |
| **Reference Framework 2.0** (2025, Npuls) | **institutions** | conditions for responsible use of education data and AI |

**UNESCO AI CFT.** Miao & Cukurova, *AI competency framework for teachers*.
Five aspects, each described at three levels. Aspect 5, *AI for professional
development*, structures this course. The framework was written for school
teachers; UNESCO names adaptation to the local context as the intended route of
implementation. It is licensed CC BY-SA; this course paraphrases and attributes
it rather than reproducing its wording, because the course is licensed CC BY.

**AILit.** *Empowering Learners for the Age of AI*, based on DigComp, UNESCO,
AI4K12 and Digital Promise. For higher education it describes the AI literacy
that incoming students can be expected to have been taught.

**DigCompEdu.** The European reference framework for the digital competence of
educators, to which many institutions map their programmes. It predates
generative systems; its categories remain applicable, but its examples do not
address the questions discussed in Block 2.

**DigComp 2.2 and ICT-CFT.** DigComp 2.2 added examples concerning AI systems to
the citizen framework. UNESCO's ICT-CFT introduced the three-level structure —
acquisition, deepening, creation — that later frameworks adopted. Neither
addresses teaching in higher education specifically.

**AI GO!** *AI Literacy in Education — a practical framework.* Based on an
umbrella review and refined in practitioner workshops. Its target group
comprises education professionals in vocational colleges, universities of
applied sciences and research universities. It does not cover national legal
requirements or examination regulations.

**Reference Framework 2.0.** A governance framework addressed to institutions
rather than individuals. It describes the conditions an institution has to
establish before AI is used in teaching, and is therefore relevant to committees
and management rather than to individual course design.

{{1}}
**The level structure is shared; the target groups differ.** Rows compare
levels within one framework; columns compare frameworks written for different
professions.

{{1}}
| | first level | second level | third level |
| --- | --- | --- | --- |
| ICT-CFT 2018 | acquisition | deepening | creation |
| UNESCO AI CFT 2024 | **Acquire** | **Deepen** | **Create** |
| AILit 2026 | three-level progression, learner-facing | | |
| DigCompEdu 2017 | A1 · A2 | B1 · B2 | C1 · C2 |

### The gap

The frameworks address learners, school teachers, citizens or educators in
general. The higher-education teaching role — with research obligations,
examination regulations, academic freedom and doctoral supervision — is covered
by these frameworks only in part.

AI GO! narrows the gap because it addresses education professionals in higher
education. What remains are national elements:

- examination regulations,
- the legal framework,
- the supervision relationship.

These elements are limited in number, which supports **adapting an existing
framework** rather than developing a new one: take a published framework as the
basis, identify where its target group differs from the local role, and document
only these differences.

### National recommendations (Germany)

The Wissenschaftsrat published recommendations in July 2026 (Drs. 3319-26) under
the guiding concept of **intellectual sovereignty**: the capacity to judge
independently, critically and with reasons in an environment shaped by
algorithms. It is a set of recommendations rather than a competence framework,
and the main national reference in Germany. Its central argument is that the
relevant question is not how higher education is designed *with* generative AI,
but how good higher education is designed in a world shaped by it. A short
version is available.

## 1.2 · Three layers of competence

--{{0}}--
AI-specific competence builds on digital competence and pedagogical judgement.

| Layer | Content |
| --- | --- |
| **AI-specific competence** | system behaviour, limits, accountability |
| **Digital competence** | files, platforms, accessibility, data protection |
| **Pedagogical judgement** | purpose of the assessment, intended learning outcomes |

The layers are interdependent: the top layer raises questions of the two layers
below. Most questions raised by AI in teaching are established questions —
whether an assessment measures what it is intended to measure, who holds the
data, whether a decision can be justified to the person affected — under
changed conditions. The course is therefore organised by teaching questions
rather than by technology.

## 1.3 · Limits of trust in model output

--{{0}}--
Fabricated content can be detected by comparison with sources. The other
failure modes affect the judgement of the person using the system.

Several failure modes are relevant to teaching. Fabricated content can be
detected by comparison with sources. The other failure modes affect the
judgement of the person using the system and are **not detected by checking
individual outputs**.

| Failure mode | In one sentence | Detectable by checking one output? |
| --- | --- | --- |
| Fabrication | plausible but false content | yes, against sources |
| Homogenisation | many texts share structure and examples | no — only across a set |
| Illusion of consensus | the controversy is omitted | no |
| Automation complacency | checking weakens over time | no |
| Confirmation and anchoring | the framing shapes the answer | no |
| Sycophancy | the model agrees with the user | no |
| Learning stall | the effortful part is skipped | no — visible later |
| Embedded positions | outputs carry unchosen positions | only with domain judgement |
| Deskilling | the judgement needed for checking declines | no |

### Fabrication

A language model generates text that is probable given the input; probability
is not the same as correctness. Invented references are the best-known case
and can be detected by checking each reference against a catalogue or database.

Fabricated references in research papers are reported as a measurable trend,
and reference verification services and research tools for detecting citation
hallucinations have appeared. These tools have their own error rates, their own
data routes and, under Art. 4 AI Act, their own requirement to be understood by
those who use them. They should be documented in the decision record together
with the tool whose output they check.

### Homogenisation

Texts produced with the same system tend to share structure, register and
choice of examples. Each text may be acceptable on its own, while a set of
thirty submissions — or a set of module descriptions — shows little variation.

### Illusion of consensus

A summary of a disputed research question can read as a coherent position. The
disagreement is not stated as absent; it is omitted.

### Automation complacency

After a series of correct outputs, users check subsequent outputs less
carefully. The error rate of the system is unchanged; the proportion of errors
that are detected decreases.

### Confirmation and anchoring

A request for reasons why a method is appropriate yields reasons for it. A first
draft sets the structure of later versions, including passages that are
subsequently written by hand.

### Sycophancy

Language models tend to confirm positions stated by the user. A hypothesis and
its opposite, presented in separate conversations, can both be assessed
favourably.

Chandra et al. (2026) model a conversation between a chatbot and an *ideal
Bayesian* user who updates beliefs rationally. This user also develops
unwarranted confidence, and the effect persists when the system makes no false
statements and when the user is informed in advance that the system is
sycophantic.

A check carried out with the same system is therefore not an independent check.
Effective countermeasures are procedural: a second reader, a request for
counter-arguments, a source outside the conversation.

### Learning stall

Where a system completes the part of a task that requires effort, the student
submits finished work without having practised the underlying skill. The
deficit becomes visible later, for example in oral examinations or in
subsequent modules.

### Embedded positions

Model outputs contain positions on contested questions of a discipline, on what
constitutes a good argument and on which authorities are cited. When a system
generates a reading list, a seminar question or a case study, the positions
implied should be identified and assessed.

### Deskilling

Evaluating model output requires domain judgement. If this judgement is no
longer exercised because the system performs the task, it declines, and with it
the ability to detect the other failure modes.

Ferdman (2026) describes deskilling as a structural rather than an individual
problem and introduces the concept of a *capacity-hostile environment*: an
environment in which the mediation of a system prevents a capacity from being
developed. Individual resolutions are therefore insufficient. Effective measures
change the environment:

- tasks that are deliberately not routed through a system,
- review steps signed by a person,
- module designs in which the difficulty is part of the learning objective.

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 5 &middot; Grounding: answers with and without a source</div>
<div style="color:#45566a;margin-top:5px;">Comparison of an answer generated from training data with an answer generated from a supplied source text.</div>
</div>

**Aim.** To compare an answer generated from the model's training data with an
answer generated from a supplied source, and to examine whether the two can be
distinguished by reading them.

**Background.** A model's knowledge ends at its training cut-off. *Grounding*
places the relevant source text in the prompt; retrieval-augmented generation
(RAG) automates this step. Grounding reduces unsupported statements but does
not eliminate them.

**Materials.**

- Question: *"Under the EU AI Act, when do the obligations for Annex III
  high-risk systems begin to apply, and what is not deferred?"*
- Source: *"Regulation (EU) 2026/1744 defers the obligations attaching to
  standalone Annex III high-risk systems from 2 August 2026 to 2 December 2027.
  The AI literacy duty in Article 4, the prohibitions in Article 5 and the
  transparency duties in Article 50 are not deferred."*

**Procedure.**

1. Run A sends the question alone.
2. Run B sends source, question and the instruction *"Answer using the source
   only. If the source does not settle the question, say so."*
3. Both runs use temperature 0 and seed 3.
4. Both answers are searched for the year 2027; run A is also checked for an
   opening sentence that declines to answer.

```bash
python -m llmlab lab ground
```

**Predict first.** Will you be able to tell the two answers apart by reading
them?

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

Run A (no source) gave an answer without 2027. Run B (with source) gave an
answer containing 2027. Only the grounded answer contains the date from the
source. **Both answers are phrased with comparable certainty, and neither states
where its information comes from.** Whether an answer is supported by a source
can only be established by comparing it with the source.

</details>

## 1.4 · Quiz — Block 1

Why is the gap between the frameworks and the higher-education teaching role practically relevant?

    [( )] The frameworks contradict each other, so none of them can be applied.
    [(X)] Each framework addresses a different profession, so local adaptation is required.
    [( )] Higher education is exempt from the EU AI Act, so a separate framework is needed.
    [( )] The frameworks predate generative systems and cannot describe them.
    *******************************************************************
    The frameworks are largely compatible, as their shared three-level
    structure shows. They differ in target group. UNESCO names adaptation to
    context as the route of implementation.
    *******************************************************************

Which framework is addressed to institutions rather than to individual teaching staff?

    [( )] AI GO!
    [( )] UNESCO AI CFT
    [(X)] Npuls Reference Framework 2.0
    [( )] DigCompEdu
    *******************************************************************
    Reference Framework 2.0 describes the conditions an institution has to
    establish before AI is used in teaching. It is relevant to committees
    and management rather than to individual course design.
    *******************************************************************

Which failure mode reduces the ability to detect the others?

    [( )] Fabrication, because false references can be published.
    [( )] Illusion of consensus, because it misrepresents a field.
    [( )] Homogenisation, because it makes marking more difficult.
    [(X)] Deskilling, because it reduces the judgement needed to detect the others.
    *******************************************************************
    The other failure modes can be detected by a person with intact domain
    judgement. Deskilling reduces this judgement, which is why countermeasures
    have to be built into the environment in advance.
    *******************************************************************

Which failure modes are detected by checking a single output against a source? (Select all that apply.)

    [[X]] A fabricated reference.
    [[X]] An incorrect date.
    [[ ]] Homogenisation across a set of submissions.
    [[ ]] Automation complacency.
    *******************************************************************
    A reference or a date can be checked against a catalogue or a source.
    Homogenisation is visible only across a set of texts, and complacency
    is a change in the checking itself.
    *******************************************************************

A colleague states that students are warned that the chatbot agrees with everything and are therefore protected. What does the evidence indicate?

    [( )] Correct: a warned user corrects for sycophancy.
    [(X)] In the model, the effect persists when users are warned and when the system states no falsehoods.
    [( )] Correct, provided the students are postgraduates.
    [( )] The effect only occurs in users who already hold unusual beliefs.
    *******************************************************************
    Neither removing false statements nor warning the user eliminated the
    effect in the model of Chandra et al. (2026). Remaining countermeasures
    are procedural: a request for counter-arguments, a second reader, a
    source outside the conversation.
    *******************************************************************

According to Ferdman (2026), which measure addresses deskilling?

    [( )] A personal resolution to check every output carefully.
    [( )] A warning in the module handbook.
    [(X)] A change to the environment, for example a task deliberately not routed through a system.
    [( )] Using a more accurate model.
    *******************************************************************
    In a capacity-hostile environment, individual resolutions are
    insufficient. The environment has to change: tasks kept without AI,
    review steps signed by a person, difficulty as part of the objective.
    *******************************************************************

--------------------------------------------------------------------------------

# 2 · Tools — four areas of use and their consequences

--{{0}}--
Tools are grouped by area of use. The four areas differ in the consequences of
an error for students.

> **Aspect 5.1 → 5.2 — Acquire to Deepen.** The transition consists in assessing
> tools by the obligations their use entails rather than by their functions.

Tools are grouped by **area of use** rather than by provider. The four areas
differ in the consequences of an error for students.

| Area | Examples | Consequence |
| --- | --- | --- |
| **Administration** | minutes, agendas, translations, forms — no student is assessed | low |
| **Preparation** | slides, reading lists, task variants, worked examples — reviewed before use | low |
| **In-class** | captioning, translation, polling — students are present and cannot easily opt out | **Art. 5(1)(f)** adjacent |
| **Evaluation** | feedback, marking support, detection — output affects a student's record | **Annex III point 3 · GDPR Art. 22** |

Ordered by consequence, not by frequency. Most everyday use falls into the first
two areas; most legal requirements concern the last two.

## 2.1 · Tools and their limitations

### Administration

- **Institutional and national platforms.** SURF EduGenAI (Netherlands): a
  national pilot with open-source and commercial models, planned for general
  availability around the end of 2026 and not intended for assessment or fraud
  detection. GWDG Chat AI (Germany), available through the academic cloud. Open
  WebUI and HAWKI: open-source front ends that an institution hosts in front of
  licensed models. *Advantage:* contractual agreement and retention rules.
  *Limitations:* the available models change, so a prompt may behave
  differently from one term to the next, and the service requires operation by
  the institution.
- **Licensed education editions.** Microsoft 365 Copilot Chat with enterprise
  data protection, Gemini for Education and NotebookLM in Google Workspace for
  Education, ChatGPT Edu, Claude for Education. Where an institution has
  concluded a contract, training on institutional data is excluded and
  administrators control retention. *Limitations:* providers are based outside
  the EU, so data residency in the EU determines the storage location but not
  every question of access; terms change faster than institutional review
  cycles; dependence increases with every module built on one provider.
- **European and open models.** Mistral (France), Apertus (Switzerland; ETH
  Zurich, EPFL, CSCS; Apache 2.0; trained on more than a thousand languages) and
  EuroLLM (EU-funded; all 24 official EU languages). Their composition is
  documented. *Limitations:* open models perform below leading commercial models
  on demanding tasks and still require hosting.
- **Local models via Ollama or LM Studio**, as used by llmlab. No data leaves
  the computer. *Limitations:* smaller models perform worse on long documents
  and in languages other than English, and computers without a suitable
  graphics processor are slow.

### Preparation

Task variants, worked examples, annotations for reading lists, question banks
and plain-language versions of handouts. Because the teacher reviews all
material before use, the risk in this area is comparatively low.

- **Transcription.** Open-weight speech models can transcribe recorded lectures
  locally. Error rates increase with technical vocabulary and regional accents,
  and some models generate text during silent passages.
- **Translation.** An EU-based service such as DeepL is suitable for teaching
  material. It is not suitable for students' submitted work (see 2.4).
- **Limitation.** Generating several versions of a task is fast; selecting and
  checking them takes the same time as before.

### In-class

Live captioning and translation improve accessibility; their quality decreases
with background noise, unfamiliar accents and technical vocabulary. They should
be announced as an aid and not used as a record.

Attendance tracking, engagement scoring and participation analytics also belong
to this area. Once their results are used to assess students, they become
evaluation tools.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>Prohibition</strong><br>Systems that infer emotions from faces, voices or posture in education are prohibited under Art. 5(1)(f) AI Act. Consent does not make a prohibited practice lawful.
</div>

### Evaluation

- **Drafting rubrics and criteria.** The teacher designs the instrument; no
  student is assessed by the system.
- **Drafting feedback.** The requirements depend on where the student's text is
  processed (see 2.4).
- **Marking support.** A grade is a decision about a person. Two questions
  follow: whether a person with authority takes the decision, and whether the
  student can contest it.
- **Detection** is discussed in 2.3.

**Automated feedback.** Krommer (2026) describes automated feedback as a choice
between two problems. Feedback general enough to be generated without risk is
too general to change students' work; feedback specific enough to change it has
to be defensible in every sentence, which requires reading the work. A
defensible use consists in drafting with a documented standing instruction
(skill prompt, Block 3) and reviewing the draft before release.

### Publicly available tools and their conditions of use

Students and staff frequently use these tools with personal accounts. **On a
personal account there is no agreement concluded by the institution:** no data
processing agreement, no administrative control over retention, no notification
of changed terms. Such use is suitable for preparation with public material and
unsuitable for student work, personal data, unpublished research and anything
that contributes to a grade.

| Tool | Typical use | Limitations |
| --- | --- | --- |
| **NotebookLM** (Google; also Gemini Notebook) | answers based on uploaded sources, with citations; study guides; audio and video overviews | **A citation does not verify a statement** — it can refer to the correct document while the statement misrepresents it. Audio overviews add emphasis not contained in the sources. Under an institutional Workspace for Education account: core service without human review or training; not on personal accounts. No student work, no third-party copyrighted material. |
| **Free tiers** of ChatGPT, Gemini, Claude, Copilot, Le Chat | drafting, explaining, rephrasing | Conversations may be used for training unless disabled; settings differ and change. The most capable versions require payment (see 2.4). |
| **Perplexity** and other AI search | web answers with links | A link does not establish that the source supports the sentence, nor that the source is reliable. |
| **Elicit, Consensus, Scite** | finding and summarising literature | Incomplete coverage favouring open-access literature in English; summaries omit disagreement between studies. |
| **Image and slide generators** (Canva, Gamma and others) | visual material | Unresolved copyright status, relevant for OER; Art. 50 requires disclosure where generated content is presented to students. |

Each row can be assessed with the three questions of the tool triage page:

1. *Where is the text processed?*
2. *Who has agreed to what?*
3. *What happens if the output is wrong?*

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 7 &middot; Deployment route and legal obligations</div>
<div style="color:#45566a;margin-top:5px;">Processing location of the session's requests and the obligations that depend on it.</div>
</div>

**Aim.** To identify where the requests were processed and which obligations
depend on the deployment route.

**Background.** llmlab sends requests over HTTP to a model server. With the
default configuration the server runs on the same computer and is addressed
through the loopback interface (127.0.0.1). A local route avoids a processor
relationship under GDPR Art. 28 and third-country transfers. Obligations under
the AI Act (Art. 4, Art. 50, Annex III point 3) attach to the use of the system
and apply regardless of where it runs.

**Procedure.** The endpoint of the active backend is read and checked for a
loopback address; the JSON request format of the backend is shown; the
obligations are listed by route.

```bash
python -m llmlab lab route
```

**Predict first.** Which of the obligations listed in 2.2 does a local route
remove?

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

The requests were processed on this computer (loopback address). The route
determines the data-protection obligations: no processor agreement and no
third-country transfer are needed, although a lawful basis for processing is
still required. **The AI Act obligations — Art. 4, Art. 50 and Annex III point
3 — apply regardless of the route.**

</details>

## 2.2 · Legal framework

--{{0}}--
Five provisions and one amended date.

| Provision | Content | Applies since |
| --- | --- | --- |
| **Art. 4 AI Act** | AI literacy of staff | Feb 2025 · not deferred |
| **Art. 5(1)(f) AI Act** | prohibition of emotion inference in workplace and education | Feb 2025 · not deferred |
| **Art. 50 AI Act** | transparency towards people | 2 Aug 2026 · not deferred |
| **Art. 14 AI Act** | human oversight of high-risk systems | with the high-risk obligations |
| **Annex III point 3 AI Act** | education uses listed as high-risk | **2 Dec 2027** (deferred) |

- **Art. 4 — AI literacy.** The deploying organisation, for teaching purposes
  the institution, takes measures to ensure sufficient AI literacy of its staff.
- **Art. 5(1)(f) — prohibited practice.** Inferring the emotions of a person in
  the workplace or in education, except for medical or safety reasons.
- **Art. 50 — transparency.** Persons must be informed when they interact with
  an AI system or receive certain artificially generated content. If a chatbot
  answers students' questions about a module, the deploying institution is
  responsible for this information.
- **Art. 14 — human oversight.** Applies to high-risk systems. Oversight must be
  exercised by persons who understand the system and are able to override its
  output; formal approval without these conditions does not meet the
  requirement.
- **Annex III point 3 — education.** Admission and assignment to institutions,
  evaluation of learning outcomes, assessment of the appropriate level of
  education, and monitoring of prohibited behaviour during tests.

**Amended date.** Regulation (EU) 2026/1744 (Digital Omnibus on AI), published
in the Official Journal on 24 July 2026 and in force since 27 July 2026, defers
the obligations for standalone Annex III high-risk systems from 2 August 2026 to
**2 December 2027**, and for Annex I embedded systems to 2 August 2028. The
stated reason is the delayed availability of harmonised standards. **Articles 4,
5 and 50 were not deferred.** The content of the high-risk obligations is
unchanged; only the date of application has moved, and education remains in
Annex III point 3.

### GDPR Art. 22

A data subject has the right not to be subject to a decision based solely on
automated processing which produces legal effects concerning them or similarly
significantly affects them. A grade is a typical example. Human involvement must
be meaningful: the person involved needs **the authority and the information**
to reach a different decision.

### Tool triage and decision record

The page records the assessment of one tool. It first asks for the area of use,
which determines the legal questions: for evaluation, Annex III point 3, GDPR
Art. 22 and Art. 14 must be answered before the record can be exported; emotion
inference in class leads to the result *decline*. Criteria marked *unclear* are
recorded as conditions.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p2_tool_triage.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the tool triage page in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p2_tool_triage.html).

## 2.3 · AI detectors

--{{0}}--
The principal objection concerns not accuracy but the impossibility of disproof
and the unequal distribution of errors.

The principal objection to detectors in assessment procedures concerns not
their accuracy but the **impossibility of disproof** and the **unequal
distribution of errors**.

**Asymmetric consequences.** A false negative results in a grade that should
have been lower. A false positive can result in disciplinary proceedings, damage
to the relationship with the department and, for some international students,
consequences for residence status. An instrument with such unequal error
consequences has to be assessed against this asymmetry rather than against an
average error rate.

**No possibility of disproof.** Version histories and drafts support a student's
account but can be produced retrospectively. A procedure in which the accused
person has no means of refuting the accusation does not meet the requirements of
a fair academic-integrity procedure (Bassett et al., 2026).

**Unequal distribution of errors.** Detector scores respond to short clauses,
conventional collocations and low lexical variability — also features of
competent academic writing in a second or third language. False positives
therefore occur more frequently among students who write in a language other
than their first, who are often less able to contest an accusation. The
instrument measures, in part, a different property from the one it is intended
to measure.

## 2.4 · Equity and copyright

### Equity of access

The most capable general models are currently available in paid versions. If a
task can be completed better with a subscription, the assessment partly measures
access to paid tools, and this is not visible in the grades.

- A tool that the institution does not provide cannot be made a condition of
  assessment.
- Where the institution provides a compliant option, its timely availability is
  the relevant equity measure.
- Tasks that assume AI use are fair only if all students have been taught the
  use and have comparable access.

### Copyright in students' work

Copyright in examination scripts, term papers and theses belongs to the student.
Uploading such work to a commercial assistant, for example to draft feedback, is
a use of a protected work by the teacher — usually without the student's
knowledge and frequently under terms that allow the provider to retain the text.
This question is separate from data protection and is **not** resolved by
anonymisation, because the protected object is the work itself.

> **Consequence:** student work is processed only with the institutional or a
> local system. Any intended use of an external service is stated in the module
> handbook before submission.

### Scope

This block treats assessment as one of four areas of use. Whether assessment
formats should change, which conditions AI-integrating tasks must meet, and what
the module handbook should state require a separate session.

## 2.5 · Resource consumption

--{{0}}--
Every inference consumes energy, water and hardware capacity.

Every inference consumes energy, water and hardware capacity, regardless of
whether the output is used. In the EU GREEN context this deserves more
attention than a single session can give it.

Measures available at module level:

- use the smallest model that meets the requirements of the task;
- process inputs in batches instead of repeating requests;
- avoid calls to hosted models in teaching materials opened by every student of
  a cohort where a stored answer would suffice.

Lab 7 reports the processing route, which determines where the consumption
occurs.

## 2.6 · Agents and online tests

AI agents can open course pages and PDF files, answer questions and submit
forms. Unsupervised online tests therefore no longer establish that the enrolled
student answered the questions. Practitioner reports describe this in regular
teaching. Detection and extended honour codes do not address the problem;
formats in which the working process itself is the evidence do. Their design is
beyond the scope of this course.

## 2.7 · Resources for departments

**Typology of didactic chatbots (ZML, KIT).** Classifies chatbots by didactic
function — tutor, sparring partner, simulated interlocutor, answering service
for module questions. Each type has specific failure modes and specific
transparency obligations under Art. 50. Classifying by type rather than by
product keeps departmental decisions valid when providers change.

**Faculty-level policy.** The policy of UC Berkeley School of Law (effective
Summer 2026) is an example of a regulation written for a single faculty and its
assessment types, specific enough to be applied in marking. For German law, the
edu-sharing FAQ answers common legal questions. Neither replaces the local
examination office.

**Open courses and support structures.**

- *Students:* Elements of AI (University of Helsinki; free, many languages);
  DigiStudi (iMooX, Austria) for German-speaking first-year students.
- *Staff:* the UNESCO AI competency frameworks; AI GO! (Npuls) for the
  higher-education role; the openly licensed twillo materials (German).
- *National and regional bodies:* SURF and Npuls (Netherlands), Jisc National
  Centre for AI (United Kingdom), KI:Expertisezentrum.nrw (North
  Rhine-Westphalia).

## 2.8 · Quiz — Block 2

A supplier offers a lecture-hall system that identifies students who appear disengaged. Which response is correct?

    [( )] Carry out a data protection impact assessment and proceed if it is positive.
    [( )] Use it only with explicit consent of the students.
    [(X)] Decline: inferring emotions in education is prohibited under Art. 5(1)(f), and consent does not make a prohibited practice lawful.
    [( )] Wait until December 2027, when the high-risk obligations apply.
    *******************************************************************
    Article 5 lists prohibited practices; they cannot be made lawful by
    consent or impact assessments. The deferral to December 2027 concerns
    Annex III high-risk obligations, not the prohibitions, which have
    applied since February 2025.
    *******************************************************************

Which statement about the date of 2 December 2027 is correct?

    [( )] All obligations of the AI Act relating to education were deferred to December 2027.
    [( )] The Article 5 prohibitions and the Article 4 literacy duty were deferred as well.
    [(X)] Annex III high-risk obligations were deferred; Articles 4, 5 and 50 were not.
    [( )] The deferral removed education from Annex III.
    *******************************************************************
    Regulation (EU) 2026/1744 moved the date for standalone Annex III
    high-risk systems because harmonised standards were delayed. The
    prohibitions, the literacy duty and the transparency obligations are
    unchanged, and education remains in Annex III point 3.
    *******************************************************************

Submitted essays are to be processed with a commercial assistant to draft feedback. What does anonymising the files achieve?

    [( )] It resolves both the data protection and the copyright question.
    [(X)] It addresses part of the data protection question and none of the copyright question.
    [( )] It resolves the copyright question, since an anonymous work has no author.
    [( )] Neither, because feedback is always a high-risk use.
    *******************************************************************
    Removing the name reduces identifiability. Copyright protects the work,
    not the name. Drafting feedback is not automatically a use under
    Annex III; awarding a grade can be.
    *******************************************************************

Which of the following does running the model on a local computer remove? (Select all that apply.)

    [[X]] The processor relationship and the transfer of text to a third party.
    [[ ]] The Annex III classification when the output contributes to a grade.
    [[ ]] The Article 50 duty to inform people that they interact with an AI system.
    [[ ]] The Article 4 literacy duty.
    *******************************************************************
    The route determines whether data is transferred. The Annex III
    classification depends on the use, the transparency obligation on what
    people are told, and the literacy duty applies to the deploying
    organisation on every route.
    *******************************************************************

A marking tool proposes grades, and a lecturer clicks "approve" on each without seeing the scripts. What does GDPR Art. 22 say about this?

    [( )] It is compliant, because a person approved every grade.
    [(X)] Human involvement is not meaningful: the person needs the authority and the information to reach a different decision.
    [( )] Art. 22 does not apply to grades.
    [( )] It is compliant until December 2027.
    *******************************************************************
    A formal approval without the information needed to decide differently
    leaves the decision based solely on automated processing. Art. 14 AI
    Act sets a similar condition for human oversight of high-risk systems.
    *******************************************************************

A colleague states that detectors are now accurate enough for use. Which reply addresses the principal objection?

    [( )] Cite the current false-positive rate from the most recent evaluation.
    [( )] Point out that paraphrasing tools defeat detectors.
    [( )] Agree, provided a second marker confirms every flagged case.
    [(X)] Ask what evidence an innocent student could provide to refute the accusation, and point out that errors correlate with first language.
    *******************************************************************
    An error rate treats the question as empirical and can be countered
    with a better rate. The lack of any possibility of disproof and the
    unequal distribution of false positives remain regardless of the error
    rate.
    *******************************************************************

NotebookLM answers with a citation to the uploaded lecture notes. What does the citation establish?

    [( )] That the statement is correct.
    [( )] That the statement is supported by the cited passage.
    [(X)] Only that a document was referenced; the statement can still misrepresent it.
    *******************************************************************
    A citation can point to the correct document while the sentence
    misrepresents it. Only comparison with the source establishes support.
    *******************************************************************

--------------------------------------------------------------------------------

# 3 · Strategies — terminology and the five stages of prompting

--{{0}}--
Six technical terms, each with a direct consequence for decisions in teaching,
and five stages of prompting applied to one example.

> **Aspect 5.2 — Deepen.** Autonomous upskilling and peer coaching. The content
> of this block can be passed on to colleagues directly.

## 3.1 · Six terms and their consequences

The following terms describe technical properties of language models. Each
property has a direct consequence for decisions in teaching; the third column
states the **error that results if the property is not taken into account**.

| Term | Definition | Error if not taken into account |
| --- | --- | --- |
| **Token** | the unit a model processes: a word, part of a word or a punctuation mark from a fixed vocabulary | Text volume is estimated in pages. The same sentence requires more tokens in German or Polish than in English, which affects cost, processing time and usable context. |
| **Context window** | the maximum number of tokens processed in one request, including instructions, documents and answer | A 90-page thesis is summarised and the summary is taken to cover the whole document. Text beyond the window is removed before processing, without notice. |
| **Training vs inference** | model parameters are fixed during use; a conversation does not change them | Corrections in a chat are assumed to be learned and are repeated instead of being written into a standing instruction. Where a system appears to remember, it reads stored text back into the prompt (memory, or a wiki at stage 5). |
| **Grounding** | whether the answer was generated with the relevant source text in the prompt | A fluent answer is treated as a look-up. Only comparison with the source shows whether a source was used. |
| **Temperature and seed** | temperature determines how the next token is sampled; the seed makes sampling repeatable | Two identical scripts receive different comments, and neither can be reproduced when a grade is contested. |
| **Deployment route** | where the text is processed: own computer, institutional server or external provider | A local route is taken to settle all legal questions; Annex III, Art. 50 and Art. 4 still apply. |

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 1–3 &middot; Tokens, context window, temperature</div>
<div style="color:#45566a;margin-top:5px;">Three exercises on the first, second and fifth term of the table.</div>
</div>

**Lab 1 · Tokens.**

- *Background:* a tokenizer divides text into units from a fixed vocabulary
  derived from the training data; languages less represented in that data need
  more tokens per word. Chat models add a template with role markers.
- *Materials:* "Assessment criteria are agreed at programme level." and
  "Bewertungskriterien werden auf Programmebene vereinbart."
- *Procedure:* each text is sent with output limited to one token; the server
  reports the token count. On Ollama the text is sent again without the chat
  template (raw mode); the difference is the template overhead.
- *Measured:* characters per token, tokens per sentence in both languages,
  template tokens.

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

Both sentences together: 107 characters, **18 tokens** (5.9 characters per
token). A simple on-screen approximation estimated 30 tokens — 67 % off the
model's own count. The chat template added **10 tokens**, so the model received
28 in total. Counted separately, the English sentence (7 words) took 8 tokens and
the German sentence (5 words) took 10 tokens — **25 % more for fewer words**.

</details>

**Lab 2 · Context window.**

- *Background:* when a prompt exceeds the window, Ollama removes its beginning
  before processing. The model receives no information that text was removed.
- *Materials:* fictitious examination regulations. § 1 states: "The portfolio
  must be submitted via the learning platform by 12:00 on 15 January 2027."
  § 2 to § 121 contain regulation text on attendance, academic integrity,
  language, format, feedback and accessibility, without dates. The question
  follows the document: "According to the regulations above, by which date
  must the portfolio be submitted? Answer with the date only."
- *Procedure:* the identical prompt is sent with a window of 8,192 tokens and
  with a window of 1,024 tokens (temperature 0, seed 7).
- *Measured:* whether each answer contains the correct date; whether the second
  answer indicates missing information.

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

The prompt comprised 4,211 tokens. With a window of 8,192 tokens the answer was
correct (*15 January 2027*). With a window of 1,024 tokens the answer was
**incorrect**: *"The provided text does not specify a submission date for the…"*.
The model reported missing information — but it could not know that text had
been removed; its statement refers only to the text it received.

</details>

**Lab 3 · Temperature and seed.**

- *Background:* at temperature 0 the most probable token is always selected; at
  higher temperatures sampling introduces variation. A fixed seed makes
  sampling repeatable.
- *Materials:* a request for one sentence of feedback on a student paragraph
  arguing that formative assessment should replace final examinations.
- *Procedure:* four requests at temperature 0 with seed 42; four at temperature
  0.8 without seed.
- *Measured:* number of character-identical outputs per group.

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

Temperature 0 with seed 42: four requests, **one** distinct output. Temperature
0.8 without seed: four requests, **four** distinct outputs. Only the first
configuration allows an output to be reproduced by repeating the request.

</details>

```bash
python -m llmlab lab tokens
python -m llmlab lab context
python -m llmlab lab vary
```

If the narrow window in lab 2 still returns the correct date, `--set sections=200`
increases the proportion of removed text. Windows much smaller than 1,024 tokens
are not applied by current Ollama versions.

## 3.2 · The five stages of prompting

--{{0}}--
The stages differ in what is retained after use, in how many steps are carried
out without intervention, and in which artefacts require review.

| Stage | Description | Artefact |
| --- | --- | --- |
| **1 · Prompt** | one request and one answer in a chat | none |
| **2 · Skill prompt** | a stored instruction with rules and reference material | instruction |
| **3 · Harness** | a program applies fixed steps to many inputs and records them | output files, provenance record |
| **4 · Loop** | automatic checks, revision, stop condition, routing | log of every round |
| **5 · Wiki** | a file of lessons, open questions and approved answers, read by every run | knowledge base under review |

Each stage retains more and delegates more steps to a program — and produces
more artefacts that have to be reviewed. The stages do **not** indicate output
quality: an answer at stage 1 can be as good as one at stage 5.

### Example: replies to student emails

The module team of a fictitious module, *EDU-204 Research Methods in
Education*, receives emails from students. Most concern dates, rooms or
materials and can be answered from the module information. Extensions and grade
changes are decided by the examination office, not by the module team. Requests
concerning other students must not be answered. The example involves many
similar inputs, a reference document, rules whose violation has consequences,
and cases that must be decided by a person, and is therefore suitable for all
five stages.

| Email | Content | Expected handling |
| --- | --- | --- |
| 01 | date and room of the written exam, registration | answer from module information |
| 02 | extension request due to illness | refer to examination office, no promise |
| 03 | availability of slides before the session | not in module information → open question |
| 04 | reading list and office hours (German) | answer in German |
| 05 | request to raise an exam grade | refer to review session and examination office |
| 06 | exam registration of a flatmate | no information; reviewed by a person |
| 07 | sample size of a portfolio study | reviewed by a person |

### Stage 1 — Prompt

Email 02 is pasted with the request *"Answer this email:"*, without instruction
or module information. The model has no information on who decides extensions
and no dates; replies frequently promise the extension ("We will extend your
deadline by one week") or state dates not contained in any source.

*Assessment:* appropriate for one-off tasks. Corrections made in the
conversation are not retained for the next email.

### Stage 2 — Skill prompt

The system prompt contains the specification and the module information. The
specification has ten rules:

1. use only the sources;
2. write a fixed sentence for open questions;
3. no decisions on extensions or grades;
4. no information about other students;
5. no identifiers;
6. reply in the language of the email;
7. salutation and signature;
8. at most 150 words;
9. answer the question asked;
10. copy names of courses, folders and rooms exactly.

Each email is pasted individually.

*Assessment:* the instruction is written once, can be reviewed by colleagues and
is reused. Stored instructions exist as custom instructions, custom GPTs and
Gems, and as `SKILL.md` files in agent tools (published as an open standard in
December 2025). For most teaching staff this stage has the most immediate
practical use. It does not check replies systematically and does not record
which reply was produced with which instruction.

### Stage 3 — Harness

For each email in a folder, a program:

1. sends a classification request that assigns one of five categories
   (*information, extension, grade, third_party, other*);
2. sends a drafting request with the handling rule for that category and the
   system prompt from stage 2;
3. writes the reply to a file with a header recording input, category, route,
   model, settings and time;
4. places the file in `ready/` or `review/`; routing depends on the category
   only, and *third_party* and *other* always go to a person.

*Assessment:* a harness is justified when the same procedure is applied to many
inputs and has to be documented. The provenance record makes each reply
traceable. Because replies are not checked, a reply in an automatic category can
be placed in `ready/` although it violates a rule.

### Stage 4 — Loop

Nine automatic checks test each draft:

| Check | Implementation |
| --- | --- |
| salutation, signature, closing | first line starts with a salutation; signature and a closing in the reply's language in the last three lines |
| word limit | at most 150 words |
| topic | at least one content word of the subject line occurs in the reply (automatic categories only) |
| dates | every date occurs in the module information, an approved answer or the email |
| quoted names | every passage in quotation marks occurs verbatim in the sources |
| no decision | no sentence with "I/we" and *grant, extend, approve, change, raise* without negation |
| examination office named | required for *extension* and *grade* |
| language | frequent German and English function words in email and reply |
| no identifiers | no number with six to eight digits |

Failed checks are returned to the model with the email, the draft and the rule
concerned, and a revised reply is requested. The loop stops when all checks
pass, when the reply contains the sentence for open questions, or after the
maximum number of rounds. A reply is placed in `ready/` only if all checks pass,
the category is automatic and no open question remains.

*Assessment:* the checks and the stop condition determine the quality of the
loop. The checks are text patterns: a reply can pass them and still be wrong,
and a correct reply can fail them. Each round is an additional inference.

### Stage 5 — Wiki

`wiki.md` has three sections:

- *Lessons from failed checks* — written by the program; one line per rule that
  first drafts violated, added to the instructions of later runs.
- *Open questions* — written by the program; emails the sources could not
  answer (email 03 in the example).
- *Approved answers* — written **only by people**, e.g. "The slides for each
  session are uploaded to the learning platform by 18:00 on the day before the
  session." Later runs use these entries as a source.

In the next run email 03 is answered from the approved answer and, if all checks
pass, placed in `ready/`. The process thus handles a growing share of emails
without intervention, while decisions remain with the examination office and
sensitive categories with a person.

*Assessment:* the model does not change; the file does. Whoever can edit the
wiki influences every later reply, errors in it are repeated, and personal data
must not be entered. Karpathy's *LLM wiki* (2026) describes this pattern; memory
functions of commercial assistants follow the same principle without making the
stored text visible.

<div style="border:1px solid #d8c8ee;border-left:5px solid #6b4a9e;border-radius:0 10px 10px 0;background:#f8f5fd;padding:12px 16px;margin:16px 0;">
<div style="font-weight:700;color:#6b4a9e;font-size:0.82em;letter-spacing:0.03em;">LAB 4 &amp; 6 &middot; System prompt; the five stages on the email task</div>
<div style="color:#45566a;margin-top:5px;">Lab 4 compares the position of rules; lab 6 and the harness carry out the five stages.</div>
</div>

**Lab 4 · Rules in the request or in the system prompt.**

- *Materials:* five feedback rules (address the writing, not the writer; quote
  the words at issue; at most two points; end with one answerable question; do
  not rewrite) and the task "Comment on this sentence from a first-year lab
  report: 'The results were quite good and matched what we expected.'"
- *Procedure:* run A task only; run B rules and task in the user message; run C
  rules as system prompt and task as user message. Temperature 0, seed 11.
- *Measured:* number of rules met per run, by five pattern checks.

<details>
<summary><strong>Reference run · gemma3:12b</strong></summary>

Run A (task only) met **3 of 5** rules; run B (rules in the message) and run C
(rules as system prompt) each met **5 of 5**. The rules had an effect; their
position had little effect. The difference that remains is **persistence**: the
system prompt applies to the next request without being repeated.

</details>

**Lab 6 · Five stages.**

- *Materials:* task folder `llmlab/tasks/student_emails` — `spec.md`,
  `context/module_information.md`, `task.json` (categories and handling rules),
  `inputs/` (seven emails), `example_approved_answer.md`.
- *Procedure:* stages 1 and 2 on email 02; stages 3 to 5 on the emails
  (parameter `emails`) with up to three rounds (parameter `rounds`). At stage 5
  the lab inserts the approved answer on slides in place of a decision by the
  module team.
- *Output:* every classification, drafting and revision prompt; checks per
  round; routing; the wiki as written and as read.

<details>
<summary><strong>Reference run · gemma3:12b (all seven emails)</strong></summary>

| Stage | Result |
| --- | --- |
| 1 · Prompt | reply to email 02 passed **4 of 9** checks |
| 2 · Skill prompt | reply to email 02 passed **9 of 9** checks |
| 3 · Harness | 7 emails classified (information 3, extension 1, grade 1, third_party 1, other 1); 5 routed to `ready/` — **2 of these failed at least one check** |
| 4 · Loop | 5 of 7 first drafts passed all checks, 7 of 7 after up to 3 rounds; 4 routed to `ready/` |
| 5 · Wiki | 2 lessons, 1 open question, 1 approved answer; first drafts passing rose from 5 to 6, `ready/` from 4 to 5 |

The checks are text-pattern tests. A reply in `ready/` has passed these tests;
this does not establish that its content is correct.

</details>

```bash
# lab 4 and lab 6
python -m llmlab lab steer
python -m llmlab lab ladder

# stages 3, 4 and 5 on all seven emails, with files written
python -m llmlab harness --task student_emails --out out
python -m llmlab harness --task student_emails --out out --loop 3
python -m llmlab harness --task student_emails --out out --loop 3 --wiki wiki.md
```

After the first stage-5 run, `wiki.md` lists email 03 under *Open questions*.
Adding an entry under *Approved answers*, deleting the open question and running
the command again moves the reply to `ready/`. The checks are defined in
`llmlab/checks.py`; `python -m llmlab copy-task student_emails my_task` creates
an editable copy of the task.

**Try it yourself.** Copy the task and adapt it to a real inbox of your own
module: replace the module information, adjust the categories in `task.json`,
and write three test emails where you expect the process to fail.

## 3.3 · Example of a specified teaching artefact

The following artefact was developed at OvGU with a written specification and is
publicly available.

**Circular construction safety and material twin.** A browser-based simulation
for vocational construction education. It combines live regional weather data, a
fault developing across eight sensor channels, three consultations with
different roles and six material passports that learners route to reuse,
repair, recycling or quarantine, with retained mass, avoided carbon emissions
and avoided replacement costs shown against a circularity score. The learner's
output is a diagnosis, an action and a **written justification**. The
application runs on a static web host without server component or API key.

### Required competences

The development required two kinds of literacy with distinct functions.

| Literacy | Function | Consequence if absent |
| --- | --- | --- |
| **Programming — reading** | understanding the project structure, running it locally, checking and publishing it | The output cannot be checked and has to be trusted. |
| **Programming — architecture** | deciding in advance against a server, keys and a database, based on the obligations each would entail | A generated architecture is accepted, and its data protection consequences become apparent afterwards. |
| **Prompting — specification** | stating constraints, data provenance rules and the pedagogical objective | A generic result that takes longer to correct than a specification would have taken to write. |
| **Prompting — iteration** | developing in small, versioned steps that can be reviewed and reverted | One large request and one large result that cannot be reviewed. |

### Three design decisions with pedagogical rationale

1. **Architecture and data protection.** No login, no accounts and no
   server-side storage: learners' decisions remain in the browser, so no
   personal data is collected. The only external request retrieves public
   weather data and transmits no personal data.
2. **Labelling of data provenance.** Weather values are labelled as live
   external data; concrete, strain, crane-tilt, dust and electrical channels as
   virtual until physical sensors are connected; impact figures as educational
   estimates. Learners know the provenance of every value on which they base a
   decision.
3. **Output as a decision record.** Diagnosis, action and written justification
   form a timestamped process artefact suitable for assessment.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>Purpose and maintenance</strong><br>Before a further artefact of this kind is developed, three questions should be answered in writing: which teaching problem it solves that a seminar does not; what it replaces rather than adds; and who maintains it when the person who specified it is unavailable. An artefact that is not maintained cannot be used as an open educational resource in the long term.
</div>

**Provenance, licensing and repository.** Where substantial parts of an artefact
were generated, its credibility depends on a public record of contributions: who
contributed what, in which commit and on which date. A repository provides this
record by default; a file sent by email does not. If the artefact is a fork, the
relationship to the original is stated on the repository page.

**Transfer to other disciplines.** Select a situation that students cannot
practise because the real setting is dangerous, slow, expensive or rare;
specify it as a system with explicit constraints; develop it in small versioned
steps; label real and simulated data; make a justification rather than a score
the learner's output. Examples include welding, clinical triage, laboratory
safety, negotiation, network incident response and ward handover.

**Legal classification of the example.** No personal data is processed, so data
protection requirements do not apply to the use. No learner is evaluated with
consequences for their studies, so Annex III point 3 does not apply; **it applies
once the score contributes to a grade**. Art. 50 applies to what learners are
told: generated consultation responses are labelled as generated. Art. 4
concerns the staff who deploy such tools and are required to be able to explain
them.

## 3.4 · Three positions from the literature

**AI as an instrument of reflection.** Instead of asking a system to improve a
draft, the instruction asks it to examine the draft: state the claim of a
paragraph, list the conditions under which the claim holds, and identify which
conditions the text does not establish. The student remains the author and
receives questions that a supervisor would ask (ZHQ, FH Aachen, 2026). As a
stored instruction this is a stage-2 artefact that a programme team can adopt,
discuss and revise.

**Academic writing as a process of thinking.** Wampfler (2026) argues that the
debate rests on the assumption that academic writing transcribes finished
thought, which makes its automation appear either harmless or fatal. If writing
is instead the process in which thought is formed, both positions are
untenable, and the relevant question is which parts of this process students
must carry out themselves. This question can be answered for a specific module,
and the answer determines the assessment design.

**AI-generated companion material.** A German-language book on higher education
in the age of generative AI is accompanied by entirely AI-generated slides and
podcasts. A note circulated in the OvGU working group observes that this material
shows the typical weaknesses of such material and that concrete recommendations
are rare. Two criteria follow for evaluating any material, including this
course: whether it states what to do in practice, and whether generated parts
are identifiable.

## 3.5 · Quiz — Block 3

A 90-page thesis is pasted into an assistant, which returns a fluent three-paragraph summary. Which assumption is appropriate?

    [( )] The whole document was processed, since the summary covers the whole argument.
    [(X)] Part of the document may not have been processed, and the answer does not indicate which part.
    [( )] Only the first page was processed, since models read from the beginning.
    [( )] This depends on the file format rather than on the context window.
    *******************************************************************
    Text beyond the context window is removed before processing, and this
    is not reported. Lab 2 demonstrates the effect with a date stated in § 1
    of a regulation.
    *******************************************************************

Two identical scripts receive different AI-drafted comments. A student contests the grade. Which setting would have made the comment reproducible?

    [( )] A longer context window.
    [(X)] Temperature 0 with a fixed seed.
    [( )] A higher temperature.
    [( )] A grounded prompt.
    *******************************************************************
    At temperature 0 with a fixed seed, repeated requests produce the same
    output (Lab 3: one distinct output from four requests). Without a seed
    and at temperature 0.8, four requests produced four different outputs.
    *******************************************************************

You correct the assistant in a chat ("never promise extensions"). What happens in a new conversation next week?

    [( )] The model has learned the rule.
    [(X)] The rule is not applied unless it is stored and sent again, for example in a skill prompt.
    [( )] The rule applies only to emails about extensions.
    *******************************************************************
    Model parameters are fixed during use. Where a system appears to
    remember, stored text is read back into the prompt.
    *******************************************************************

At stage 3 of the email example, the reply to email 02 promises an extension and is routed to `ready/`. Which stage prevents this, and how?

    [( )] Stage 2, because the specification prohibits promises.
    [( )] Stage 3, because the provenance header records the category.
    [(X)] Stage 4, because the reply fails the decision check and is revised or routed to review.
    [( )] Stage 5, because the model learns not to promise extensions.
    *******************************************************************
    A rule in the specification does not ensure compliance. At stage 4 the
    decision check detects the sentence; the reply is revised or, if the
    check still fails, routed to review. At stage 5 the model does not
    change; only the wiki file does.
    *******************************************************************

Which of the following is a stage-2 artefact (skill prompt)?

    [( )] A well-phrased request that produced a good answer.
    [(X)] A stored instruction stating rules, reference material and prohibitions.
    [( )] A six-turn conversation that arrived at the right output.
    [( )] A folder of replies with provenance headers.
    *******************************************************************
    A skill prompt is written once, can be read by colleagues and is reused.
    A conversation remains stage 1; a folder of replies with provenance
    headers is the artefact of stage 3.
    *******************************************************************

What is a stage-5 wiki in the email example?

    [( )] A retrained version of the model.
    [( )] The conversation history of the chat.
    [( )] The folder of reply files with provenance headers.
    [(X)] A text file with lessons and open questions written by the program and approved answers written by people, read by every later run.
    *******************************************************************
    The model parameters remain unchanged. The wiki is a text file that can
    be read, corrected and versioned; the reply files are the artefact of
    stage 3.
    *******************************************************************

A reply has passed all nine checks and is in `ready/`. What does this establish?

    [( )] The reply is correct.
    [(X)] The reply matches the text patterns the checks test for; its content can still be wrong.
    [( )] The examination office has approved the reply.
    *******************************************************************
    The checks are text patterns. A reply can pass them and still be wrong,
    and a correct reply can fail them.
    *******************************************************************

The construction simulation labels its concrete and strain values as virtual. Why is this labelling pedagogically relevant?

    [( )] It protects the authors from liability if a learner acts on a wrong value.
    [( )] It allows real sensor data to be added later without changing the code.
    [(X)] Learners justify decisions, and a justification can only be assessed if the provenance of the evidence is known.
    [( )] The AI Act requires simulated values in educational software to be labelled.
    *******************************************************************
    The assessed output is the justification. A justification based on
    evidence of unknown provenance cannot be assessed.
    *******************************************************************

--------------------------------------------------------------------------------

# 4 · Reflection — and the route to Create

--{{0}}--
Levels reached by the course and levels that require further work.

> **Aspect 5.2 → 5.3 — Deepen to Create.** Human-controlled uses of AI for
> collaborative professional development, moving towards AI-enhanced design of
> training programmes.

This block states which levels the course reaches and which require further
work.

| Level | Content | Status |
| --- | --- | --- |
| **Acquire** | rights and obligations · readiness self-assessment · human-directed use | reached in the course |
| **Deepen** | autonomous upskilling · peer coaching · collaborative development | begun in two places |
| **Create** | hybrid coach · programme design · communities of co-creation | not reached in 90 minutes |

**Conditions of the Create level.** Create requires other people, a review cycle
and a published artefact. A period of about ninety days is realistic; the plan
in Block 5 is designed for this period.

## 4.1 · Three reflection questions

Take ten minutes and write down your answers. They are the raw material of your
90-day plan.

**Question 1 — Which task remains without AI support, and why?**
Name one task that continues to be carried out without AI support because the
judgement it requires is needed to evaluate AI output in other tasks. State the
reason in writing; a task for which no such reason can be given is not a
suitable answer.

The Wissenschaftsrat uses the term **intellectual sovereignty** for the capacity
to judge independently, critically and with reasons in a world shaped by these
systems. The term locates the objective in the person and makes judgement,
rather than output, the target of teaching. Combined with Ferdman's concept of
capacity-hostile environments (1.3), question 1 has a structural answer: the
task has to be anchored in the module design, a deadline or a review step, where
it is visible to others.

**Question 2 — Which past decision would now be taken differently?**
One decision from the last twelve months: a tool adopted, a task set, a
statement in a module handbook, feedback drafted with an unsuitable tool. Name
the legal provision or the principle that changes the assessment, so that the
conclusion can be communicated to colleagues.

**Question 3 — Who else should be informed?**
Name one person and one piece of information. In Aspect 5, peer coaching is the
activity named for the Deepen level.

## 4.2 · Levels covered

| Aspect 5 level | Covered by the course | Not covered |
| --- | --- | --- |
| **Acquire** (5.1) | Rights and obligations with legal references; readiness self-assessment; human-directed use examined on a local model (`python -m llmlab all`). | Complete if the [self-check](pages/p1_self_check.html) was carried out. |
| **Deepen** (5.2) | Begun in two places: the tool decision record and the stage-2 skill prompt, both of which can be reviewed and passed on. | No peer coaching; no use of data on one's own practice to guide development. |
| **Create** (5.3) | Described with one example and planned over ninety days. | **Not attempted.** Requires a community, a review cycle and a published artefact. |

### 90-day plan

The last line of the self-check from Block 0 is pasted into the page; the two
largest gaps become the two development areas, and no third area can be added.
Each area receives two dated tasks at the target level. Tasks can be edited and
added, and the plan can be exported as a calendar file.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p3_cpd_plan.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the plan page in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V7/pages/p3_cpd_plan.html).

## 4.3 · Quiz — Block 4

Why is the Create level not reached in a 90-minute session?

    [( )] It requires programming skills that take longer than 90 minutes to acquire.
    [( )] It is reserved for staff in formal educational development roles.
    [( )] It applies only to institutions with an approved AI strategy.
    [(X)] Its activities require other people, a review cycle and a published artefact.
    *******************************************************************
    Hybrid coaching, designing training for others and co-creating with a
    community involve other people over time. The limitation is social and
    temporal rather than technical.
    *******************************************************************

Which is a suitable answer to reflection question 1?

    [( )] "I will not use AI for anything, to be safe."
    [(X)] "I keep marking the first essay of each cohort by hand, because that is where I calibrate the judgement I need to check AI-drafted feedback — the step is fixed in the module's marking schedule."
    [( )] "I will try to check AI output more carefully from now on."
    *******************************************************************
    The answer names one task, gives the reason (the judgement is needed to
    evaluate AI output elsewhere) and anchors it in the environment, where
    it is visible to others. A general resolution does not.
    *******************************************************************

A colleague uses no AI at all and says none of this applies to them. Which reply is accurate?

    [( )] Correct: the obligations only concern people who use AI.
    [(X)] Reasoned non-use is a legitimate decision, but the Art. 4 literacy duty applies to the institution and is discharged by staff who can explain the tools in use.
    [( )] They must start using AI to comply with Art. 4.
    *******************************************************************
    Deciding not to use AI for a task, for a stated reason, is itself a
    competence; deciding by default is not. Students use these tools
    regardless, and AI is embedded in many systems already in use.
    *******************************************************************

--------------------------------------------------------------------------------

# 5 · Plan and summary

--{{0}}--
The plan is limited to two development areas.

> **Aspect 5.3 — Create, preparation.** AI-enhanced design of training
> programmes: a dated list of tasks.

The plan is limited to two development areas. Plans with many areas are
frequently discontinued within a few weeks, which is then attributed to the
person rather than to the scope of the plan.

**Four options for further work:**

1. **Adapt the session** for a department or discipline. All material is CC BY
   4.0; tool examples can be replaced with those used locally, the legal panel
   remains valid. About one afternoon of adaptation, 90 minutes of delivery.
2. **Mentor one colleague.** One person, four meetings over a term, with the aim
   that the colleague completes a tool decision record independently. This is
   the activity named for Deepen.
3. **Publish one artefact** — a task specification, rubric, decision record,
   skill prompt or small simulation — openly licensed, with version history and
   attribution.
4. **Establish a practice group** of at least three people with regular
   meetings, for the joint development of tools, methods or rules. The result is
   a documented set of decisions with dates and reasons, from which a policy can
   later be derived.

### Written commitment

> *By [date], I will [specific action] so that [named colleague or group] can
> [outcome].*

A commitment without a date cannot be reviewed; a commitment without another
person does not correspond to the collaborative activities described in Aspect 5.

**Write yours down** — on paper or in the 90-day plan page — and send it to the
person it names.

## Summary

- Models process tokens, and the context window limits the text processed in one request; text beyond it is removed without notice.
- The wording of an answer does not show whether it is based on a source; only comparison with the source does.
- The deployment route determines data-protection obligations; obligations under the AI Act apply regardless of the route.
- Art. 5(1)(f) is a prohibition and cannot be satisfied by an impact assessment or consent.
- Annex III obligations were deferred to 2 December 2027; Articles 4, 5 and 50 were not.
- Copyright in student work is not resolved by anonymisation.
- The five stages of prompting differ in what is retained, which steps are automated and which artefacts require review; automatic checks approximate rules and do not establish correctness.
- Deskilling is a structural problem; countermeasures change the environment.
- Tools, strategies and reflection build on one another.

### Further reading and self-study route

Three central sources: Ferdman (2026) on deskilling as a structural problem; the
recommendations of the Wissenschaftsrat (2026) for the German context; Chandra
et al. (2026) on the persistence of sycophancy effects despite warnings.

Five open LiaScript modules written for teachers in vocational education, under
the UNESCO-UNEVOC ASSET co-initiative, cover the basics in about four hours of
self-study:

- **AI Orientation** — lifelong professional learning
- **AI Basics** — non-anthropomorphic description of AI systems and human agency
- **AI Tools** — system types, data origin, OER
- **Prompting** — the structure a standing instruction needs
- **Quality and Ethics** — bias, ethics and the human-rights framing

Their examples are taken from electronics. Blocks 2 and 3 of this course cover
content that the modules do not address.

## Final quiz

Which statements are correct? (Select all that apply.)

    [[X]] Text beyond the context window is removed without notice.
    [[ ]] A local model removes all obligations under the AI Act.
    [[X]] Art. 5(1)(f) cannot be satisfied by consent.
    [[ ]] At stage 5 the model learns from approved answers.
    [[X]] A check with the same system is not an independent check.
    *******************************************************************
    A local route removes the processor relationship only. At stage 5 the
    model does not change; the wiki file does. Sycophancy persists even when
    users are warned, so independent checks need a second reader or a source
    outside the conversation.
    *******************************************************************

Why is the 90-day plan limited to two areas?

    [(X)] Because plans with many areas are frequently discontinued within a few weeks.
    [( )] Because the UNESCO framework prescribes at most two competences per cycle.
    [( )] Because the two areas correspond to the Acquire and Deepen levels.
    [( )] Because institutional budgets usually cover two activities.
    *******************************************************************
    The limit is a practical decision, not a requirement of the framework.
    It keeps the plan feasible within the period.
    *******************************************************************

Which commitment meets both conditions stated in Block 5?

    [( )] "I will learn more about AI this term."
    [( )] "By 1 December I will rewrite my feedback prompt."
    [(X)] "By 1 December I will share my feedback skill prompt with the module team so that they can review and reuse it."
    *******************************************************************
    A reviewable commitment needs a date and another person. The first has
    neither; the second has no other person.
    *******************************************************************

--------------------------------------------------------------------------------

# Appendix — References

--{{0}}--
All sources cited in this course, grouped by subject.

A large part of the sources added since version 4 comes from the reading list
of the OvGU working group on AI and digitality in study and teaching. Links were
checked at the time of writing. Unpublished items and items without a stable
link are marked as such.

## Competence frameworks

1. Miao, F. & Cukurova, M. (2024). *AI competency framework for teachers.* UNESCO, Paris. CC BY-SA 3.0 IGO. <https://unesdoc.unesco.org/ark:/48223/pf0000391104>
1. UNESCO (2024). *AI competency framework for students.* UNESCO, Paris. <https://unesdoc.unesco.org/ark:/48223/pf0000391105>
1. OECD & European Commission (2026). *Empowering Learners for the Age of AI: an AI literacy framework (AILit).* Addressee: primary and secondary learners. <https://ailiteracyframework.org>
1. Redecker, C. (2017). *European Framework for the Digital Competence of Educators: DigCompEdu.* JRC Science for Policy Report, Publications Office of the EU. <https://joint-research-centre.ec.europa.eu/digcompedu_en>
1. Vuorikari, R., Kluzer, S. & Punie, Y. (2022). *DigComp 2.2: The Digital Competence Framework for Citizens.* JRC128415. Adds examples concerning AI systems. <https://publications.jrc.ec.europa.eu/repository/handle/JRC128415>
1. UNESCO (2018). *UNESCO ICT Competency Framework for Teachers, version 3.* Origin of the three-level acquisition / deepening / creation grammar. <https://unesdoc.unesco.org/ark:/48223/pf0000265721>
1. Npuls (2025). *AI GO! AI Literacy in Education — a practical framework.* Addressed to education professionals in mbo, hbo and wo; the closest published comparator to a higher-education-facing framework. <https://npuls.nl/en/knowledge-base/ai-go-ai-literacy-in-education-a-practical-framework>
1. Npuls (2025). *Reference Framework 2.0 — Responsible use of education data and AI.* Governance-facing companion to AI GO!; written for institutions rather than individuals. <https://npuls.nl/en/knowledge-base/reference-framework-2-0-responsible-use-of-education-data-and-ai>
1. Long, D. & Magerko, B. (2020). *What is AI literacy? Competencies and design considerations.* CHI '20. Competence list adopted by many later frameworks. <https://doi.org/10.1145/3313831.3376727>

## Policy, recommendations and institutional practice

1. Wissenschaftsrat (2026). *Intellektuelle Souveränität: Empfehlungen für die Hochschulbildung in Zeiten von generativer KI.* Drs. 3319-26, Köln, July 2026. doi:10.57674/1evx-t906. Argues that the relevant question is how good higher education is designed in a world shaped by generative AI. <https://www.wissenschaftsrat.de/download/2026/3319-26>
1. OECD (2026). *Policies supporting responsible and systematic GenAI adoption in higher education.* OECD Education Policy Perspectives. <https://www.oecd.org/en/publications/policies-supporting-responsible-and-systematic-genai-adoption-in-higher-education_c4e5621f-en.html>
1. Hochschulforum Digitalisierung (2026). *Generative KI in der Hochschullehre — wie wir Innovation verantwortungsvoll gestalten.* <https://hochschulforumdigitalisierung.de/genki-in-der-hochschullehre/>
1. UC Berkeley School of Law (2026). *Artificial Intelligence Policy, effective Summer 2026.* Example of a policy at the level of a single faculty. <https://www.law.berkeley.edu/wp-content/uploads/2026/05/AI-Final-Policy-26.pdf>
1. heise online (2026). *Leiden Declaration: Mathematiker fordern bewussten Umgang mit KI — „Don't believe the hype“.* Example of guidance issued by a discipline. <https://www.heise.de/news/Mathematiker-fordern-bewussten-Umgang-mit-KI-Don-t-believe-the-hype-11378210.html>
1. KI:Expertisezentrum.nrw (2026). *Regional AI competence centre for higher education in North Rhine-Westphalia.* An example of the regional support structure the Wissenschaftsrat recommendations call for. <https://ki-expertisezentrum.nrw/>
1. Universität zu Köln (2026). *Universität zu Köln ist Teil des neuen KI:Expertisezentrum.nrw.* <https://uni-koeln.de/universitaet/aktuell/meldungen/meldungen-detail/universitaet-zu-koeln-ist-teil-des-neuen-kiexpertisezentrumnrw>
1. HIS-HE (2026). *Perspektiven einer KI-unterstützten offenen Bildungspraxis.* <https://his-he.de/publikation/perspektiven-einer-ki-unterstuetzten-offenen-bildungspraxis/>

## Law

1. European Union (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act).* Arts. 4, 5(1)(f), 14, 50; Annex III §3. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
1. European Union (2026). *Regulation (EU) 2026/1744 (Digital Omnibus on AI).* OJ 24 July 2026, in force 27 July 2026. Defers standalone Annex III high-risk obligations to 2 December 2027. Arts. 4, 5 and 50 not deferred. <https://eur-lex.europa.eu>
1. European Union (2016). *Regulation (EU) 2016/679 (GDPR).* Arts. 5 and 22. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
1. edu-sharing / Open Innovation Community (2026). *KI in der Bildung — Rechtliche Orientierung für Bildungseinrichtungen und Lehrkräfte (FAQ).* German-language legal FAQ on common questions. <https://edu-sharing.atlassian.net/wiki/spaces/OIC/pages/1891565573/>

## How the systems fail — the evidence base

1. Ferdman, A. (2026). *AI deskilling is a structural problem.* *AI & Society* 41, 3001–3013. doi:10.1007/s00146-025-02686-z. Introduces *capacity-hostile environments*: settings in which AI mediation blocks the cultivation of a capacity, so that deskilling is a property of the environment rather than a failure of individual willpower. <https://doi.org/10.1007/s00146-025-02686-z>
1. Chandra, K., Kleiman-Weiner, M., Ragan-Kelley, J. & Tenenbaum, J. B. (2026). *Sycophantic chatbots cause delusional spiraling, even in ideal Bayesians.* arXiv:2602.19141. A Bayesian model in which even a perfectly rational user spirals; the effect survives both removing hallucination and warning the user that the system is sycophantic. <https://arxiv.org/abs/2602.19141>
1. Bassett et al. (2026). *Heads we win, tails you lose: AI detectors in education.* Source of the arguments on disproof and asymmetric consequences in Block 2.
1. Forschung & Lehre (2026). *Zahl falscher KI-Referenzen in Forschungsarbeiten nimmt zu.* <https://www.forschung-und-lehre.de/forschung/zahl-falscher-ki-referenzen-in-forschungsarbeiten-nimmt-zu-7760>
1. CheckIfExist (2026). *Detecting citation hallucinations in the era of AI-generated content.* arXiv:2602.15871. <https://arxiv.org/abs/2602.15871>
1. BibFox (2026). *Reference verification service.* Reference verification tool with its own error rate. <https://bibfox.com/en/solutions/reference-verification>
1. Tagide (2026). *The anatomy of a learning stall.* On learning when productive difficulty is omitted. <https://tagide.com/blog/llm/the-anatomy-of-a-learning-stall/>
1. Golem.de (2026). *KI-Agenten übernehmen marxistische Ansichten.* Report on value drift in populations of AI agents. <https://www.golem.de/news/kuenstliche-intelligenz-ki-agenten-uebernehmen-marxistische-ansichten-2605-208696.html>
1. Springer / IJETHE (2026). *Generative AI literacy across education and business: competencies, obstacles, and benefits — a systematic literature review.* <https://link.springer.com/article/10.1186/s41239-026-00596-8>

## Teaching practice, didactics and commentary

1. Krommer, A. (2026). *KI-Feedback. Oder: die Entscheidung zwischen Skylla und Charybdis.* On automated feedback as a choice between feedback that is too general to be useful and feedback that is too specific to be defensible without reading the work. <https://axelkrommer.com/2026/07/25/ki-feedback-oder-die-entscheidung-zwischen-skylla-und-charybdis/>
1. ZML, Karlsruher Institut für Technologie (2026). *Didaktische Chatbot-Typen — Beispiele für Ihren Einsatz.* Classification of chatbots by didactic function. <https://www.zml.kit.edu/didaktische-chatbots.php>
1. ZHQ, FH Aachen (2026). *KI als Reflexionsinstrument im wissenschaftlichen Arbeiten.* <https://zhq-blog.fh-aachen.de/kompetenzen-studierende/ki-als-reflexionsinstrument-im-wissenschaftlichen-arbeiten/>
1. Hochschulforum Digitalisierung (2026). *Warum KI-Agenten das Ende klassischer Onlinetests einleiten.* <https://hochschulforumdigitalisierung.de/ki-agenten-in-onlinetests/>
1. Moodle (2026). *Feldnotizen: Wenn KI-Agenten in der Klasse auftauchen.* Practitioner field notes. <https://moodle.com/de/nachrichten/feldnotizen-wenn-ki-agenten-in-der-klasse-auftauchen/>
1. Wampfler, P. (2026). *Wissenschaftliches Schreiben und KI — wie ein fundamentales Missverständnis die Lehrentwicklung blockiert.* <https://schulesocialmedia.com/2026/06/16/wissenschaftliches-schreiben-und-ki-wie-ein-fundamentales-missverstandnis-die-lehrentwicklung-blockiert/>
1. Lehrwende (2026). *Lehrwende — Hochschulbildung im Zeitalter generativer KI.* Its companion material (slides, podcasts) is AI-generated. <https://lehrwende.de/>
1. twillo (2026). *Handlungsempfehlungen für Hochschullehrende zum Einsatz von Künstlicher Intelligenz.* OER, German. <https://www.twillo.de/edu-sharing/components/render/27d39f95-eada-4cec-939f-95eada0cec80>
1. twillo (2026). *KI-Literacy — Grundlagen und Orientierung für Lehrende.* OER, German. <https://www.twillo.de/edu-sharing/components/render/2e1ef4ad-15e0-4d17-af45-4c7223041966>
1. Springer (2026). *GenAI in novel educational applications: practices of integrating GenAI in the K-12 classroom.* <https://link.springer.com/book/10.1007/978-3-032-16153-6>
1. In Preparation (Substack) (2026). *Opinion: I was not allowed to type prompts into ChatGPT during my chalk talk.* Opinion piece on tool access in assessment. <https://inpreparation.substack.com/p/opinion-i-was-not-allowed-to-type>

## Open offers you can point students and colleagues at

1. iMooX (2026). *DigiStudi — Digitale Kompetenzen für Studienanfänger*innen.* Open course for first-year students. <https://imoox.at/course/DigiStudi>
1. Deutscher Bildungsserver (2026). *complett — Portal für Bildungsressourcen.* <https://complett.bildungsserver.de/>
1. University of Helsinki & MinnaLearn (2018–). *Elements of AI.* Free introductory course in many languages. <https://www.elementsofai.com>
1. KI-Campus (2026). *KI-Campus — die Lernplattform für Künstliche Intelligenz.* German-language course platform, including modules for educators. <https://ki-campus.org/>

## Tools named in Block 2

1. SURF & Npuls (2026). *EduGenAI — a generative AI platform for Dutch education.* National pilot for mbo, hbo and wo institutions; open-source and commercial models; not for assessment or fraud detection. <https://www.surf.nl/en/themes/artificial-intelligence/projects-and-collaborations/ai-hub>
1. Utrecht University (2026). *EduGenAI — AI policy for teachers.* Institutional information on the pilot and its limits. <https://www.uu.nl/en/organisation/ai-policy/teachers/edugenai>
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
1. Anthropic (2025). *Effective context engineering for AI agents.* On the design of the information provided to agents. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
1. Karpathy, A. (2026). *llm-wiki.* GitHub gist, 4 April 2026. An idea file for a markdown knowledge base that an LLM agent builds and maintains from raw sources. Stage five. <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## This session

1. EduGreenLabs / OvGU Magdeburg (2026). *Workshop 4 — AI in Teaching: Tools, Strategies and Reflection.* This session. Page, LiaScript course and `llmlab`. CC BY 4.0.
1. EduGreenLabs / OvGU Magdeburg (2026). *llmlab — seven exercises on language models, run on a local model.* Version 2.0. Python 3.9+, standard library only. CC BY 4.0.
1. UNESCO-UNEVOC / ASSET Co-initiative, OvGU (2026). *Self-learning nuggets: AI Orientation, AI Basics, AI Tools, Prompting, Quality and Ethics.* Five LiaScript modules written for TVET teachers; recommended in Block 5 as a self-study route into the basics.

--------------------------------------------------------------------------------

# Licence and provenance

**AI in Teaching: Tools, Strategies and Reflection**, version 7, September 2026.
EduGreenLabs / OvGU Magdeburg — WP2 Training Lab, EU GREEN Alliance.

Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Funded by the
European Union. Views expressed are those of the authors alone.

The UNESCO AI Competency Framework for Teachers is licensed CC BY-SA; this course
paraphrases and attributes it rather than reproducing its wording, because this
course is licensed CC BY.

**Changes from version 6:** the unpublished draft competence framework and the
placement map (former Appendix A) removed; the self-study course now carries the
full explanatory text, a quiz for every block and a final quiz, while the live
page shows key points only; reference results of all seven lab exercises
(gemma3:12b) added; content previously only on the live page added (Reference
Framework 2.0, confirmation and anchoring, embedded positions, transcription and
translation, required competences for the teaching artefact, legal
classification of the example).

**Companion files:** `masterclass_ai_in_teaching_v7_labs.html` (live version
with lab results) · `llmlab/` (the seven lab exercises) · `pages/` (self-check,
tool triage, plan) · `REFERENCES.md` (bibliography).
