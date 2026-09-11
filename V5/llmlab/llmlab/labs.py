"""Seven exercises. Each one exists to make a single claim from the session
checkable on the participant's own machine.

Every lab returns the same shape:

    {"lab", "title", "claim", "runs": [...], "reading": str, "ask": str}

`claim` is what the session asserted. `reading` is what the numbers mean —
and it is built from the numbers, so a run that does not show the claim says
so instead of asserting it anyway. `ask` is the question the facilitator puts
to the room while the output is on screen. The CLI prints all three; the
browser interface renders them.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from .backend import Backend, approx_tokens

FILLER = (
    "Institutional policy on the use of generative systems in teaching is "
    "revised annually. Module handbooks are published four weeks before the "
    "start of term. Assessment criteria are agreed at programme level and "
    "recorded in the quality handbook. Staff development is coordinated by the "
    "centre for teaching and learning. "
)


# ------------------------------------------------------ checks on feedback
#
# The steer and ladder labs hand the model a written rule set. These checks
# turn five of those rules into something a machine can test. They are crude
# on purpose: each is a line or two you can read, argue with and improve.
# At stage two a person checks the rules; from stage four on, these checks
# are what the loop runs against — so a crude check makes a crude loop.

_QUOTED = re.compile(
    r'["“„«]([^"“”„«»\n]{3,})["”“»]'
    r"|(?<!\w)['‘]([^'‘’\n]{3,}?)['’](?!\w)"
)
_LIST_ITEM = re.compile(r"^\s*(\d+[.)]|[-*•])\s+")
_ORDINAL = re.compile(r"\b(first|second|third|fourth)(ly)?\b[,:]", re.I)
_REWRITE = re.compile(
    r"\b(could|should|might|would) (instead )?(say|write|read|put|phrase)\b"
    r"|\b(revised|rewritten|improved|better) (version|sentence|text|paragraph|wording)\b"
    r"|\bhere(?:'s| is) (a|an|one) (rewrite|revision|revised|improved|better)\b"
    r"|\binstead,? (write|say|try)\b"
    r"|\btry (something like|writing|saying)\b",
    re.I,
)
_WRITER = re.compile(r"\b(you|your|the (writer|student|author))\b", re.I)


def _paragraphs(text: str) -> List[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


def check_feedback(text: str) -> List[Dict[str, Any]]:
    """Five of the written rules, as checks. Returns [{"rule", "ok"}, ...]."""
    t = text.strip().replace("’", "'")
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    last = lines[-1] if lines else ""
    ends_q = last.rstrip("*_\"' )").endswith("?")
    # The body is everything before the closing question.
    body = t[: t.rfind(last)] if ends_q else t
    items = [l for l in body.splitlines() if _LIST_ITEM.match(l)]
    if items:
        points = len(items)
    elif _ORDINAL.search(body):
        points = len(_ORDINAL.findall(body))
    else:
        points = len([p for p in _paragraphs(body) if not p.rstrip("*").endswith(":")])
    return [
        {"rule": "quotes the words at issue", "ok": bool(_QUOTED.search(t))},
        {"rule": "two points at most", "ok": points <= 2},
        {"rule": "ends with one question", "ok": ends_q and last.count("?") == 1},
        {"rule": "does not rewrite the text", "ok": not _REWRITE.search(t)},
        {"rule": "addresses the writing, not the writer", "ok": not _WRITER.search(body)},
    ]


def _met(checks: List[Dict[str, Any]]) -> int:
    return sum(1 for c in checks if c["ok"])


# ---------------------------------------------------------------- 1 · tokens


TOKENS_PAIR = (
    "Assessment criteria are agreed at programme level.",
    "Bewertungskriterien werden auf Programmebene vereinbart.",
)


def lab_tokens(backend: Backend, text: str = "", **kw) -> Dict[str, Any]:
    default = not text
    text = text or " ".join(TOKENS_PAIR)
    r = backend.count_prompt_tokens(text)
    chips = approx_tokens(text)
    chars = len(text)
    counted = r.prompt_tokens
    lines = []
    if counted:
        lines.append(
            "%d characters became %d tokens: %.2f characters per token."
            % (chars, counted, chars / counted)
        )
        off = abs(len(chips) - counted) / float(counted)
        lines.append(
            "The approximation drawn on screen gives %d. %s Only the model's own "
            "count decides what you are charged for and what fits."
            % (
                len(chips),
                "It is close and it is not the same number."
                if off <= 0.25
                else "It is off by %d%%, which is why it is labelled an "
                "approximation." % round(100 * off),
            )
        )
        if r.wrapper_tokens:
            lines.append(
                "The model actually received %d. The other %d are the chat "
                "template wrapped around your text: role markers and, on some "
                "models, a default system prompt. You never typed them, and they "
                "still count against the window."
                % (counted + r.wrapper_tokens, r.wrapper_tokens)
            )
    else:
        lines.append(
            "%d characters, approximately %d tokens by the on-screen rule."
            % (chars, len(chips))
        )
    if default and counted:
        en, de = (backend.count_prompt_tokens(s).prompt_tokens for s in TOKENS_PAIR)
        if en and de:
            lines.append(
                "Counted separately, the English sentence took %d tokens and the "
                "German one, with the same meaning, took %d. %s"
                % (
                    en,
                    de,
                    "The same content is a larger object in German, which is a "
                    "budgeting fact and an equity fact."
                    if de > en
                    else "On this model the German cost no more, which is not true "
                    "of every tokenizer; try Polish or Greek with --text.",
                )
            )
    elif any(ord(c) > 127 for c in text):
        lines.append(
            "Text outside basic Latin often costs more tokens per character than "
            "English — a budgeting fact and an equity fact. Run the lab without "
            "--text to see an English and a German sentence measured side by side."
        )
    return {
        "lab": "tokens",
        "title": "What the model actually receives",
        "claim": "A token is not a word, and the difference is a number you can see.",
        "runs": [{"label": "prompt", "input": text, "chips": chips, **r.as_dict()}],
        "reading": " ".join(lines),
        "ask": "Whose language costs more to process, and what follows from that?",
    }


# --------------------------------------------------------------- 2 · context

_ADMITS = re.compile(
    r"\b(not (found|present|included|provided|visible|available|mentioned|given)"
    r"|cannot|can't|unable|no code word|missing|does not (appear|contain|mention|say))\b",
    re.I,
)


def lab_context(
    backend: Backend,
    num_ctx: int = 256,
    filler_repeats: int = 40,
    code_word: str = "BASALT",
    **kw
) -> Dict[str, Any]:
    haystack = ("The CODE WORD is %s.\n\n" % code_word) + (FILLER * int(filler_repeats))
    question = (
        haystack
        + "\n\nUsing only the text above, state the code word. Answer with the word alone."
    )
    wide = backend.generate(question, temperature=0.0, seed=7, num_ctx=8192, max_tokens=20)
    narrow = backend.generate(
        question, temperature=0.0, seed=7, num_ctx=int(num_ctx), max_tokens=20
    )
    hit_wide = code_word.lower() in wide.text.lower()
    hit_narrow = code_word.lower() in narrow.text.lower()
    reading = (
        "The code word sits in the first line. With a wide window the answer is "
        "%s. With a %d-token window the answer is %s."
        % (
            "correct" if hit_wide else "wrong",
            int(num_ctx),
            "correct" if hit_narrow else "wrong",
        )
    )
    if hit_narrow:
        reading += (
            " This run does not show the claim. Raise the filler or lower the "
            "window until the narrow run fails — the failure is the demonstration."
        )
    elif _ADMITS.search(narrow.text):
        reading += (
            " Nothing about the question changed; the first line stopped being "
            "available. This time the narrow run did say something was missing. "
            "Most runs do not, and you cannot tell in advance which kind you will get."
        )
    else:
        reading += (
            " Nothing about the question changed; the first line stopped being "
            "available. Note what the narrow run did not do: it did not report "
            "that material was missing. It answered with the same confidence as "
            "the correct run."
        )
    return {
        "lab": "context",
        "title": "The window is a boundary, not a setting",
        "claim": "Material outside the context window is absent, and absence is silent.",
        "runs": [
            {"label": "window 8192", "correct": hit_wide, **wide.as_dict()},
            {"label": "window %d" % int(num_ctx), "correct": hit_narrow, **narrow.as_dict()},
        ],
        "reading": reading,
        "ask": "You paste a 90-page thesis and ask for a summary. Which parts were read?",
    }


# ------------------------------------------------------------------- 3 · vary


def lab_vary(
    backend: Backend,
    prompt: str = "Give one sentence of feedback on a student essay that argues its case clearly but cites only one source.",
    n: int = 4,
    temperature: float = 0.8,
    **kw
) -> Dict[str, Any]:
    cold = [
        backend.generate(prompt, temperature=0.0, seed=42, max_tokens=90)
        for _ in range(int(n))
    ]
    hot = [
        backend.generate(prompt, temperature=float(temperature), seed=None, max_tokens=90)
        for _ in range(int(n))
    ]
    d_cold = len({r.text for r in cold})
    d_hot = len({r.text for r in hot})
    reading = (
        "%d identical runs at temperature 0 produced %d distinct answers. The "
        "same runs at temperature %.1f produced %d. The setting that changed is "
        "not a quality dial; it is how the next token is chosen. If you are "
        "grading with this, an unstable setting means two identical scripts can "
        "receive different comments, and you cannot reproduce either."
        % (int(n), d_cold, float(temperature), d_hot)
    )
    return {
        "lab": "vary",
        "title": "Same input, different output",
        "claim": "Reproducibility is a configuration choice, and the default is not it.",
        "runs": [{"label": "temperature 0.0, seed 42", **r.as_dict()} for r in cold]
        + [{"label": "temperature %.1f, no seed" % float(temperature), **r.as_dict()} for r in hot],
        "reading": reading,
        "ask": "Which of your uses would survive a student asking you to run it again?",
    }


# ------------------------------------------------------------------ 4 · steer

STEER_SPEC = (
    "You comment on undergraduate scientific writing. You address the "
    "writing, never the writer. You quote the specific words at issue. "
    "You give at most two points and end with one question the student "
    "can answer without further reading. You do not rewrite the sentence."
)


def lab_steer(
    backend: Backend,
    task: str = "Comment on this sentence from a first-year lab report: 'The results were quite good and matched what we expected.'",
    **kw
) -> Dict[str, Any]:
    bare = backend.generate(task, temperature=0.0, seed=11, max_tokens=180)
    pasted = backend.generate(
        STEER_SPEC + "\n\n" + task, temperature=0.0, seed=11, max_tokens=180
    )
    standing = backend.generate(
        task, system=STEER_SPEC, temperature=0.0, seed=11, max_tokens=180
    )
    runs, scores = [], []
    for label, r in (
        ("request only", bare),
        ("the same rules pasted into the request", pasted),
        ("request plus skill prompt", standing),
    ):
        checks = check_feedback(r.text)
        scores.append(_met(checks))
        runs.append({"label": label, "checks": checks, **r.as_dict()})
    b, p, s = scores
    n = len(runs[0]["checks"])
    reading = (
        "Same task, same temperature, same seed. Checked against five of the "
        "instruction's rules, the bare request met %d of %d, the same rules "
        "pasted into the request met %d, and the standing instruction met %d."
        % (b, n, p, s)
    )
    if b >= max(p, s):
        reading += (
            " The bare request did as well as either, so this model met these "
            "rules without being told. Try a harder task before drawing a "
            "conclusion from this one."
        )
    elif abs(s - p) <= 1:
        reading += (
            " The words did the work, not the place they sat. The difference is "
            "what happens next time: the standing instruction applies to the "
            "next request without anyone retyping it, and the pasted version has "
            "to be pasted again, by you, correctly, every time."
        )
    elif s > p:
        reading += (
            " Here the standing position also helped the output. That is a "
            "property of this model, not a rule, and the stronger reason to keep "
            "it standing is still that it survives to the next request."
        )
    else:
        reading += (
            " Here the pasted version did better. Where an instruction sits "
            "matters to some models; the reason to keep it standing is still "
            "that it survives to the next request."
        )
    reading += (
        " The checks are crude on purpose — a line or two each in llmlab/labs.py. "
        "Read one and argue with it."
    )
    return {
        "lab": "steer",
        "title": "The instruction that stays",
        "claim": (
            "A skill prompt — a standing instruction — is worth more than a "
            "better-worded request, because it stays, not because it writes better."
        ),
        "runs": runs,
        "reading": reading,
        "ask": "Which of the three could you hand to a colleague and expect the same result?",
    }


# ----------------------------------------------------------------- 5 · ground

_ABSTAINS = re.compile(
    r"\bi(?:'m| am) (?:not able|unable) to\b"
    r"|\bi (?:do not|don't|cannot|can't) (?:have|provide|know|give|say|confirm|answer)\b"
    r"|\bno (?:reliable |specific |up-to-date )?information\b"
    r"|\bas of my (?:last|knowledge)\b"
    r"|\bmy (?:training|knowledge) (?:data|cut-?off)\b",
    re.I,
)


def abstained(text: str) -> bool:
    """Did the answer open by declining? Only the first sentence is read, so
    a fluent answer that ends on a disclaimer still counts as an answer."""
    first = re.split(r"(?<=[.!?])\s", text.strip().replace("’", "'"), 1)[0]
    return bool(_ABSTAINS.search(first[:300]))


def lab_ground(
    backend: Backend,
    source: str = (
        "Regulation (EU) 2026/1744 defers the obligations attaching to standalone "
        "Annex III high-risk systems from 2 August 2026 to 2 December 2027. The AI "
        "literacy duty in Article 4, the prohibitions in Article 5 and the "
        "transparency duties in Article 50 are not deferred."
    ),
    question: str = (
        "Under the EU AI Act, when do the obligations for Annex III high-risk "
        "systems begin to apply, and what is not deferred?"
    ),
    fact: str = "2027",
    **kw
) -> Dict[str, Any]:
    ungrounded = backend.generate(question, temperature=0.0, seed=3, max_tokens=160)
    grounded = backend.generate(
        "Source:\n%s\n\nQuestion: %s\n\nAnswer using the source only. If the "
        "source does not settle it, say so." % (source, question),
        temperature=0.0,
        seed=3,
        max_tokens=160,
    )
    declined = abstained(ungrounded.text)
    u = {"label": "no source supplied", **ungrounded.as_dict()}
    if declined:
        u["notes"] = u["notes"] + ["This answer declined rather than answering."]

    if declined:
        reading = (
            "This run does not show the claim. Without the source, this model "
            "declined to answer — the good case, and not one you can count on: "
            "the same question put to another model may come back as a fluent "
            "timeline for the wrong year or the wrong law. Run it again with "
            "--model and a different model to see the other case. The claim "
            "still holds in the other direction: the grounded answer's "
            "confidence is not evidence that it used its source. Only checking "
            "it against the source tells you that."
        )
    else:
        reading = (
            "Both answers are fluent, and neither says where its information came "
            "from. One had the text in front of it and one did not, and the "
            "register gives you no way to tell them apart."
        )
        if fact and fact in source and not backend.simulated:
            g_has, u_has = fact in grounded.text, fact in ungrounded.text
            if g_has and not u_has:
                reading += (
                    " Only the grounded one gives the detail the source supplies "
                    "(%s); the other answered anyway." % fact
                )
            elif u_has:
                reading += (
                    " The ungrounded one also gives %s — from training data or by "
                    "luck, and nothing on the screen tells you which." % fact
                )
            else:
                reading += (
                    " Neither gives %s, the detail the source supplies, so even the "
                    "grounded answer did not use its source. That is its own "
                    "finding." % fact
                )
        reading += (
            " Fluency is not evidence of grounding, which is why the verification "
            "step belongs to you and cannot be delegated to the thing being verified."
        )
    return {
        "lab": "ground",
        "title": "With the source and without it",
        "claim": "You cannot tell a grounded answer from an ungrounded one by reading it.",
        "runs": [u, {"label": "source supplied", **grounded.as_dict()}],
        "reading": reading,
        "ask": "Which of these would you have forwarded to a colleague without checking?",
    }


# ----------------------------------------------------------------- 6 · ladder


LADDER_TASK = "Write feedback on one paragraph of student writing."

LADDER_SPEC = (
    "You comment on undergraduate writing. Address the writing, never "
    "the writer. Quote the words at issue. Two points maximum. End with "
    "one answerable question. Do not rewrite the text."
)


# What a stage-five wiki records when a rule was missed. One line per rule, so
# the wiki stays short enough for a person to read and correct.
LESSONS = {
    "quotes the words at issue": "Quote the exact words at issue, in quotation marks.",
    "two points at most": "Stop at two points, even when more come to mind.",
    "ends with one question": "End with exactly one question the student can answer.",
    "does not rewrite the text": "Do not offer replacement wording; the student revises.",
    "addresses the writing, not the writer": "Talk about the text, never about 'you' or 'the writer'.",
}


def lessons_for(checks: List[Dict[str, Any]]) -> List[str]:
    """The wiki lines a run earns: one per rule it missed."""
    return [LESSONS[c["rule"]] for c in checks if not c["ok"] and c["rule"] in LESSONS]


def revise_until_met(
    backend: Backend,
    system: str,
    draft: str,
    rounds: int,
    seed: int = 5,
    max_tokens: int = 140,
) -> List[Dict[str, Any]]:
    """Stage four: check the draft, revise what failed, check again.

    Stops when all checks pass or after `rounds` rounds in total, whichever
    comes first. Returns one entry per round, so the loop leaves a log.
    """
    log = [{"round": 1, "text": draft, "checks": check_feedback(draft)}]
    while len(log) < rounds:
        missed = [c["rule"] for c in log[-1]["checks"] if not c["ok"]]
        if not missed:
            break
        r = backend.generate(
            "Here is your comment:\n\n%s\n\nIt missed these rules: %s. Revise it so "
            "it meets them, keep what already works, and output only the revised "
            "comment." % (log[-1]["text"], "; ".join(missed)),
            system=system,
            temperature=0.0,
            seed=seed,
            max_tokens=max_tokens,
        )
        log.append({"round": len(log) + 1, "text": r.text, "checks": check_feedback(r.text)})
    return log


STAGES = ("prompt", "skill", "harness", "loop", "wiki")


def lab_ladder(backend: Backend, stage: str = "all", rounds: int = 3, **kw) -> Dict[str, Any]:
    sample = (
        "In conclusion, this essay has shown that assessment is important and "
        "that many factors are involved, which shows the topic is complex."
    )
    want = STAGES if stage == "all" else (stage,)
    runs = []
    skill = None

    def skill_run():
        # Stages four and five both start from the stage-two draft.
        nonlocal skill
        if skill is None:
            skill = backend.generate(sample, system=LADDER_SPEC, temperature=0.0, seed=5, max_tokens=140)
        return skill

    if "prompt" in want:
        r = backend.generate(
            "Give feedback on this paragraph:\n" + sample, temperature=0.0, seed=5, max_tokens=140
        )
        runs.append({"label": "1 · prompt", "artefact": "a chat window",
                     "checks": check_feedback(r.text), **r.as_dict()})

    if "skill" in want:
        r = skill_run()
        runs.append({"label": "2 · skill prompt", "artefact": "a saved instruction",
                     "spec": LADDER_SPEC, "checks": check_feedback(r.text), **r.as_dict()})

    if "harness" in want:
        runs.append({
            "label": "3 · harness prompt",
            "artefact": "a specification an agent works inside, and a trail",
            "text": (
                "Not shown here, because the point of this stage is that it does not "
                "live in a window. Run it from the command line:\n\n"
                "    python -m llmlab harness --spec examples/feedback_spec.md "
                "--inputs examples/inputs --out out\n\n"
                "That command applies one written specification to every file in a "
                "folder, writes one output file per input, and records the model, the "
                "settings and the timestamp in each."
            ),
            "prompt_tokens": None, "output_tokens": None, "seconds": 0.0,
            "model": backend.model, "endpoint": "command line",
            "simulated": backend.simulated, "notes": [],
        })

    loop_log = None
    if "loop" in want:
        first = skill_run()
        loop_log = revise_until_met(backend, LADDER_SPEC, first.text, int(rounds))
        last = loop_log[-1]
        notes = ["round %d: %d of %d rules met" % (e["round"], _met(e["checks"]), len(e["checks"]))
                 for e in loop_log]
        notes.append("stopped: all rules met" if _met(last["checks"]) == len(last["checks"])
                     else "stopped: limit of %d rounds reached" % int(rounds))
        runs.append({"label": "4 · loop prompt", "artefact": "a log of every round",
                     "text": last["text"], "checks": last["checks"], "notes": notes,
                     "prompt_tokens": None, "output_tokens": None, "seconds": 0.0,
                     "model": backend.model, "endpoint": first.endpoint,
                     "simulated": backend.simulated})

    wiki_lines = None
    before = after = None
    if "wiki" in want:
        first = skill_run()
        before = check_feedback(first.text)
        wiki_lines = lessons_for(before)
        if wiki_lines:
            wiki = "Lessons from earlier runs:\n" + "\n".join("- " + l for l in wiki_lines)
            r = backend.generate(sample, system=LADDER_SPEC + "\n\n" + wiki,
                                 temperature=0.0, seed=5, max_tokens=140)
            after = check_feedback(r.text)
            runs.append({"label": "5 · wiki", "artefact": "a knowledge base that grows",
                         "wiki": wiki, "checks": after, **r.as_dict()})
        else:
            runs.append({"label": "5 · wiki", "artefact": "a knowledge base that grows",
                         "text": "Nothing to write down: the stage-two draft met every rule, "
                                 "so this run earns no lesson and the wiki stays empty.",
                         "prompt_tokens": None, "output_tokens": None, "seconds": 0.0,
                         "model": backend.model, "endpoint": "none",
                         "simulated": backend.simulated, "notes": []})

    parts = []
    if skill is not None:
        s = check_feedback(skill.text)
        parts.append("Stage two, the skill prompt, met %d of %d written rules." % (_met(s), len(s)))
    if loop_log is not None:
        last = loop_log[-1]["checks"]
        parts.append(
            "The stage-four loop %s after %d round%s."
            % ("met every rule" if _met(last) == len(last) else "stopped at its limit with %d of %d met" % (_met(last), len(last)),
               len(loop_log), "" if len(loop_log) == 1 else "s")
        )
    if wiki_lines:
        parts.append(
            "At stage five the misses became %d line%s of wiki, and the same model, "
            "reading them, met %d of %d instead of %d. Nothing about the model changed. "
            "A few lines of text did — which is all 'self-learning' means here, and why "
            "the wiki is the thing to govern."
            % (len(wiki_lines), "" if len(wiki_lines) == 1 else "s", _met(after), len(after), _met(before))
        )
    elif wiki_lines == []:
        parts.append(
            "Stage five had nothing to learn from this run: stage two met every rule, "
            "so no lesson was written. To watch the wiki being written, run the "
            "harness with --loop 3 --wiki wiki.md over the example inputs, or this lab "
            "with a smaller model."
        )
    parts.append(
        "The checks are crude on purpose, and the loop and the wiki inherit that: a "
        "crude check makes a crude loop. What survives the session: nothing, one "
        "instruction, a specification and its trail, a log of rounds, a wiki that grows."
    )
    return {
        "lab": "ladder",
        "title": "Five stages, five artefacts",
        "claim": "The stage you work at decides what survives — and what you now have to govern.",
        "runs": runs,
        "reading": " ".join(parts),
        "ask": "Which stage is your current practice at, and who reads what it leaves behind?",
    }


# ------------------------------------------------------------------ 7 · route


def lab_route(backend: Backend, **kw) -> Dict[str, Any]:
    ep = backend.endpoint or "in-process"
    loopback = ("127.0.0.1" in ep) or ("localhost" in ep) or ("in-process" in ep)
    obligations = [
        "Art. 4 AI Act — the literacy duty falls on the deploying organisation "
        "and applies on every route, including this one.",
        "Art. 50 AI Act — transparency to the person interacting, if learners "
        "meet the output.",
    ]
    if loopback:
        obligations.append(
            "GDPR — no transfer to a processor occurs on this route, so there is "
            "no processor agreement to hold. The lawful basis for holding the "
            "data at all does not disappear with it."
        )
        obligations.append(
            "Annex III §3 is unaffected by where the model runs. A local model "
            "used to determine access, assign learning or grade is the same "
            "situation as a hosted one."
        )
    else:
        obligations.append(
            "GDPR Arts. 5 and 28 — this route sends text to a third party. A "
            "processor agreement and a lawful basis are required before student "
            "material goes near it."
        )
    return {
        "lab": "route",
        "title": "Where the bytes went",
        "claim": "Deployment route changes which obligations apply — and which it does not.",
        "runs": [
            {
                "label": "this session",
                "text": "Endpoint: %s\nLoopback: %s\nModel: %s"
                % (ep, "yes" if loopback else "no", backend.model),
                "endpoint": ep,
                "model": backend.model,
                "simulated": backend.simulated,
                "prompt_tokens": None,
                "output_tokens": None,
                "seconds": 0.0,
                "notes": obligations,
            }
        ],
        "reading": (
            "Everything in this lab stayed on %s. That answers the data-protection "
            "question and none of the others. Local is a hosting fact, not a "
            "compliance verdict." % ("this machine" if loopback else "a remote host")
        ),
        "ask": "Which of the four obligations above did running it locally remove?",
    }


LABS = {
    "tokens": lab_tokens,
    "context": lab_context,
    "vary": lab_vary,
    "steer": lab_steer,
    "ground": lab_ground,
    "ladder": lab_ladder,
    "route": lab_route,
}

ORDER = ["tokens", "context", "vary", "steer", "ground", "ladder", "route"]

BLOCK_MAP = {
    "tokens": "Block 3.1 — terminology as diagnostic",
    "context": "Block 3.1 — terminology as diagnostic",
    "vary": "Block 2D — evaluation, and Block 1 on non-verifiability",
    "steer": "Block 3 — stage two of the prompting evolution, the skill prompt",
    "ground": "Block 1 — why outputs cannot be trusted",
    "ladder": "Block 3 — the five stages of the prompting evolution",
    "route": "Block 2 — hosting, and the legal panel",
}


def run(name: str, backend: Backend, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if name not in LABS:
        raise KeyError("Unknown lab %r. Known: %s" % (name, ", ".join(ORDER)))
    out = LABS[name](backend, **(params or {}))
    out["block"] = BLOCK_MAP.get(name, "")
    out["simulated"] = backend.simulated
    return out
