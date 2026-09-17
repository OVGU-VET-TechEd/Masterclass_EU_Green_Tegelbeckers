"""Seven exercises on the behaviour of language models.

Every lab returns the same structure:

    {"lab", "title", "aim", "background": [..], "procedure": [..],
     "materials": [{"label", "text"}], "runs": [..], "reading", "block"}

`aim`, `background` and `procedure` describe the exercise. `materials` holds
the texts the exercise sends to the model. Each entry in `runs` records the
system prompt and the user message exactly as sent, the settings, and the
output. `reading` states what the measured figures show; it is composed from
the figures, so it also reports when a run does not show the expected effect.
"""

from __future__ import annotations

import copy
import json
from typing import Any, Callable, Dict, List, Optional

from . import tasks
from .backend import Backend, approx_tokens
from .checks import EMAIL_RULES, FEEDBACK_RULES, all_passed, check_feedback, passed, score

import re


def _run(label: str, result=None, prompt: Optional[str] = None, system: str = "",
         settings: Optional[Dict[str, Any]] = None, **extra) -> Dict[str, Any]:
    d: Dict[str, Any] = result.as_dict() if result is not None else {
        "text": "", "prompt_tokens": None, "output_tokens": None, "seconds": 0.0,
        "model": "", "endpoint": "", "simulated": False, "notes": []}
    d.update(label=label, prompt=prompt, system=system, settings=settings or {})
    d.update(extra)
    return d


def _plural(n: int, word: str) -> str:
    if n == 1:
        return "%d %s" % (n, word)
    return "%d %s" % (n, word[:-1] + "ies" if word.endswith("y") and word[-2:-1] not in "aeiou" else word + "s")


# ================================================================ 1 · tokens

TOKENS_PAIR = (
    "Assessment criteria are agreed at programme level.",
    "Bewertungskriterien werden auf Programmebene vereinbart.",
)

INFO_TOKENS = {
    "title": "Tokens: what the model receives",
    "aim": "To measure into how many tokens a text is divided, how this differs "
           "between an English and a German sentence of the same meaning, and how "
           "many tokens the chat template adds.",
    "background": [
        "Language models do not process words or characters but tokens. A tokenizer "
        "divides the input into units taken from a fixed vocabulary: frequent words "
        "are usually a single token, less frequent words are split into several "
        "subword units, and spaces and punctuation form part of tokens. The "
        "vocabulary is built from the training data. Languages that are less "
        "represented in that data are therefore divided, on average, into more "
        "tokens per word.",
        "Token counts have three practical consequences. The context window is "
        "measured in tokens. Hosted services charge per token. Processing time "
        "increases with the number of tokens.",
        "Chat models receive the user's text inside a template that marks the roles "
        "(system, user, assistant) with special tokens. Some models also insert a "
        "default system prompt. These tokens are not visible in a chat interface, "
        "but they occupy the context window.",
    ],
    "procedure": [
        "The text is sent to the model with output limited to one token. The server "
        "reports how many prompt tokens it processed, including the chat template.",
        "On the Ollama route, the same text is sent again in raw mode, which bypasses "
        "the chat template. The difference between the two counts is the template "
        "overhead.",
        "The segmentation shown on screen is a local approximation (words longer than "
        "five characters are split every four characters). It is not the model's "
        "tokenizer and is shown for comparison only.",
        "With the default text, the English and the German sentence are also counted "
        "separately.",
    ],
}


def _materials_tokens(p):
    if p["text"]:
        return [{"label": "Text sent to the model", "text": p["text"]}]
    return [{"label": "Text sent to the model (both sentences together)", "text": " ".join(TOKENS_PAIR)},
            {"label": "English sentence, counted separately", "text": TOKENS_PAIR[0]},
            {"label": "German sentence, counted separately", "text": TOKENS_PAIR[1]}]


def lab_tokens(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    default = not p["text"]
    text = p["text"] or " ".join(TOKENS_PAIR)
    r = backend.count_prompt_tokens(text)
    chips = approx_tokens(text)
    chars, counted = len(text), r.prompt_tokens
    lines = []
    runs = [_run("Text as counted by the model", r, text, settings={"max_tokens": 1}, chips=chips)]
    if counted:
        lines.append("The text has %d characters and was counted as %d tokens, i.e. "
                     "%.2f characters per token." % (chars, counted, chars / counted))
        off = abs(len(chips) - counted) / float(counted)
        lines.append("The on-screen approximation gives %d tokens, a deviation of %d%% "
                     "from the model's count." % (len(chips), round(100 * off)))
        if r.wrapper_tokens:
            lines.append("The model received %d tokens in total: %d for the text and %d "
                         "added by the chat template." % (counted + r.wrapper_tokens, counted,
                                                         r.wrapper_tokens))
    else:
        lines.append("The server returned no token count. The approximation gives %d "
                     "tokens for %d characters." % (len(chips), chars))
    if default and counted:
        en_r, de_r = (backend.count_prompt_tokens(s) for s in TOKENS_PAIR)
        en, de = en_r.prompt_tokens, de_r.prompt_tokens
        runs.append(_run("English sentence", en_r, TOKENS_PAIR[0], settings={"max_tokens": 1},
                         chips=approx_tokens(TOKENS_PAIR[0])))
        runs.append(_run("German sentence", de_r, TOKENS_PAIR[1], settings={"max_tokens": 1},
                         chips=approx_tokens(TOKENS_PAIR[1])))
        if en and de:
            words_en, words_de = len(TOKENS_PAIR[0].split()), len(TOKENS_PAIR[1].split())
            lines.append(
                "Counted separately, the English sentence (%d words) took %d tokens and "
                "the German sentence (%d words) took %d tokens%s." % (
                    words_en, en, words_de, de,
                    ", %.0f%% more" % (100.0 * (de - en) / en) if de > en else
                    "; on this tokenizer the German sentence is not longer"))
    return {"runs": runs, "reading": " ".join(lines)}


# =============================================================== 2 · context

CONTEXT_TITLE = "Examination regulations, module EDU-204 (fictitious excerpt)"
CONTEXT_FACT = (
    "§ 1 Submission\n"
    "The portfolio must be submitted via the learning platform by 12:00 on "
    "15 January 2027. Late submissions are graded as failed unless the examination "
    "office has granted an extension."
)
CONTEXT_SECTIONS = [
    ("Attendance", "Attendance at seminars is expected but not recorded. Students who "
     "miss more than three sessions should contact the module team to discuss how to "
     "cover the material."),
    ("Academic integrity", "Submitted work must be the student's own. Sources, including "
     "generative AI tools, are acknowledged according to the faculty's citation "
     "guidelines. Suspected breaches are referred to the examination board."),
    ("Language", "Coursework may be written in English or German. The language chosen "
     "for the portfolio is used consistently throughout."),
    ("Format", "The portfolio is a single PDF file. Pages are numbered, and the title "
     "page states the module code and the student's name."),
    ("Feedback", "Written feedback on formative tasks is provided within three weeks. "
     "Feedback on the portfolio is released together with the final grade."),
    ("Accessibility", "Students with a disability or chronic illness may apply for "
     "compensation for disadvantages. Applications are handled confidentially by the "
     "examination office."),
]
CONTEXT_QUESTION = (
    "Question: According to the regulations above, by which date must the portfolio "
    "be submitted? Answer with the date only."
)

INFO_CONTEXT = {
    "title": "Context window: text beyond the limit",
    "aim": "To test whether a model can answer a question when the passage that "
           "contains the answer lies outside its context window, and whether the "
           "answer indicates that information is missing.",
    "background": [
        "The context window is the maximum number of tokens a model processes in one "
        "request. It includes the system prompt, any supplied documents, the question "
        "and the answer being generated. Text beyond this limit is not processed.",
        "When a request exceeds the window, the serving software shortens the input "
        "before the model receives it. Ollama, the default route of this tool, keeps "
        "the end of the prompt and removes the beginning. The model receives no "
        "information that text was removed and therefore cannot report it; it answers "
        "from the remaining text.",
        "In Ollama the window is a per-request setting (num_ctx). The server default "
        "depends on the Ollama version and the available memory. Chat products do not "
        "usually display the window size. A request to summarise a document longer "
        "than the window produces a summary of the part that was retained.",
    ],
    "procedure": [
        "A document is assembled from fictitious examination regulations. § 1 states "
        "the portfolio submission deadline. The following sections (number set by the "
        "parameter 'sections') contain regulation text without any date.",
        "The question is placed after the document, so it lies at the end of the prompt.",
        "The identical prompt is sent twice at temperature 0 and seed 7: once with a "
        "window of 8,192 tokens and once with a narrow window (parameter 'num_ctx').",
        "An answer is counted as correct if it contains the date stated in § 1 "
        "(15 January). The answer from the narrow window is also searched for "
        "phrases indicating missing information, such as 'not found' or 'cannot'.",
    ],
}


def context_document(sections: int) -> str:
    parts = [CONTEXT_TITLE, CONTEXT_FACT]
    for i in range(int(sections)):
        title, text = CONTEXT_SECTIONS[i % len(CONTEXT_SECTIONS)]
        parts.append("§ %d %s\n%s" % (i + 2, title, text))
    return "\n\n".join(parts)


def _materials_context(p):
    doc = context_document(p["sections"])
    n = int(p["sections"])
    shown = "\n\n".join([CONTEXT_TITLE, CONTEXT_FACT] + [
        "§ %d %s\n%s" % (i + 2, t, x) for i, (t, x) in enumerate(CONTEXT_SECTIONS[:min(n, 2)])])
    if n > 2:
        shown += ("\n\n[§ 4 to § %d: the six regulation sections Attendance, Academic "
                  "integrity, Language, Format, Feedback and Accessibility, repeated in "
                  "turn]" % (n + 1))
    return [
        {"label": "Document (%d sections, approx. %d tokens by the local approximation)"
                  % (n + 1, len(approx_tokens(doc))), "text": shown},
        {"label": "Question, appended after the document", "text": CONTEXT_QUESTION},
    ]


_ADMITS = re.compile(
    r"\b(not (found|present|included|provided|visible|available|mentioned|given|stated)"
    r"|not specified|cannot|can't|unable|no (date|deadline|information)|missing|does not (appear|contain|mention|say|state|specify|include|provide))\b",
    re.I,
)


def _has_date(text: str) -> bool:
    t = text.lower()
    return ("15 january" in t or "january 15" in t or "15.01" in t or "15. januar" in t)


def lab_context(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    num_ctx = int(p["num_ctx"])
    prompt = context_document(p["sections"]) + "\n\n" + CONTEXT_QUESTION
    wide = backend.generate(prompt, temperature=0.0, seed=7, num_ctx=8192, max_tokens=20)
    narrow = backend.generate(prompt, temperature=0.0, seed=7, num_ctx=num_ctx, max_tokens=20)
    hit_wide, hit_narrow = _has_date(wide.text), _has_date(narrow.text)
    size = wide.prompt_tokens
    reading = ("The prompt comprised %s. With a window of 8,192 tokens the answer was %s "
               "(%r). With a window of %d tokens the answer was %s (%r)." % (
                   "%d tokens as reported by the server" % size if size else "an unknown number of tokens",
                   "correct" if hit_wide else "incorrect", wide.text[:60],
                   num_ctx, "correct" if hit_narrow else "incorrect", narrow.text[:60]))
    if hit_narrow:
        reading += (" The narrow run found the date, so this run does not show the effect. "
                    "Possible reasons: the server does not truncate at this setting, or the "
                    "document is shorter than the window. Increase 'sections' or reduce "
                    "'num_ctx' and repeat.")
    elif not hit_wide:
        reading += (" The wide run also failed, so the result does not isolate the effect of "
                    "the window. The model may not have followed the question; repeat with a "
                    "different model.")
    elif _ADMITS.search(narrow.text):
        reading += (" The narrow answer indicated that information was missing. It could not "
                    "know which text had been removed; the statement refers to the text it "
                    "received.")
    else:
        reading += (" The narrow answer gave a date without indicating that the relevant "
                    "section was unavailable. The question was identical in both runs; only "
                    "the amount of retained text differed.")
    return {"runs": [
        _run("Window 8,192 tokens", wide, prompt, settings={"num_ctx": 8192, "temperature": 0.0, "seed": 7},
             correct=hit_wide, window=8192),
        _run("Window %d tokens" % num_ctx, narrow, prompt,
             settings={"num_ctx": num_ctx, "temperature": 0.0, "seed": 7},
             correct=hit_narrow, window=num_ctx),
    ], "reading": reading}


# ================================================================== 3 · vary

VARY_PROMPT = (
    "A student submitted the following paragraph in an essay on assessment. Write one "
    "sentence of feedback on it.\n\n"
    "Paragraph: \"Formative assessment improves learning because students receive "
    "information about their progress while they can still act on it. Black and Wiliam "
    "(1998) showed this in their review. Therefore every module should replace its "
    "final examination with weekly quizzes.\""
)

INFO_VARY = {
    "title": "Temperature and seed: reproducibility of outputs",
    "aim": "To compare how many distinct outputs identical requests produce at "
           "temperature 0 with a fixed seed and at a higher temperature without a seed.",
    "background": [
        "A language model generates text one token at a time. For each position it "
        "computes a probability for every token in its vocabulary; a sampling procedure "
        "then selects one token.",
        "Temperature rescales these probabilities before sampling. At temperature 0 the "
        "most probable token is always selected, so the output is determined by the "
        "input. At higher temperatures, less probable tokens are selected more often and "
        "repeated requests yield different outputs. The seed initialises the random "
        "number generator used for sampling; with the same seed, settings, model version "
        "and software, the sampling is repeatable.",
        "Chat interfaces generally use a temperature above 0 and do not expose the seed. "
        "The same request can therefore yield different feedback or different "
        "assessments of the same text, and an earlier output cannot be reproduced. Even "
        "at temperature 0, identical outputs are only expected on the same model version, "
        "software and hardware.",
    ],
    "procedure": [
        "The prompt is sent n times at temperature 0 with seed 42 (parameter 'n').",
        "The same prompt is sent n times at a higher temperature without a seed "
        "(parameter 'temperature').",
        "Distinct outputs are counted in each group. Two outputs count as identical only "
        "if they match character for character.",
    ],
}


def lab_vary(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    n, temp, prompt = int(p["n"]), float(p["temperature"]), p["prompt"]
    cold = [backend.generate(prompt, temperature=0.0, seed=42, max_tokens=90) for _ in range(n)]
    hot = [backend.generate(prompt, temperature=temp, seed=None, max_tokens=90) for _ in range(n)]
    d_cold, d_hot = len({r.text for r in cold}), len({r.text for r in hot})
    reading = ("At temperature 0 with seed 42, %s produced %s. At temperature %.1f without "
               "a seed, %s produced %s." % (_plural(n, "request"), _plural(d_cold, "distinct output"),
                                            temp, _plural(n, "request"), _plural(d_hot, "distinct output")))
    if d_cold == 1 and d_hot > 1:
        reading += (" Only the first configuration allows an output to be reproduced by "
                    "repeating the request.")
    elif d_cold > 1:
        reading += (" Temperature 0 did not yield identical outputs on this route. Some "
                    "servers are not fully deterministic, for example when requests are "
                    "processed in parallel.")
    else:
        reading += (" The higher temperature also produced identical outputs in this run. "
                    "With a short answer and a strongly preferred wording this can occur; "
                    "increase 'n' or the temperature.")
    runs = [_run("Run %d · temperature 0.0, seed 42" % (i + 1), r, prompt,
                 settings={"temperature": 0.0, "seed": 42}) for i, r in enumerate(cold)]
    runs += [_run("Run %d · temperature %.1f, no seed" % (i + 1, temp), r, prompt,
                  settings={"temperature": temp, "seed": None}) for i, r in enumerate(hot)]
    return {"runs": runs, "reading": reading}


# ================================================================= 4 · steer

STEER_SPEC = (
    "You comment on undergraduate scientific writing. You address the writing, never "
    "the writer. You quote the specific words at issue. You give at most two points and "
    "end with one question the student can answer without further reading. You do not "
    "rewrite the sentence."
)
STEER_TASK = (
    "Comment on this sentence from a first-year lab report: 'The results were quite good "
    "and matched what we expected.'"
)

INFO_STEER = {
    "title": "Rules in the request or in the system prompt",
    "aim": "To compare the output for one task when the rules are absent, included in "
           "the user message, or supplied as a system prompt.",
    "background": [
        "Chat models distinguish messages by role. The system prompt is set before the "
        "conversation and applies to every subsequent request; user messages contain the "
        "individual requests. Custom instructions, custom GPTs, Gems and comparable "
        "features store a system prompt so that it need not be retyped. In the five "
        "stages used in this workshop, a stored instruction of this kind is called a "
        "skill prompt (stage 2).",
        "Whether a model follows rules more reliably from the system prompt than from "
        "the user message depends on the model and its training. Independently of that, "
        "a system prompt applies to every request in a session or tool, whereas rules "
        "typed into a request apply only to that request.",
        "To make compliance measurable, five of the rules are implemented as automatic "
        "checks (check_feedback in llmlab/checks.py). The checks are text-pattern tests, "
        "for example whether a passage stands in quotation marks or whether the last "
        "line ends with a question mark. They can misjudge individual outputs.",
    ],
    "procedure": [
        "Run A sends the task alone.",
        "Run B sends the rules followed by the task, both in the user message.",
        "Run C sends the rules as the system prompt and the task as the user message.",
        "All runs use temperature 0 and seed 11. Each output is checked against the "
        "five rules listed under materials.",
    ],
}


def _materials_steer(p):
    return [
        {"label": "Rules (used in runs B and C)", "text": STEER_SPEC},
        {"label": "Task", "text": p["task"]},
        {"label": "Automatic checks", "text": "\n".join(
            "- %s: %s" % (rule, how) for _, rule, how in FEEDBACK_RULES)},
    ]


def lab_steer(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    task = p["task"]
    settings = {"temperature": 0.0, "seed": 11}
    specs = (
        ("A · task only", "", task),
        ("B · rules and task in the user message", "", STEER_SPEC + "\n\n" + task),
        ("C · rules as system prompt, task as user message", STEER_SPEC, task),
    )
    runs, scores = [], []
    for label, system, prompt in specs:
        r = backend.generate(prompt, system=system, temperature=0.0, seed=11, max_tokens=180)
        checks = check_feedback(r.text)
        scores.append(passed(checks))
        runs.append(_run(label, r, prompt, system=system, settings=settings, checks=checks))
    a, b, c = scores
    reading = ("Checked against the five rules, run A passed %d, run B passed %d and run C "
               "passed %d." % (a, b, c))
    if a >= max(b, c):
        reading += (" The task alone performed as well as either version with rules, so this "
                    "model met the checked rules without being given them. The comparison is "
                    "not informative for this task and model.")
    elif abs(c - b) <= 1:
        reading += (" Runs B and C differ by at most one check. The rules had an effect; their "
                    "position had little effect. The difference that remains is persistence: "
                    "the system prompt applies to the next request without being repeated.")
    elif c > b:
        reading += (" The system prompt produced the higher score. This is a property of this "
                    "model and task and cannot be generalised.")
    else:
        reading += (" The rules in the user message produced the higher score. This is a "
                    "property of this model and task and cannot be generalised.")
    return {"runs": runs, "reading": reading}


# ================================================================ 5 · ground

GROUND_SOURCE = (
    "Regulation (EU) 2026/1744 defers the obligations attaching to standalone Annex III "
    "high-risk systems from 2 August 2026 to 2 December 2027. The AI literacy duty in "
    "Article 4, the prohibitions in Article 5 and the transparency duties in Article 50 "
    "are not deferred."
)
GROUND_QUESTION = (
    "Under the EU AI Act, when do the obligations for Annex III high-risk systems begin "
    "to apply, and what is not deferred?"
)
GROUND_TEMPLATE = (
    "Source:\n{source}\n\nQuestion: {question}\n\nAnswer using the source only. If the "
    "source does not settle the question, say so."
)

INFO_GROUND = {
    "title": "Grounding: answers with and without a source",
    "aim": "To compare an answer generated from the model's training data with an answer "
           "generated from a supplied source text, and to examine whether the two can be "
           "distinguished by reading them.",
    "background": [
        "A model's knowledge is limited to its training data, which ends at a cut-off "
        "date and contains errors and gaps. Asked about something outside that data, many "
        "models still produce a fluent answer. Such unsupported answers are commonly "
        "called hallucinations or confabulations.",
        "Grounding means placing the relevant source text in the prompt and instructing "
        "the model to answer from it. Retrieval-augmented generation (RAG) automates this "
        "step: a search component selects passages from a document collection and "
        "inserts them into the prompt. Grounding reduces unsupported statements but does "
        "not eliminate them; the model can still ignore, misread or go beyond the source.",
        "The source used here describes the amendment of the application dates of the EU "
        "AI Act by Regulation (EU) 2026/1744 (Digital Omnibus on AI). It postdates the "
        "training data of most local models, so the deferred date (2 December 2027) can "
        "only be given correctly with the source.",
    ],
    "procedure": [
        "Run A sends the question alone.",
        "Run B sends the source, the question and the instruction to answer from the "
        "source only.",
        "Both runs use temperature 0 and seed 3.",
        "Both answers are searched for the year 2027. Run A is also checked for an "
        "opening sentence that declines to answer.",
    ],
}


def _materials_ground(p):
    return [{"label": "Source (run B only)", "text": p["source"]},
            {"label": "Question", "text": p["question"]},
            {"label": "Prompt template for run B", "text": GROUND_TEMPLATE.format(
                source="<source>", question="<question>")}]


_ABSTAINS = re.compile(
    r"\bi(?:'m| am) (?:not able|unable) to\b"
    r"|\bi (?:do not|don't|cannot|can't) (?:have|provide|know|give|say|confirm|answer)\b"
    r"|\bno (?:reliable |specific |up-to-date )?information\b"
    r"|\bas of my (?:last|knowledge)\b"
    r"|\bmy (?:training|knowledge) (?:data|cut-?off)\b",
    re.I,
)


def abstained(text: str) -> bool:
    """Whether the answer opens by declining. Only the first sentence is read, so
    an answer that ends with a disclaimer still counts as an answer."""
    first = re.split(r"(?<=[.!?])\s", text.strip().replace("’", "'"), 1)[0]
    return bool(_ABSTAINS.search(first[:300]))


def lab_ground(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    source, question, fact = p["source"], p["question"], str(p["fact"])
    settings = {"temperature": 0.0, "seed": 3}
    grounded_prompt = GROUND_TEMPLATE.format(source=source, question=question)
    ungrounded = backend.generate(question, temperature=0.0, seed=3, max_tokens=160)
    grounded = backend.generate(grounded_prompt, temperature=0.0, seed=3, max_tokens=160)
    declined = abstained(ungrounded.text)
    u_has, g_has = fact in ungrounded.text, fact in grounded.text
    reading = ("Run A (no source) %s. Run B (with source) %s." % (
        "declined to answer" if declined else
        ("gave an answer containing %s" % fact if u_has else "gave an answer without %s" % fact),
        "gave an answer containing %s" % fact if g_has else "gave an answer without %s" % fact))
    if backend.simulated:
        reading += (" On the simulated route the wording is not generated by a model, so the "
                    "content of the answers is not interpretable.")
    elif declined:
        reading += (" This model declined without the source, which is the appropriate "
                    "behaviour. Other models answer the same question with a fluent but "
                    "outdated or invented date; repeat the lab with --model to compare.")
    elif g_has and not u_has:
        reading += (" Only the grounded answer contains the date from the source. Both answers "
                    "are phrased with comparable certainty, and neither states where its "
                    "information comes from.")
    elif u_has:
        reading += (" The ungrounded answer also contains %s. This may come from training data "
                    "or from chance; the answer itself gives no indication of which." % fact)
    else:
        reading += (" Neither answer contains %s, so the grounded answer did not use the "
                    "decisive detail of its source." % fact)
    reading += (" Whether an answer is supported by a source can only be established by "
                "comparing it with the source.")
    return {"runs": [
        _run("A · no source", ungrounded, question, settings=settings, declined=declined),
        _run("B · source supplied", grounded, grounded_prompt, settings=settings),
    ], "reading": reading}


# ================================================================ 6 · ladder

STAGES = ("prompt", "skill", "harness", "loop", "wiki")
LADDER_SINGLE = "02_extension.txt"

INFO_LADDER = {
    "title": "Five stages of prompting: answering student emails",
    "aim": "To apply the five stages of prompting to one administrative task and to "
           "record, for each stage, what is produced, what is checked and what remains "
           "for a person to decide.",
    "background": [
        "Task. The module team of a (fictitious) module, EDU-204, receives emails from "
        "students. Most concern dates, rooms or materials and can be answered from the "
        "module information. Requests for extensions and grade changes are decided by the "
        "examination office, not by the module team. Requests about other students must "
        "not be answered. The inbox contains seven emails, one of them in German.",
        "Stage 1, prompt. A single request in a chat window. The model has no module "
        "information, and nothing is stored after the exchange.",
        "Stage 2, skill prompt. A stored instruction contains the reply rules and the "
        "module information. Each email is still pasted and handled individually, and "
        "nobody checks the output systematically.",
        "Stage 3, harness. A program applies the same procedure to a folder of emails: it "
        "classifies each email, drafts a reply using the handling rule for its category, "
        "writes the reply to a file with a record of how it was produced, and sorts it "
        "into 'ready' or 'review'. At this stage the routing depends on the category "
        "alone. A harness is justified when one procedure is applied to many inputs and "
        "has to be documented.",
        "Stage 4, loop. Every draft is tested by nine automatic checks. Failed checks are "
        "returned to the model with a revision request, up to a fixed number of rounds. A "
        "reply is placed in 'ready' only if it passes all checks, belongs to a category "
        "approved for automatic handling and contains no open question.",
        "Stage 5, wiki. A Markdown file is read at the start of each run and extended at "
        "the end. The harness records lessons derived from failed checks and questions "
        "the sources could not answer. People answer open questions in the section "
        "'Approved answers', which later runs use as a source. The model does not change; "
        "the file does, and it can be read, corrected and versioned.",
    ],
    "procedure": [
        "Stage 1: email 02_extension.txt is sent with the request 'Answer this email:'. "
        "No system prompt.",
        "Stage 2: the same email is sent as the user message; the system prompt contains "
        "the specification and the module information.",
        "Stage 3: the first n emails of the inbox (parameter 'emails') are processed. Per "
        "email: one classification request, then one drafting request with the system "
        "prompt from stage 2. The nine checks are evaluated for comparison but not used "
        "for routing.",
        "Stage 4: the stage-3 drafts pass through the check-and-revise loop (parameter "
        "'rounds', counting the first draft). Routing now uses the checks.",
        "Stage 5: a wiki is compiled from stage 4 (lessons from failed first drafts; open "
        "questions). The lab then adds the entry from example_approved_answer.md under "
        "'Approved answers', in place of a decision by the module team, and processes the "
        "same emails again with the wiki. The categories from stage 3 are reused.",
        "All requests use temperature 0 and seed 42 (stages 1 and 2: seed 5).",
    ],
}


def _materials_ladder(p):
    task = tasks.load_task("student_emails")
    n = max(1, min(int(p["emails"]), len(task.inputs)))
    inbox = "\n\n".join("=== %s%s\n%s" % (name, "" if i < n else "  (not in this run)", text.strip())
                        for i, (name, text) in enumerate(task.inputs))
    cats = "\n".join("- %s (%s): %s Handling: %s" % (
        k, "reviewed by a person" if v["route"] == "human" else "automatic if checks pass",
        v["description"], v["handling"]) for k, v in task.categories.items())
    return [
        {"label": "Specification (spec.md)", "text": task.spec.strip()},
        {"label": "Reference document (context/module_information.md)", "text": task.context_text},
        {"label": "Categories (task.json)", "text": cats},
        {"label": "Inbox (inputs/)", "text": inbox},
        {"label": "Classification prompt (step 1)", "text": tasks.CLASSIFY_TEMPLATE.format(
            categories="\n".join("- %s: %s" % (k, v["description"]) for k, v in task.categories.items()),
            email="<email>")},
        {"label": "Drafting prompt (step 2; system prompt = specification + reference document)",
         "text": tasks.DRAFT_TEMPLATE},
        {"label": "Revision prompt (stage 4)", "text": tasks.REVISE_TEMPLATE},
        {"label": "Automatic checks (llmlab/checks.py)", "text": "\n".join(
            "- %s: %s" % (rule, how) for _, rule, how in EMAIL_RULES)},
        {"label": "Approved answer inserted at stage 5 (example_approved_answer.md)",
         "text": task.approved_example},
    ]


def _blocks(rec: Dict[str, Any]) -> List[Dict[str, str]]:
    b = [{"label": "Email", "text": rec["email"].strip()}]
    if rec.get("classify_prompt"):
        b.append({"label": "Step 1 · classification prompt", "text": rec["classify_prompt"]})
        b.append({"label": "Step 1 · model answer", "text": "%s  → category: %s" % (
            rec["classify_answer"], rec["category"])})
    for r in rec["rounds"]:
        if r["round"] == 1:
            b.append({"label": "Step 2 · drafting prompt (user message)", "text": r["prompt"]})
            b.append({"label": "Step 2 · draft (checks %s)" % score(r["checks"]), "text": r["text"]})
        else:
            b.append({"label": "Round %d · revision prompt" % r["round"], "text": r["prompt"]})
            b.append({"label": "Round %d · revised reply (checks %s)" % (r["round"], score(r["checks"])),
                      "text": r["text"]})
    return b


def _items(recs):
    return [{"label": "%s · %s · %s" % (r["name"], r["category"], r["route"]),
             "blocks": _blocks(r), "checks": r["checks"]} for r in recs]


def _unique(seq):
    out = []
    for x in seq:
        if x not in out:
            out.append(x)
    return out


def lab_ladder(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    stage = p["stage"]
    if stage != "all" and stage not in STAGES:
        raise KeyError("Unknown stage %r. Known: all, %s" % (stage, ", ".join(STAGES)))
    want = STAGES if stage == "all" else (stage,)
    task = tasks.load_task("student_emails")
    n = max(1, min(int(p["emails"]), len(task.inputs)))
    rounds = max(1, int(p["rounds"]))
    inbox = task.inputs[:n]
    system = tasks.system_prompt(task)
    one = task.input(LADDER_SINGLE).strip()
    meta = {"model": backend.model, "endpoint": backend.endpoint, "simulated": backend.simulated}
    runs, parts = [], []

    if "prompt" in want:
        prompt = "Answer this email:\n\n" + one
        r = backend.generate(prompt, temperature=0.0, seed=5, max_tokens=tasks.MAX_TOKENS)
        checks = tasks.run_checks(task, r.text, one, "extension")
        run = _run("Stage 1 · prompt", r, prompt, settings={"temperature": 0.0, "seed": 5},
                   artefact="None; the exchange remains in the chat window.", checks=checks)
        run["notes"].append("For the checks, the category 'extension' was assigned manually; "
                            "stage 1 has no classification step.")
        runs.append(run)
        parts.append("Stage 1 (request only) passed %s checks." % score(checks))

    if "skill" in want:
        r = backend.generate(one, system=system, temperature=0.0, seed=5, max_tokens=tasks.MAX_TOKENS)
        checks = tasks.run_checks(task, r.text, one, "extension")
        runs.append(_run("Stage 2 · skill prompt", r, one, system=system,
                         settings={"temperature": 0.0, "seed": 5},
                         artefact="A stored instruction: specification and module information.",
                         checks=checks))
        parts.append("Stage 2 (stored instruction with module information) passed %s checks."
                     % score(checks))

    s3: List[Dict[str, Any]] = []
    s4: List[Dict[str, Any]] = []

    def stage3():
        if not s3:
            s3.extend(tasks.draft(backend, task, name, email, system) for name, email in inbox)
        return s3

    def stage4():
        if not s4:
            s4.extend(tasks.loop(backend, task, copy.deepcopy(r), rounds) for r in stage3())
        return s4

    if "harness" in want:
        recs = stage3()
        ready = [r for r in recs if r["route"] == "ready"]
        ready_failing = [r for r in ready if not all_passed(r["checks"])]
        cats = ", ".join("%s: %d" % (c, sum(r["category"] == c for r in recs))
                         for c in _unique(r["category"] for r in recs))
        runs.append(_run(
            "Stage 3 · harness", None, None, system=system,
            settings={"temperature": 0.0, "seed": 42}, **meta,
            artefact="One reply file per email with a provenance header, sorted into "
                     "ready/ and review/, and a log.",
            text="%s processed: %d routed to 'ready', %d to 'review'." % (
                _plural(len(recs), "email"), len(ready), len(recs) - len(ready)),
            table={"columns": ["email", "language", "category", "route", "reason",
                               "checks (not used)"],
                   "rows": [[r["name"], r["language"], r["category"], r["route"], r["reason"],
                             score(r["checks"])] for r in recs]},
            items=_items(recs),
            notes=["Command for the full inbox, with files written: "
                   "python -m llmlab harness --task student_emails --out out"]))
        parts.append(
            "Stage 3 classified %s (%s). Routing by category placed %d in 'ready'; evaluated "
            "afterwards, %d of these failed at least one check." % (
                _plural(len(recs), "email"), cats, len(ready), len(ready_failing)))

    if "loop" in want:
        recs = stage4()
        first_ok = sum(all_passed(r["rounds"][0]["checks"]) for r in recs)
        final_ok = sum(all_passed(r["checks"]) for r in recs)
        ready = sum(r["route"] == "ready" for r in recs)
        revisions = sum(len(r["rounds"]) - 1 for r in recs)
        runs.append(_run(
            "Stage 4 · loop", None, None, system=system,
            settings={"temperature": 0.0, "seed": 42, "rounds": rounds}, **meta,
            artefact="A log of every round: checks, revision prompt, revised reply.",
            text="%s passed all checks as first drafts and %d after the loop; %d revision "
                 "requests were sent." % (_plural(first_ok, "reply"), final_ok, revisions),
            table={"columns": ["email", "category", "checks per round", "route", "reason"],
                   "rows": [[r["name"], r["category"],
                             " → ".join(score(x["checks"]) for x in r["rounds"]),
                             r["route"], r["reason"]] for r in recs]},
            items=_items(recs),
            notes=["Command for the full inbox: python -m llmlab harness --task "
                   "student_emails --out out --loop %d" % rounds]))
        parts.append(
            "At stage 4, %d of %d first drafts passed all checks and %d of %d did after up "
            "to %d rounds. %d replies were routed to 'ready'." % (
                first_ok, len(recs), final_ok, len(recs), rounds, ready))

    if "wiki" in want:
        recs4 = stage4()
        lessons = _unique(l for r in recs4 for l in tasks.lessons_for(r["rounds"][0]["checks"]))
        open_q = [tasks.open_question_entry(r) for r in recs4 if r["open_question"]]
        written = {"Lessons from failed checks": lessons, "Open questions": open_q,
                   "Approved answers": []}
        approved = [task.approved_example] if task.approved_example else []
        read = {"Lessons from failed checks": lessons, "Open questions": [],
                "Approved answers": approved}
        system5 = tasks.system_prompt(task, lessons, approved)
        recs5 = []
        for r in recs4:
            d = tasks.draft(backend, task, r["name"], r["email"], system5,
                            label=r["category"], approved=approved)
            recs5.append(tasks.loop(backend, task, d, rounds, approved=approved))
        first4 = sum(all_passed(r["rounds"][0]["checks"]) for r in recs4)
        first5 = sum(all_passed(r["rounds"][0]["checks"]) for r in recs5)
        ready4 = sum(r["route"] == "ready" for r in recs4)
        ready5 = sum(r["route"] == "ready" for r in recs5)
        runs.append(_run(
            "Stage 5 · wiki", None, None, system=system5,
            settings={"temperature": 0.0, "seed": 42, "rounds": rounds}, **meta,
            artefact="wiki.md: a Markdown file with lessons, open questions and approved "
                     "answers, read by every later run.",
            text="The wiki contained %s and %s. With it, %d of %d first drafts passed all "
                 "checks (stage 4: %d) and %d replies were routed to 'ready' (stage 4: %d)." % (
                     _plural(len(lessons), "lesson"), _plural(len(approved), "approved answer"),
                     first5, len(recs5), first4, ready5, ready4),
            files=[{"name": "wiki.md after stage 4 (entries written by the harness)",
                    "text": tasks.render_wiki(task, written)},
                   {"name": "wiki.md as read by stage 5 (approved answer added, answered "
                            "question removed)", "text": tasks.render_wiki(task, read)}],
            table={"columns": ["email", "category", "first draft: stage 4", "first draft: stage 5",
                               "route: stage 4", "route: stage 5"],
                   "rows": [[a["name"], a["category"], score(a["rounds"][0]["checks"]),
                             score(b["rounds"][0]["checks"]), a["route"], b["route"]]
                            for a, b in zip(recs4, recs5)]},
            items=_items(recs5),
            notes=["The entry under 'Approved answers' was inserted by the lab from "
                   "example_approved_answer.md. In the harness, only people write to this "
                   "section.",
                   "Command: python -m llmlab harness --task student_emails --out out "
                   "--loop %d --wiki wiki.md (run it twice, and add an approved answer to "
                   "wiki.md between the runs)." % rounds]))
        parts.append(
            "At stage 5 the wiki held %s, %s written by the harness, and %s. First drafts "
            "passing all checks rose from %d to %d, and replies routed to 'ready' from %d to "
            "%d." % (_plural(len(lessons), "lesson"), _plural(len(open_q), "open question"),
                     _plural(len(approved), "approved answer"), first4, first5, ready4, ready5))

    if any(s in want for s in ("harness", "loop", "wiki")):
        parts.append("The checks are text-pattern tests. A reply in 'ready' has passed these "
                     "tests; this does not establish that its content is correct.")
    return {"runs": runs, "reading": " ".join(parts)}


# ================================================================= 7 · route

INFO_ROUTE = {
    "title": "Deployment route and legal obligations",
    "aim": "To identify where the requests of this session were processed and which legal "
           "obligations depend on that deployment route.",
    "background": [
        "llmlab sends each request over HTTP to a model server. In the default "
        "configuration the server runs on the same computer and is addressed through the "
        "loopback interface (127.0.0.1), which other computers cannot reach. On this route "
        "the prompt and the output do not leave the computer.",
        "Data protection law distinguishes processing by the institution itself from "
        "processing by a service provider on its behalf (GDPR Art. 28), and it regulates "
        "transfers to third countries. A local route avoids the processor relationship "
        "and the transfer. It does not remove the need for a lawful basis for processing "
        "personal data (GDPR Art. 6).",
        "Obligations under the AI Act attach to the use of an AI system, not to its "
        "hosting: the AI literacy duty (Art. 4), transparency duties (Art. 50) and the "
        "classification of certain uses in education as high-risk (Annex III point 3) "
        "apply regardless of where the model runs.",
    ],
    "procedure": [
        "The endpoint of the active backend is read and checked for a loopback address.",
        "The request format of this backend is shown with a short example.",
        "The obligations are listed according to the route.",
    ],
}


def _materials_route(p, backend=None):
    if backend is None:
        return []
    url, payload = backend.request("Example user message", system="Example system prompt",
                                   temperature=0.0, seed=42, max_tokens=300)
    return [{"label": "Request format of the active backend (POST %s)" % url,
             "text": json.dumps(payload, indent=2, ensure_ascii=False)}]


def lab_route(backend: Backend, p: Dict[str, Any]) -> Dict[str, Any]:
    ep = backend.endpoint or "in-process"
    loopback = ("127.0.0.1" in ep) or ("localhost" in ep) or ("in-process" in ep)
    obligations = [
        "AI Act Art. 4: the deploying organisation takes measures to ensure sufficient AI "
        "literacy of its staff. Applies on every route.",
        "AI Act Art. 50: transparency towards persons who interact with an AI system or "
        "receive certain generated content. Applies on every route.",
        "AI Act Annex III point 3: AI systems used to decide on admission, to evaluate "
        "learning outcomes, to assign educational level or to monitor examinations are "
        "high-risk. Applies on every route.",
    ]
    if loopback:
        obligations.append(
            "GDPR: no transfer to a processor takes place on this route, so no processing "
            "agreement under Art. 28 is required. A lawful basis for processing personal "
            "data (Art. 6) is still required.")
    else:
        obligations.append(
            "GDPR Arts. 5, 6 and 28: this route sends text to another host. Before personal "
            "data of students is sent, a lawful basis and, for a service provider, a "
            "processing agreement are required.")
    return {"runs": [_run("Active route", None, None, **{
        "text": "Endpoint: %s\nLoopback: %s\nModel: %s" % (ep, "yes" if loopback else "no", backend.model),
        "endpoint": ep, "model": backend.model, "simulated": backend.simulated,
        "notes": obligations})],
        "reading": ("The requests in this session were processed on %s. The route determines "
                    "the data-protection obligations listed above; the AI Act obligations "
                    "apply regardless of the route." % (
                        "this computer" if loopback else "another host (%s)" % ep))}


# ================================================================= registry

INFO = {"tokens": INFO_TOKENS, "context": INFO_CONTEXT, "vary": INFO_VARY, "steer": INFO_STEER,
        "ground": INFO_GROUND, "ladder": INFO_LADDER, "route": INFO_ROUTE}

LABS: Dict[str, Callable] = {"tokens": lab_tokens, "context": lab_context, "vary": lab_vary,
                             "steer": lab_steer, "ground": lab_ground, "ladder": lab_ladder,
                             "route": lab_route}

DEFAULTS: Dict[str, Dict[str, Any]] = {
    "tokens": {"text": ""},
    "context": {"num_ctx": 1024, "sections": 120},
    "vary": {"n": 4, "temperature": 0.8, "prompt": VARY_PROMPT},
    "steer": {"task": STEER_TASK},
    "ground": {"source": GROUND_SOURCE, "question": GROUND_QUESTION, "fact": "2027"},
    "ladder": {"stage": "all", "emails": 4, "rounds": 3},
    "route": {},
}

MATERIALS = {
    "tokens": _materials_tokens,
    "context": _materials_context,
    "vary": lambda p: [{"label": "Prompt (identical in all runs)", "text": p["prompt"]}],
    "steer": _materials_steer,
    "ground": _materials_ground,
    "ladder": _materials_ladder,
    "route": _materials_route,
}

ORDER = ["tokens", "context", "vary", "steer", "ground", "ladder", "route"]

BLOCK_MAP = {
    "tokens": "Block 3.1 — terminology",
    "context": "Block 3.1 — terminology",
    "vary": "Block 2D — evaluation; Block 1 — verifiability",
    "steer": "Block 3 — stage 2, the skill prompt",
    "ground": "Block 1 — reliability of outputs",
    "ladder": "Block 3 — the five stages of prompting",
    "route": "Block 2 — hosting and legal framework",
}


def params(name: str, given: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Defaults merged with the given parameters, converted to the default's type."""
    if name not in LABS:
        raise KeyError("Unknown lab %r. Known: %s" % (name, ", ".join(ORDER)))
    p = dict(DEFAULTS[name])
    for k, v in (given or {}).items():
        if k in p and p[k] is not None and v is not None and not isinstance(p[k], str):
            v = type(p[k])(v)
        if v == "" and isinstance(p.get(k), str) and p[k]:
            continue  # an empty field in the interface keeps the default text
        p[k] = v
    return p


def describe(name: str, given: Optional[Dict[str, Any]] = None,
             backend: Optional[Backend] = None) -> Dict[str, Any]:
    """Everything about a lab except its results; no model is called."""
    p = params(name, given)
    mats = _materials_route(p, backend) if name == "route" else MATERIALS[name](p)
    return {"lab": name, **INFO[name], "block": BLOCK_MAP[name], "params": p, "materials": mats}


def run(name: str, backend: Backend, given: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    out = describe(name, given, backend)
    out.update(LABS[name](backend, out["params"]))
    out["simulated"] = backend.simulated
    return out
