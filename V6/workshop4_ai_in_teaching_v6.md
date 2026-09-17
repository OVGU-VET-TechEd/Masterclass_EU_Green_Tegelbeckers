<!--
author:   Hannes Tegelbeckers · EduGreenLabs / OvGU Magdeburg
email:    hannes.tegelbeckers@ovgu.de
version:  6.0.0
language: en
narrator: UK English Male
comment:  Workshop 4 of the EU GREEN WP2 Training Lab. AI in higher education
          teaching — tools, strategies and reflection — with a placement map
          against a higher-education AI competence framework.
license:  CC BY 4.0

-->

# AI in Teaching: Tools, Strategies and Reflection

--{{0}}--
This is the self-study version of the EU GREEN Training Lab session on AI in
teaching. It contains the content of the session, the lab exercises and a
placement map against a competence framework.

<div style="background:linear-gradient(118deg,#e7eefa 0%,#eef2f8 55%,#f1ebf9 100%);border-bottom:2px solid #1a4a88;padding:22px 20px;border-radius:10px;">
<div style="color:#45566a;font-size:0.82em;">EU GREEN · Transformative Teaching and Learning · WP2 Training Lab · Workshop 4 · <strong>version 6</strong></div>
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
The course can be used in three ways.

**Teaching.** The live version is `masterclass_ai_in_teaching_v6.html`. This
file is the self-study and re-publication version. All material is licensed
CC BY 4.0.

**Self-study.** About two hours, including the lab exercises. Seven exercises
examine statements of the course on a model running on the participant's own
computer.

**Placement.** [Appendix A](#appendix-a--the-placement-map) relates common
teaching practices to competences. Selecting the most frequent own practice
shows the competences exercised and the competences needed first.

### Requirements for the lab

The lab is a Python package, `llmlab` (folder `V6/llmlab`). Python 3.9 or later,
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

## 0 · Structure and outcomes

--{{0}}--
Target group, outcomes and structure of the course.

The course does not train software development. It addresses decisions that
teaching staff make about tools, assessments and module handbooks and that now
have technical preconditions: where text is processed, how outputs are
produced, and which obligations follow. The competence addressed is the
ability to take such decisions and to justify them.

**Outcomes:**

1. A self-assessed readiness profile — [self-check page](pages/p1_self_check.html).
2. A decision record for one tool — [tool triage page](pages/p2_tool_triage.html).
3. Results of seven lab exercises on a local model (`python -m llmlab all`).
4. A dated 90-day plan with two development areas — [plan page](pages/p3_cpd_plan.html).

> **UNESCO AI CFT, Aspect 5.1 — Acquire.** Awareness of teachers' rights and
> obligations in the AI era. Each block of this course is assigned to a level
> of Aspect 5.

### Readiness self-check

Eight statements. For each statement, select the level that describes current
practice: **Not yet**, **Acquire**, **Deepen** or **Create**. The page returns
a profile and names the two largest gaps; the 90-day plan in Block 5 is based
on them. No data is transmitted or stored; the result can be exported.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p1_self_check.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the self-check in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p1_self_check.html).

--------------------------------------------------------------------------------

# 1 · Competences — frameworks and their target groups

--{{0}}--
A competence framework describes competences at defined levels. Used for
self-assessment, it identifies competences that are not yet developed.

> **Aspect 5.1 — Acquire.** Self-assessment of readiness for teaching in the AI era.

## 1.1 · Six frameworks and their target groups

| Framework | Target group | Content |
| --- | --- | --- |
| **UNESCO AI CFT** (2024) | school teachers | 5 aspects × 3 levels; Aspect 5 structures this course |
| **AILit** (2026, OECD/EC) | primary and secondary **learners** | AI literacy that incoming students can be expected to have |
| **DigCompEdu** (2017) | educators, EU | 22 competences; predates generative systems |
| **DigComp 2.2** (2022) | citizens | adds examples concerning AI systems |
| **ICT-CFT** (2018) | teachers | origin of the three-level structure |
| **AI GO!** (2025, Npuls) | education professionals including **higher education** | the published framework closest to the higher-education teaching role |

{{1}}
**The level structure is shared; the target groups differ.** Rows compare
levels; columns compare frameworks written for different professions.

{{1}}
| | first level | second level | third level |
| --- | --- | --- | --- |
| ICT-CFT 2018 | acquisition | deepening | creation |
| UNESCO AI CFT 2024 | **Acquire** | **Deepen** | **Create** |
| DigCompEdu 2017 | A1 · A2 | B1 · B2 | C1 · C2 |
| HETAICF v0.11 (draft) | Foundation | Applied | Advanced |

### The gap

The higher-education teaching role — with research obligations, examination
regulations, academic freedom and doctoral supervision — is covered by these
frameworks only in part.

AI GO! narrows the gap because it addresses education professionals in
vocational colleges, universities of applied sciences and research
universities. What remains are national elements: examination regulations,
the legal framework and the supervision relationship. These elements are
limited in number, which supports adapting an existing framework rather than
developing a new one.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>HETAICF v0.11 — unpublished draft, under review.</strong><br>A working group at OvGU is drafting a framework for teaching in higher education. It is used in this course as an example of local adaptation and, in Appendix A, for its structure. Its numbering will change; competence identifiers must not be cited as authoritative.
</div>

### National recommendations (Germany)

The Wissenschaftsrat published recommendations in July 2026 under the guiding
concept of **intellectual sovereignty**: the capacity to judge independently,
critically and with reasons in an environment shaped by algorithms. Its
central argument is that the relevant question is not how higher education is
designed *with* generative AI, but how good higher education is designed in a
world shaped by it.

## 1.2 · Three layers of competence

--{{0}}--
AI-specific competence builds on digital competence and pedagogical judgement.

| Layer | Content |
| --- | --- |
| **AI-specific competence** | system behaviour, limits, accountability |
| **Digital competence** | files, platforms, accessibility, data protection |
| **Pedagogical judgement** | purpose of the assessment, intended learning outcomes |

Most questions raised by AI in teaching are established questions — whether an
assessment measures what it is intended to measure, who holds the data, whether
a decision can be justified to the person affected — under changed conditions.
The course is therefore organised by teaching questions rather than by
technology.

## 1.3 · Limits of trust in model output

--{{0}}--
Fabricated content can be detected by comparison with sources. The other
failure modes affect the judgement of the person using the system.

### Fabrication

A language model generates text that is probable given the input; probability
is not the same as correctness. Invented references are the best-known case
and can be detected by checking each reference against a catalogue.

Fabricated references in research papers are reported as increasing, and
verification tools have appeared. These tools have their own error rates and
data routes and should be documented together with the tool whose output they
check.

### Homogenisation

Texts produced with the same system tend to share structure, register and
choice of examples. Each text may be acceptable, while a set of submissions or
module descriptions shows little variation.

### Illusion of consensus

A summary of a disputed research question can read as a coherent position. The
disagreement is not stated as absent; it is omitted.

### Automation complacency

After a series of correct outputs, users check subsequent outputs less
carefully. The error rate is unchanged; the proportion of detected errors
decreases.

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
submits finished work without having practised the underlying skill.

### Deskilling

Evaluating model output requires domain judgement. If this judgement is no
longer exercised, it declines, and with it the ability to detect the other
failure modes.

Ferdman (2026) describes deskilling as a structural problem and introduces the
concept of a *capacity-hostile environment*: an environment in which the
mediation of a system prevents a capacity from being developed. Individual
resolutions are therefore insufficient. Effective measures change the
environment: tasks that are deliberately not routed through a system, review
steps signed by a person, and module designs in which the difficulty is part of
the learning objective.

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

## 1.4 · Quick check — Block 1

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

--------------------------------------------------------------------------------

# 2 · Tools — four areas of use and their consequences

--{{0}}--
Tools are grouped by area of use. The four areas differ in the consequences of
an error for students.

> **Aspect 5.1 → 5.2 — Acquire to Deepen.** The transition consists in assessing
> tools by the obligations their use entails rather than by their functions.

| Area | Examples | Consequence |
| --- | --- | --- |
| **Administration** | minutes, agendas, translations, forms — no student is assessed | low |
| **Preparation** | slides, reading lists, task variants — reviewed before use | low |
| **In-class** | captioning, translation, polling — students are present | **Art. 5(1)(f)** adjacent |
| **Evaluation** | feedback, marking support, detection — output affects a student's record | **Annex III point 3 · GDPR Art. 22** |

Ordered by consequence, not by frequency. Most everyday use falls into the first
two areas; most legal requirements concern the last two.

## 2.1 · Tools and their limitations

### Administration

- **Institutional and national platforms.** SURF EduGenAI (Netherlands): a
  national pilot with open-source and commercial models, planned for general
  availability around the end of 2026 and not intended for assessment or fraud
  detection. GWDG Chat AI (Germany). Open WebUI and HAWKI: open-source front
  ends hosted by an institution. Advantage: contractual agreement and retention
  rules. Limitations: the available models change, and the service requires
  operation.
- **Licensed education editions.** Microsoft 365 Copilot Chat with enterprise
  data protection, Gemini for Education and NotebookLM in Google Workspace for
  Education, ChatGPT Edu, Claude for Education. Where contracted, training on
  institutional data is excluded. Limitations: providers are based outside the
  EU, so data residency determines the storage location but not every question
  of access; terms change faster than institutional review; dependence
  increases with use.
- **European and open models.** Mistral (France), Apertus (Switzerland; Apache
  2.0; more than a thousand languages) and EuroLLM (EU-funded; all 24 official
  EU languages). Their composition is documented. Limitations: open models
  perform below leading commercial models on demanding tasks and require
  hosting.
- **Local models via Ollama or LM Studio**, as used by llmlab. No data leaves
  the computer. Limitations: smaller models perform worse on long documents and
  in languages other than English.

### Preparation

The teacher reviews all material before use, which keeps the risk low.
Generating several versions of a task is fast; selecting and checking them
takes the same time as before.

### In-class

Live captioning and translation improve accessibility; their quality decreases
with background noise, unfamiliar accents and technical vocabulary. They should
be announced as an aid and not used as a record.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>Prohibition</strong><br>Systems that infer emotions from faces, voices or posture in education are prohibited under Art. 5(1)(f) AI Act. Consent does not make a prohibited practice lawful.
</div>

### Evaluation

Drafting rubrics is low-risk: the teacher designs the instrument. Marking
support concerns decisions about persons; the questions are whether a person
with authority takes the decision and whether the student can contest it.

Krommer (2026) describes automated feedback as a choice between two problems.
Feedback general enough to be generated without risk is too general to change
students' work; feedback specific enough to change it has to be defensible in
every sentence, which requires reading the work. A defensible use consists in
drafting with a documented standing instruction (skill prompt, Block 3) and
reviewing the draft before release.

### Publicly available tools and their conditions of use

On a personal account there is no agreement concluded by the institution: no
data processing agreement, no administrative control over retention, no
notification of changed terms. Such use is suitable for preparation with public
material and unsuitable for student work, personal data, unpublished research
and anything that contributes to a grade.

| Tool | Typical use | Limitations |
| --- | --- | --- |
| **NotebookLM** (Google; also Gemini Notebook) | answers based on uploaded sources, with citations; study guides; audio and video overviews | A citation does not verify a statement. Audio overviews add emphasis not contained in the sources. Under an institutional Workspace for Education account: core service without human review or training; not on personal accounts. No student work, no third-party copyrighted material. |
| **Free tiers** of ChatGPT, Gemini, Claude, Copilot, Le Chat | drafting, explaining, rephrasing | Conversations may be used for training unless disabled; settings differ and change. The most capable versions require payment. |
| **Perplexity** and other AI search | web answers with links | A link does not establish that the source supports the sentence. |
| **Elicit, Consensus, Scite** | finding and summarising literature | Incomplete coverage favouring open-access literature in English; summaries omit disagreement. |
| **Image and slide generators** (Canva, Gamma and others) | visual material | Unresolved copyright status for OER; Art. 50 requires disclosure where generated content is presented to students. |

Each row can be assessed with the questions of the tool triage page: *Where is
the text processed? Who has agreed to what? What happens if the output is wrong?*

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

## 2.2 · Legal framework

--{{0}}--
Five provisions and one amended date.

- **Art. 4 AI Act — AI literacy.** The deploying organisation, for teaching
  purposes the institution, takes measures to ensure sufficient AI literacy of
  its staff. Applicable since February 2025; not deferred.
- **Art. 5(1)(f) AI Act — prohibited practice.** Inferring the emotions of a
  person in the workplace or in education, except for medical or safety
  reasons. Applicable since February 2025.
- **Art. 50 AI Act — transparency.** Persons must be informed when they interact
  with an AI system or receive certain artificially generated content.
  Applicable since 2 August 2026.
- **Art. 14 AI Act — human oversight.** Applies to high-risk systems. Oversight
  must be exercised by persons who understand the system and can override its
  output.
- **Annex III point 3 AI Act — education.** Admission and assignment,
  evaluation of learning outcomes, assessment of the appropriate level of
  education, and monitoring of prohibited behaviour during tests.

**Amended date.** Regulation (EU) 2026/1744 (Digital Omnibus on AI), published
on 24 July 2026 and in force since 27 July 2026, defers the obligations for
standalone Annex III high-risk systems from 2 August 2026 to **2 December
2027**, and for Annex I embedded systems to 2 August 2028. The stated reason is
the delayed availability of harmonised standards. **Articles 4, 5 and 50 were
not deferred.** The content of the high-risk obligations is unchanged; only the
date of application has moved.

### GDPR Art. 22

A data subject has the right not to be subject to a decision based solely on
automated processing which produces legal effects or similarly significantly
affects them. A grade is a typical example. Human involvement must be
meaningful: the person involved needs the authority and the information to
reach a different decision.

### Tool triage and decision record

The page records the assessment of one tool. The area of use determines the
legal questions: for evaluation, Annex III point 3, GDPR Art. 22 and Art. 14
must be answered before the record can be exported; emotion inference in class
leads to the result *decline*.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p2_tool_triage.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the tool triage page in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p2_tool_triage.html).

## 2.3 · AI detectors

--{{0}}--
The principal objection concerns not accuracy but the impossibility of disproof
and the unequal distribution of errors.

**Asymmetric consequences.** A false negative results in a grade that should
have been lower. A false positive can result in disciplinary proceedings and,
for some international students, consequences for residence status. The
instrument has to be assessed against this asymmetry rather than an average
error rate.

**No possibility of disproof.** Version histories and drafts support a student's
account but can be produced retrospectively. A procedure in which the accused
person cannot refute the accusation does not meet the requirements of a fair
academic-integrity procedure (Bassett et al., 2026).

**Unequal distribution of errors.** Detector scores respond to short clauses,
conventional collocations and low lexical variability — also features of
competent academic writing in a second or third language. False positives
therefore occur more frequently among students writing in a language other
than their first.

## 2.4 · Equity and copyright

**Equity.** The most capable general models are currently available in paid
versions. If a task can be completed better with a subscription, the assessment
partly measures access to paid tools. A tool that the institution does not
provide cannot be made a condition of assessment.

**Copyright in students' work.** Copyright in examination scripts, term papers
and theses belongs to the student. Uploading such work to a commercial
assistant is a use of a protected work by the teacher. This question is
separate from data protection and is **not** resolved by anonymisation, because
the protected object is the work itself.

> **Consequence:** student work is processed only with the institutional or a
> local system. Any intended use of an external service is stated in the module
> handbook before submission.

## 2.5 · Resource consumption

--{{0}}--
Every inference consumes energy, water and hardware capacity.

The framework in Appendix A contains a competence on comparing the resource
consumption of AI systems; this course reaches only its Foundation level.

Measures available at module level:

- use the smallest model that meets the requirements of the task;
- process inputs in batches instead of repeating requests;
- avoid calls to hosted models in teaching materials opened by every student of a cohort where a stored answer would suffice.

Lab 7 reports the processing route, which determines where the consumption occurs.

## 2.6 · Agents and online tests

AI agents can open course pages and PDF files, answer questions and submit
forms. Unsupervised online tests therefore no longer establish that the
enrolled student answered the questions. Detection and extended honour codes
do not address the problem; formats in which the working process itself is the
evidence do. Their design is beyond the scope of this course.

## 2.7 · Resources for departments

**Typology of didactic chatbots (ZML, KIT).** Classifies chatbots by didactic
function — tutor, sparring partner, simulated interlocutor, answering service
for module questions. Each type has specific failure modes and transparency
obligations under Art. 50.

**Faculty-level policy.** The policy of UC Berkeley School of Law (effective
Summer 2026) is an example of a regulation written for a single faculty and its
assessment types.

**Open courses and support structures.** Students: Elements of AI (University of
Helsinki), DigiStudi (iMooX). Staff: the UNESCO frameworks, AI GO! (Npuls), the
twillo OER materials (German). National and regional bodies: SURF and Npuls
(Netherlands), Jisc National Centre for AI (United Kingdom),
KI:Expertisezentrum.nrw (North Rhine-Westphalia).

## 2.8 · Quick check — Block 2

A supplier offers a lecture-hall system that identifies students who appear disengaged. Which response is correct?

    [( )] Carry out a data protection impact assessment and proceed if it is positive.
    [( )] Use it only with explicit consent of the students.
    [(X)] Decline: inferring emotions in education is prohibited under Art. 5(1)(f), and consent does not make a prohibited practice lawful.
    [( )] Wait until December 2027, when the high-risk obligations apply.
    *******************************************************************
    Article 5 lists prohibited practices. The deferral to December 2027
    concerns Annex III high-risk obligations, not the prohibitions, which
    have applied since February 2025.
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

--------------------------------------------------------------------------------

# 3 · Strategies — terminology and the five stages of prompting

--{{0}}--
Six technical terms, each with a direct consequence for decisions in teaching,
and five stages of prompting applied to one example.

> **Aspect 5.2 — Deepen.** Autonomous upskilling and peer coaching.

## 3.1 · Six terms and their consequences

| Term | Definition | Error if not taken into account |
| --- | --- | --- |
| **Token** | the unit a model processes: a word, part of a word or a punctuation mark from a fixed vocabulary | Text volume is estimated in pages. The same sentence requires more tokens in German or Polish than in English, which affects cost, processing time and usable context. |
| **Context window** | the maximum number of tokens processed in one request, including instructions, documents and answer | A 90-page thesis is summarised and the summary is taken to cover the whole document. Text beyond the window is removed before processing, without notice. |
| **Training vs inference** | model parameters are fixed during use; a conversation does not change them | Corrections in a chat are assumed to be learned and are repeated instead of being written into a standing instruction. Where a system appears to remember, it reads stored text back into the prompt (memory, or a wiki at stage 5). |
| **Grounding** | whether the answer was generated with the relevant source text in the prompt | A fluent answer is treated as a look-up. Only comparison with the source shows whether a source was used. |
| **Temperature and seed** | temperature determines how the next token is sampled; the seed makes sampling repeatable | Two identical scripts receive different comments, and neither can be reproduced when a grade is contested. |
| **Deployment route** | where the text is processed | A local route is taken to settle all legal questions; Annex III, Art. 50 and Art. 4 still apply. |

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

**Lab 3 · Temperature and seed.**

- *Background:* at temperature 0 the most probable token is always selected; at
  higher temperatures sampling introduces variation. A fixed seed makes
  sampling repeatable.
- *Materials:* a request for one sentence of feedback on a student paragraph
  arguing that formative assessment should replace final examinations.
- *Procedure:* four requests at temperature 0 with seed 42; four at temperature
  0.8 without seed.
- *Measured:* number of character-identical outputs per group.

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

The stages do not indicate output quality: an answer at stage 1 can be as good
as one at stage 5.

### Example: replies to student emails

The module team of a fictitious module, *EDU-204 Research Methods in
Education*, receives emails from students. Most concern dates, rooms or
materials and can be answered from the module information. Extensions and grade
changes are decided by the examination office. Requests concerning other
students must not be answered. The example involves many similar inputs, a
reference document, rules whose violation has consequences, and cases that must
be decided by a person, and is therefore suitable for all five stages.

| Email | Content | Expected handling |
| --- | --- | --- |
| 01 | date and room of the written exam, registration | answer from module information |
| 02 | extension request due to illness | refer to examination office, no promise |
| 03 | availability of slides before the session | not in module information → open question |
| 04 | reading list and office hours (German) | answer in German |
| 05 | request to raise an exam grade | refer to review session and examination office |
| 06 | exam registration of a flatmate | no information; reviewed by a person |
| 07 | sample size of a portfolio study | reviewed by a person |

**Stage 1 — Prompt.** Email 02 is pasted with the request *"Answer this
email:"*, without instruction or module information. The model has no
information on who decides extensions and no dates; replies frequently promise
the extension or state dates not contained in any source. Corrections made in
the conversation are not retained for the next email.

**Stage 2 — Skill prompt.** The system prompt contains the specification and the
module information. The specification has ten rules: use only the sources;
write a fixed sentence for open questions; no decisions on extensions or grades;
no information about other students; no identifiers; reply in the language of
the email; salutation and signature; at most 150 words; answer the question
asked; copy names of courses, folders and rooms exactly. The instruction is
written once, can be reviewed by colleagues and is reused, for example as a
custom instruction or a `SKILL.md` file (open standard since December 2025).
For most teaching staff this stage has the most immediate practical use. Replies
are not checked systematically.

**Stage 3 — Harness.** For each email in a folder, a program:

1. sends a classification request that assigns one of five categories
   (*information, extension, grade, third_party, other*);
2. sends a drafting request with the handling rule for that category and the
   system prompt from stage 2;
3. writes the reply to a file with a header recording input, category, route,
   model, settings and time;
4. places the file in `ready/` or `review/`; routing depends on the category
   only, and *third_party* and *other* always go to a person.

A harness is justified when the same procedure is applied to many inputs and
has to be documented. Because replies are not checked, a reply in an automatic
category can be placed in `ready/` although it violates a rule.

**Stage 4 — Loop.** Nine automatic checks test each draft:

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
concerned. The loop stops when all checks pass, when the reply contains the
sentence for open questions, or after the maximum number of rounds. A reply is
placed in `ready/` only if all checks pass, the category is automatic and no
open question remains. The checks are text patterns: a reply can pass them and
still be wrong, and a correct reply can fail them. Each round is an additional
inference.

**Stage 5 — Wiki.** `wiki.md` has three sections:

- *Lessons from failed checks* — written by the program; one line per rule that
  first drafts violated, added to the instructions of later runs.
- *Open questions* — written by the program; emails the sources could not
  answer (email 03 in the example).
- *Approved answers* — written only by people, e.g. "The slides for each session
  are uploaded to the learning platform by 18:00 on the day before the session."
  Later runs use these entries as a source.

In the next run email 03 is answered from the approved answer and, if all checks
pass, placed in `ready/`. The process thus handles a growing share of emails
without intervention, while decisions remain with the examination office and
sensitive categories with a person. The model does not change; the file does.
Whoever can edit the wiki influences every later reply, errors in it are
repeated, and personal data must not be entered. Karpathy's *LLM wiki* (2026)
describes this pattern; memory functions of commercial assistants follow the
same principle without making the stored text visible.

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

**Lab 6 · Five stages.**

- *Materials:* task folder `llmlab/tasks/student_emails` — `spec.md`,
  `context/module_information.md`, `task.json` (categories and handling rules),
  `inputs/` (seven emails), `example_approved_answer.md`.
- *Procedure:* stages 1 and 2 on email 02; stages 3 to 5 on the first four
  emails (parameter `emails`) with up to three rounds (parameter `rounds`). At
  stage 5 the lab inserts the approved answer on slides in place of a decision
  by the module team.
- *Output:* every classification, drafting and revision prompt; checks per
  round; routing; the wiki as written and as read.

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

## 3.3 · Example of a specified teaching artefact

**Circular construction safety and material twin.** A browser-based simulation
for vocational construction education. It combines live regional weather data, a
fault developing across eight sensor channels, three consultations with
different roles and six material passports that learners route to reuse,
repair, recycling or quarantine, with retained mass, avoided carbon emissions
and avoided replacement costs shown against a circularity score. The learner's
output is a diagnosis, an action and a **written justification**. The
application runs on a static web host without server component or API key.

### Three design decisions with pedagogical rationale

1. **Architecture and data protection.** No login, no accounts and no
   server-side storage: learners' decisions remain in the browser, so no
   personal data is collected.
2. **Labelling of data provenance.** Weather values are labelled as live
   external data; concrete, strain, crane-tilt, dust and electrical channels as
   virtual until physical sensors are connected; impact figures as educational
   estimates.
3. **Output as a decision record.** Diagnosis, action and written justification
   form a timestamped process artefact suitable for assessment.

<div style="border:1px solid #8a3324;border-left:5px solid #8a3324;border-radius:0 10px 10px 0;background:#fbe9e6;padding:12px 16px;margin:16px 0;color:#6d2a1e;">
<strong>Purpose and maintenance</strong><br>Before a further artefact of this kind is developed, three questions should be answered in writing: which teaching problem it solves that a seminar does not; what it replaces rather than adds; and who maintains it when the person who specified it is unavailable. An artefact that is not maintained cannot be used as an open educational resource in the long term.
</div>

**Transfer to other disciplines.** Select a situation that students cannot
practise because the real setting is dangerous, slow, expensive or rare;
specify it as a system with explicit constraints; develop it in small versioned
steps; label real and simulated data; make a justification rather than a score
the learner's output.

## 3.4 · Three positions from the literature

**AI as an instrument of reflection.** Instead of asking a system to improve a
draft, the instruction asks it to examine the draft: state the claim of a
paragraph, list the conditions under which the claim holds, and identify which
conditions the text does not establish. The student remains the author. As a
stored instruction this is a stage-2 artefact.

**Academic writing as a process of thinking.** Wampfler (2026) argues that the
debate rests on the assumption that academic writing transcribes finished
thought. If writing is instead the process in which thought is formed, the
relevant question is which parts of this process students must carry out
themselves. This question can be answered for a specific module, and the answer
determines the assessment design.

**AI-generated companion material.** A German-language book on higher education
in the age of generative AI is accompanied by entirely AI-generated slides and
podcasts. A note circulated in the OvGU working group observes that this material
shows the typical weaknesses of such material and that concrete recommendations
are rare. Two criteria follow for evaluating any material, including this
course: whether it states what to do in practice, and whether generated parts
are identifiable.

## 3.5 · Quick check — Block 3

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

> **Aspect 5.2 → 5.3 — Deepen to Create.**

## 4.1 · Three questions

**Question 1 — Which task remains without AI support, and why?**
Name one task that continues to be carried out without AI support because the
judgement it requires is needed to evaluate AI output in other tasks. State the
reason in writing.

The Wissenschaftsrat uses the term **intellectual sovereignty** for this
capacity. Combined with Ferdman's concept of capacity-hostile environments, the
task has to be anchored in the module design, a deadline or a review step, where
it is visible to others.

**Question 2 — Which past decision would now be taken differently?**
One decision from the last twelve months. Name the legal provision or the
principle that changes the assessment.

**Question 3 — Who else should be informed?**
Name one person and one piece of information. In Aspect 5, peer coaching is the
activity named for the Deepen level.

## 4.2 · Levels covered

| Aspect 5 level | Covered by the course | Not covered |
| --- | --- | --- |
| **Acquire** (5.1) | Rights and obligations with legal references; readiness self-assessment; human-directed use examined on a local model (`python -m llmlab all`). | Complete if the [self-check](pages/p1_self_check.html) was carried out. |
| **Deepen** (5.2) | Begun in two places: the tool decision record and the stage-2 skill prompt. | No peer coaching; no use of data on one's own practice. |
| **Create** (5.3) | Described with one example and planned over ninety days. | **Not attempted.** Requires a community, a review cycle and a published artefact. |

### 90-day plan

The last line of the self-check is pasted into the page; the two largest gaps
become the two development areas, and no third area can be added. Each area
receives two dated tasks at the target level; the plan can be exported as a
calendar file.

<iframe src="https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p3_cpd_plan.html" width="100%" height="640"
 style="border:1px solid #ddd;border-radius:8px"></iframe>

If the page does not load, [open the plan page in a separate tab](https://ovgu-vet-teched.github.io/Masterclass_EU_Green_Tegelbeckers/V6/pages/p3_cpd_plan.html).

To describe the plan in the vocabulary of a competence framework, select the most
frequent own practice in the placement map below and add the two identifiers
from the column *needed first* to the plan. The identifiers come from an
unpublished draft and serve as labels only.

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

--------------------------------------------------------------------------------

# 5 · Plan and summary

--{{0}}--
The plan is limited to two development areas.

Plans with many areas are frequently discontinued within a few weeks, which is
then attributed to the person rather than to the scope of the plan.

**Four options for further work:**

1. **Adapt the session** for a department. All material is CC BY 4.0; tool
   examples can be replaced, the legal panel remains valid. About one afternoon
   of adaptation, 90 minutes of delivery.
2. **Mentor one colleague.** One person, four meetings over a term.
3. **Publish one artefact** — a task specification, rubric, decision record,
   skill prompt or small simulation — with version history and licence.
4. **Establish a practice group** of at least three people with regular
   meetings. The result is a documented set of decisions with dates and reasons.

### Written commitment

> *By [date], I will [specific action] so that [named colleague or group] can
> [outcome].*

A commitment without a date cannot be reviewed; a commitment without another
person does not correspond to the collaborative activities described in Aspect 5.

## Summary

- Models process tokens, and the context window limits the text processed in one request; text beyond it is removed without notice.
- The wording of an answer does not show whether it is based on a source; only comparison with the source does.
- The deployment route determines data-protection obligations; obligations under the AI Act apply regardless of the route.
- Art. 5(1)(f) is a prohibition and cannot be satisfied by an impact assessment or consent.
- The five stages of prompting differ in what is retained, which steps are automated and which artefacts require review; automatic checks approximate rules and do not establish correctness.
- Tools, strategies and reflection build on one another.

--------------------------------------------------------------------------------

# Appendix A — The placement map

--{{0}}--
Relation between common teaching practices and competences.

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

## A.2 · The router — common practices

--{{0}}--
Twelve practices from this course. Each entry lists the competences exercised
and the competences needed first. Nothing is stored or scored.

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
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> The route does not establish compliance. Annex III §3, Art. 50 and Art. 4 apply regardless of the processing location.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E3</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Evaluate whether AI outputs should be accepted, revised, or rejected.</strong> Smaller models are measurably weaker on long documents and on languages other than English, so verification effort goes up, not down.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Removes the processor relationship and the transfer. Removes nothing else.<br><strong>In this course:</strong> Block 2 · Lab 7 (`route`) · Block 3 terminology table, deployment route.<br><strong>Read:</strong> llmlab — seven exercises on language models, run on a local model · [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)</p>
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
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> None new. The instruction is what makes your human oversight demonstrable under Art. 14 if it ever matters.<br><strong>In this course:</strong> Block 3 — stage two · Lab 4 (`steer`).<br><strong>Read:</strong> llmlab — seven exercises on language models, run on a local model · [KI als Reflexionsinstrument im wissenschaftlichen Arbeiten](https://zhq-blog.fh-aachen.de/kompetenzen-studierende/ki-als-reflexionsinstrument-im-wissenschaftlichen-arbeiten/)</p>
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
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> The provenance header is the practical form of Art. 14 oversight and of an appeal-proof position.<br><strong>In this course:</strong> Block 3 — stage 3 · Lab 6 (`ladder`) and the `harness` command (email task).<br><strong>Read:</strong> llmlab — seven exercises on language models, run on a local model · Workshop 4 — AI in Teaching: Tools, Strategies and Reflection</p>
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
<td style="border:0;width:50%;padding:0 0 0 10px;"><h5 style="margin:0 0 6px;font-size:0.78em;text-transform:uppercase;color:#a86a12;">You needed these first</h5><ul style="list-style:none;padding:0;margin:0;"><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-S4</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Improve AI use and AI systems to promote well-being and societal benefit.</strong> Maintenance. An unmaintained repository cannot serve as an OER.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-X1</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Applied</span><br><strong>Apply the legal framework for AI in higher education.</strong> It becomes the Annex III situation the moment the score attaches to a grade.</li><li style="margin-bottom:8px;padding-left:10px;border-left:3px solid #a86a12;"><code style="font-size:0.8em;color:#1a4a88;">HET-E5</code> <span style="background:#f1ebf9;color:#4b3573;border-radius:4px;padding:0 5px;font-size:0.7em;font-weight:700;">Foundation</span><br><strong>Compare how AI systems consume energy and natural resources.</strong> If it calls a hosted model at runtime, that cost is now in your teaching, every cohort, every year.</li></ul></td>
</tr></table>
<p style="margin:12px 0 0;border-top:1px dashed #d6dee8;padding-top:9px;font-size:0.9em;"><strong>Legal floor:</strong> Art. 50 for what the learner is told. Annex III §3 as soon as it is graded.<br><strong>In this course:</strong> Block 3.4 — the worked example and the three pedagogical decisions.<br><strong>Read:</strong> Workshop 4 — AI in Teaching: Tools, Strategies and Reflection · [Perspektiven einer KI-unterstützten offenen Bildungspraxis](https://his-he.de/publikation/perspektiven-einer-ki-unterstuetzten-offenen-bildungspraxis/)</p>
</div>
</details>


## A.3 · Coverage of the course, by competence

The table also lists the competences the course does not reach.

| Competence | Level reached | Where | What is still missing |
| --- | --- | --- | --- |
| `HET-E1` **Recognise AI's role and influence in academic contexts** | Foundation | Block 0 diagram; Block 2 four-family map; ASSET module 01 | Institution-wide mapping (Advanced) is not attempted. |
| `HET-E2` **Describe how AI systems perform tasks in accurate, non-anthropomorphic language** | Applied | Block 3 terminology table (six terms); Labs 1–3; ASSET module 02 | The most extensive coverage in the session. |
| `HET-E3` **Evaluate whether AI outputs should be accepted, revised, or rejected** | Applied | Block 1 failure modes; Lab 5 `ground`; Block 3 grounding row | Covered as a judgement; a written verification procedure is not developed. |
| `HET-E4` **Examine how predictive AI recommendations can inform or limit perspectives** | Foundation | Block 1 — confirmation and anchoring; Block 3 — context window | Recommender pre-selection is named rather than examined. |
| `HET-E5` **Compare how AI systems consume energy and natural resources** | Foundation | Block 2 — the resource panel; Lab 7 route report | Covered at Foundation level only, which is limited in the EU GREEN context. |
| `HET-E6` **Explain how AI can amplify societal biases and concentrate epistemic authority** | Applied | Block 1 homogenisation and illusion of consensus; Block 2 detectors, uneven errors | Bias is treated through one worked case (detectors) rather than systematically. |
| `HET-E7` **Analyse how well AI use aligns with ethical principles and human values** | Applied | Block 2 equity and copyright panels; Block 4 reflection questions | Ethics is treated through cases rather than a list of principles. |
| `HET-C1` **Use AI to explore perspectives that build upon original academic ideas** | Foundation | Block 2 preparation family; Block 3 stages one and two | — |
| `HET-C2` **Visualise, prototype and combine ideas using different types of AI systems** | Foundation | Block 2 preparation family; Block 3.4 worked example (Advanced, demonstrated not practised) | Demonstrated, not practised. |
| `HET-C3` **Direct and iterate with generative AI systems (prompting as a documented practice)** | Applied | Block 3 — the five stages; Labs 4 and 6; the harness command with `--loop` and `--wiki` | Central competence of Block 3. |
| `HET-C4` **Analyse how AI can safeguard or violate authenticity, authorship and intellectual property** | Foundation | Block 2 copyright panel; Block 3 provenance disclosure | Institutional disclosure rules vary; the session gives the question, not your answer. |
| `HET-M1` **Decide whether to use AI based on the nature of the academic task, including reasoned non-use** | Applied | Block 2 four families ordered by consequence; Block 4 question one | Reasoned non-use is defined as a competence. |
| `HET-M2` **Choose an appropriate AI approach by comparing how different systems operate** | Foundation | Block 2 tool cards; Lab 7 `route` | — |
| `HET-M3` **Decompose a task to determine where AI should automate and where it should only augment** | Applied | Block 3 stage two; Block 4 — what will you keep doing by hand | Directly reinforced by Ferdman's capacity-hostile environments. |
| `HET-M4` **Monitor and evaluate AI use throughout an academic process** | Foundation | Block 1 automation complacency; Block 3 provenance headers | Checkpoints across a term are described, not practised. |
| `HET-S1` **Investigate how an AI system is intended to work, whom it is designed for, and what its limits are** | Foundation | Block 2 tool cards, each with its stated fault | — |
| `HET-S2` **Evaluate AI systems using defined outcomes, test cases and user feedback** | Applied | The whole lab: seven claims put to a system on your own machine | The lab exercises correspond to this competence. |
| `HET-S3` **Design AI use attentive to data sources, data selection and information flow** | Applied | Block 2 deployment routes; Block 3 route row | — |
| `HET-S4` **Improve AI use and AI systems to promote well-being and societal benefit** | not reached | Named in Block 5 (publish one artefact); not reached | Requires other people and a review cycle over a longer period. |
| `HET-X1` **Apply the legal framework for AI in higher education** | Applied | Block 2 legal panel; GDPR Art. 22 panel; copyright panel; closing quiz | The most extensively covered competence of Stratum X. |
| `HET-X2` **Practise scholarly work with AI** | Foundation | Block 3.4 provenance and licensing; Block 1 fabrication | Scholarly writing with AI, and doctoral supervision, each need a session of their own. |
| `HET-X3` **Develop professionally and collaboratively with AI** | Applied | Block 4 question three; Block 5 mentor one colleague; the 90-day plan | Begun, not completed, in line with the Deepen level. |

### Competences the course does not reach

- **`HET-S4` — improving systems and use for well-being and societal benefit.**
  Requires a community and a review cycle over a longer period.
- **`HET-E5` — comparing energy and resource consumption.** Foundation level
  only, which is limited in the EU GREEN context.
- **`HET-C2` at Advanced — prototyping.** Demonstrated in 3.3, not practised.
- **`HET-X2` — scholarly work with AI** beyond provenance and licensing.
  Doctoral supervision and publication ethics require a separate session.

## A.4 · Self-study route

Five open LiaScript modules written for teachers in vocational education cover
the Foundation level of most of the Engage domain and part of Create, in about
four hours:

- **AI Orientation** — lifelong professional learning (`E1`, `X3`)
- **AI Basics** — non-anthropomorphic description and human agency (`E2`, `E3`, `M4`)
- **AI Tools** — system types, data origin, OER (`M2`, `S1`, `S3`)
- **Prompting** — `C3` at Foundation, and the structure of a standing instruction
- **Quality and Ethics** — `E6`, `E7`, and the human-rights framing

The modules were written under the UNESCO-UNEVOC ASSET co-initiative, and their
examples are taken from electronics. Blocks 2 and 3 of this course cover content
that the modules do not address.

## A.5 · Check yourself — the placement map

You run every model locally. Which claim does the framework support?

    [( )] You have satisfied the legal floor, since no data leaves the institution.
    [(X)] You are Applied on the data-flow competence and unchanged on the legal one.
    [( )] You have reached Advanced on all four Shape competences.
    [( )] Local hosting is outside the framework, since it is an infrastructure choice.
    *******************************************************************
    The route determines whether data is transferred. Annex III §3,
    Art. 50 and Art. 4 apply regardless of the processing location, which
    is why the router lists the legal competence under "needed first" for
    this practice.
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
All sources cited in this course, grouped by subject.

A large part of the sources added since version 4 comes from the reading list
of the OvGU working group on AI and digitality in study and teaching.

Three central sources: Ferdman (2026) on deskilling as a structural problem;
the recommendations of the Wissenschaftsrat (2026) for the German context;
Chandra et al. (2026) on the persistence of sycophancy effects despite warnings.

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
1. OvGU Zentrum für Lehrer*innenbildung, working group (2026). *HETAICF v0.11 — Higher Education Teaching AI Competence Framework.* **Unpublished draft, in review. Numbering will change. Do not cite competence identifiers as authority.** Used in this session as a mechanism for local adaptation, not as a source.
1. AK Digitalisierung im Lehramt, OvGU (2026). *DACT v1.0 — Digital and AI Competency Framework for University Teacher Trainers.* Local framework for the teacher-trainer role; one of the source frameworks crosswalked in HETAICF.

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
1. UNESCO-UNEVOC / ASSET Co-initiative, OvGU (2026). *Self-learning nuggets: AI Orientation, AI Basics, AI Tools, Prompting, Quality and Ethics.* Five LiaScript modules written for TVET teachers, mapped in Appendix A as the self-study route into the Foundation level.


--------------------------------------------------------------------------------

# Licence and provenance

**AI in Teaching: Tools, Strategies and Reflection**, version 6, September 2026.
EduGreenLabs / OvGU Magdeburg — WP2 Training Lab, EU GREEN Alliance.

Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Funded by the
European Union. Views expressed are those of the authors alone.

The UNESCO AI Competency Framework for Teachers is licensed CC BY-SA; this course
paraphrases and attributes it rather than reproducing its wording, because this
course is licensed CC BY.

The framework used for the structure of Appendix A is an unpublished draft under
review and **should not be cited**.

**Changes from version 5:** academic register throughout; facilitator notes
removed; each lab description states aim, background, materials and procedure;
the five stages of prompting are described with one continuous example (replies
to student emails) that matches llmlab 2.0.

**Companion files:** `masterclass_ai_in_teaching_v6.html` (live version) ·
`llmlab/` (the seven lab exercises) · `pages/` (self-check, tool triage, plan) ·
`REFERENCES.md` (bibliography).
