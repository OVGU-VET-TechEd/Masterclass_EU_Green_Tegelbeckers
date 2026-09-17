"""Automatic checks on model output.

Two sets of checks are defined here:

  check_feedback  five rules for written feedback on student text (lab 4)
  check_email     seven rules for replies to student emails (lab 6 and the
                  harness)

Each check is a short text-pattern test. None of them interprets the text.
A check reports whether a pattern is present, which approximates whether a
rule was followed. Individual outputs can be misjudged in both directions,
and the loop in stage four inherits every such error.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Set, Tuple

# ------------------------------------------------------------- feedback rules

FEEDBACK_RULES = [
    ("quoted", "quotes the words at issue",
     "passes if a passage of at least three characters stands in quotation marks"),
    ("points", "two points at most",
     "counts list items; if there are none, ordinal words (first, second, ...); "
     "otherwise paragraphs"),
    ("question", "ends with one question",
     "passes if the last line ends with a question mark and contains no other"),
    ("no_rewrite", "does not rewrite the text",
     "fails on phrases such as 'could say', 'revised version', 'instead, write'"),
    ("writing", "addresses the writing, not the writer",
     "fails if 'you', 'your', 'the student', 'the writer' or 'the author' occurs "
     "before the closing question"),
]

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
    """The five feedback rules as checks. Returns [{"id", "rule", "ok"}, ...]."""
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
    ok = {
        "quoted": bool(_QUOTED.search(t)),
        "points": points <= 2,
        "question": ends_q and last.count("?") == 1,
        "no_rewrite": not _REWRITE.search(t),
        "writing": not _WRITER.search(body),
    }
    return [{"id": i, "rule": rule, "ok": ok[i]} for i, rule, _ in FEEDBACK_RULES]


# ---------------------------------------------------------------- email rules

EMAIL_RULES = [
    ("frame", "opens with a salutation and closes with the signature in the reply's language",
     "the first line starts with Dear, Hello, Hi, Sehr geehrte, Liebe, Hallo or "
     "Guten Tag; the last three lines contain the signature and a closing in the "
     "language of the reply (e.g. 'Kind regards' or 'Mit freundlichen Grüßen')"),
    ("length", "stays within the word limit",
     "counts words; passes at or below the limit set in task.json"),
    ("topic", "addresses the subject of the email",
     "takes the content words of the subject line (e.g. 'slides' in 'Slides for "
     "next week') and passes if at least one of them occurs in the reply; required "
     "only for categories handled automatically, and not for a reply that states "
     "the open-question sentence"),
    ("dates", "every date appears in the reference documents or in the email",
     "extracts dates such as '9 February', 'February 9' or '09.02.2027' and "
     "compares day and month with the dates in the sources"),
    ("quoted", "quoted names match the sources exactly",
     "every passage in quotation marks (course, folder or room names) must occur "
     "verbatim in the reference documents, the approved answers or the email"),
    ("decision", "makes no decision reserved for the examination office",
     "fails on a sentence with 'I' or 'we' and a verb such as grant, extend, "
     "approve, change or raise without a negation, or on phrases such as "
     "'your extension has been granted'"),
    ("referral", "names the examination office",
     "required for the categories extension and grade; passes if 'examination "
     "office' or 'Prüfungsamt' occurs"),
    ("language", "replies in the language of the email",
     "counts frequent German and English function words in email and reply"),
    ("identifiers", "repeats no matriculation number",
     "fails if a number with six to eight digits occurs"),
]

EMAIL_LESSONS = {
    "frame": "Open with a salutation; close with 'Kind regards,' (German: 'Mit freundlichen Grüßen') and the signature on its own line.",
    "length": "Keep the reply within the word limit.",
    "topic": "Answer the question the email asks, using the sources only; if the sources do not contain the answer, write the sentence for open questions instead of promising or inventing anything.",
    "dates": "Give only dates that appear in the reference documents, the approved answers or the student's email.",
    "quoted": "Copy names of courses, folders and rooms exactly as written in the reference documents; do not translate them.",
    "decision": "Do not grant, promise or suggest an extension or a grade change; the examination office decides.",
    "referral": "For extensions, illness and grades, name the examination office and its address.",
    "language": "Reply in the language of the student's email.",
    "identifiers": "Do not repeat matriculation numbers or other identifiers.",
}

MONTHS = {
    "january": 1, "jan": 1, "januar": 1, "jänner": 1,
    "february": 2, "feb": 2, "februar": 2,
    "march": 3, "mar": 3, "märz": 3, "maerz": 3,
    "april": 4, "apr": 4,
    "may": 5, "mai": 5,
    "june": 6, "jun": 6, "juni": 6,
    "july": 7, "jul": 7, "juli": 7,
    "august": 8, "aug": 8,
    "september": 9, "sep": 9, "sept": 9,
    "october": 10, "oct": 10, "oktober": 10, "okt": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12, "dezember": 12, "dez": 12,
}
MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
_M = "|".join(sorted(MONTHS, key=len, reverse=True))
_DAY_MONTH = re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)?\.?\s+(?:of\s+)?(%s)\b" % _M, re.I)
_MONTH_DAY = re.compile(r"\b(%s)\.?\s+(\d{1,2})(?:st|nd|rd|th)?\b" % _M, re.I)
_NUMERIC = re.compile(r"(?<![\d.])(\d{1,2})\.(\d{1,2})\.(?:\d{4}|\d{2})?(?![\d:])")


def dates_in(text: str) -> Set[Tuple[int, int]]:
    """Day and month of every date the patterns recognise."""
    found = set()
    for m in _DAY_MONTH.finditer(text):
        found.add((int(m.group(1)), MONTHS[m.group(2).lower()]))
    for m in _MONTH_DAY.finditer(text):
        found.add((int(m.group(2)), MONTHS[m.group(1).lower()]))
    for m in _NUMERIC.finditer(text):
        found.add((int(m.group(1)), int(m.group(2))))
    return {(d, mo) for d, mo in found if 1 <= d <= 31 and 1 <= mo <= 12}


_DE = {"der", "die", "das", "und", "ich", "sie", "ihre", "ihr", "nicht", "ist", "wir",
       "für", "mit", "von", "zu", "bitte", "vielen", "dank", "grüße", "grüßen", "sehr",
       "geehrte", "geehrtes", "geehrter", "finden", "wann", "wo", "auf", "im", "eine",
       "einen", "ein", "dem", "den", "bei", "freundlichen", "modulteam", "außerdem"}
_EN = {"the", "and", "is", "you", "your", "for", "with", "to", "please", "thank",
       "dear", "regards", "of", "we", "our", "can", "will", "be", "on", "this", "that",
       "are", "an", "module", "team", "kind"}


def language(text: str) -> str:
    """'de' or 'en', by counting frequent function words."""
    words = re.findall(r"[a-zäöüß]+", text.lower())
    de = sum(w in _DE for w in words)
    en = sum(w in _EN for w in words)
    return "de" if de > en else "en"


_SENTENCE = re.compile(r"(?<=[.!?])\s+|\n+")
_COMMIT_VERB = re.compile(
    r"\b(grant(ed|ing)?|extend(ed|ing)?|approve[ds]?|approving|change[ds]?|changing"
    r"|raise[ds]?|raising|increase[ds]?|adjust(ed)?|verlänger(n|t|e)|genehmig(en|t|e)"
    r"|ändern|geändert|anheben|angehoben|erhöhen|erhöht)\b",
    re.I,
)
_FIRST_PERSON = re.compile(r"\b(i|we|ich|wir)\b", re.I)
_NEGATION = re.compile(r"\b(not|cannot|unable|no|only|nicht|kein\w*|nur)\b|n't\b", re.I)
_DECIDED = re.compile(
    r"\b(deadline|extension|grade|mark|frist|note)\b[^.!?\n]{0,40}\b(has been|have been|is|was|will be|wurde|wird)\s+"
    r"(granted|extended|approved|changed|raised|increased|verlängert|genehmigt|geändert|angehoben)\b",
    re.I,
)
_REFER = re.compile(r"examination office|pr(ü|ue)fungsamt", re.I)
_IDENTIFIER = re.compile(r"(?<!\d)\d{6,8}(?!\d)")
_SALUTATION = re.compile(
    r"^(dear|hello|hi|good (morning|afternoon)|sehr geehrte\w*|liebe\w*|hallo|guten tag)\b", re.I
)
_WORDS = re.compile(r"\w+(?:[-'’]\w+)*")
_CLOSING = {
    "en": re.compile(r"\b(kind regards|best regards|regards|best wishes|sincerely)\b", re.I),
    "de": re.compile(r"(mit freundlichen grüßen|freundliche grüße|viele grüße|beste grüße)", re.I),
}
_SUBJECT_LINE = re.compile(r"^(?:subject|betreff):\s*(.+)$", re.I | re.M)
_TOPIC_STOP = {"about", "question", "questions", "regarding", "from", "next", "week", "with",
               "your", "this", "that", "please", "request", "frage", "fragen", "über", "und",
               "mein", "meine", "meiner", "für", "eine", "einer"}
_QUOTE = re.compile(r'["“„«]([^"“”„«»\n]{2,60})["”“»]')


def topic_words(email: str) -> List[str]:
    """Content words of the subject line, lower case."""
    m = _SUBJECT_LINE.search(email)
    if not m:
        return []
    return [w for w in re.findall(r"[a-zäöüß]{4,}", m.group(1).lower()) if w not in _TOPIC_STOP]


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def decision_sentence(text: str) -> Optional[str]:
    """The first sentence that reads as a decision the module team cannot make."""
    for s in _SENTENCE.split(text.replace("’", "'")):
        if _DECIDED.search(s):
            return s.strip()
        if _COMMIT_VERB.search(s) and _FIRST_PERSON.search(s) and not _NEGATION.search(s):
            return s.strip()
    return None


def check_email(
    reply: str,
    email: str,
    sources: str,
    refer: bool,
    signature_pattern: str,
    max_words: int,
    open_question: bool = False,
    topic_required: bool = True,
) -> List[Dict[str, Any]]:
    """The nine email rules as checks.

    Returns [{"id", "rule", "ok", "applies", "detail"}, ...]. A check that does
    not apply (e.g. the referral for an information request) counts as passed.
    """
    lines = [l.strip() for l in reply.strip().splitlines() if l.strip()]
    first = lines[0] if lines else ""
    tail = "\n".join(lines[-3:])
    words = len(_WORDS.findall(reply))
    unsupported = sorted(dates_in(reply) - dates_in(sources) - dates_in(email), key=lambda d: (d[1], d[0]))
    decision = decision_sentence(reply)
    lang_email, lang_reply = language(email), language(reply)
    ids = _IDENTIFIER.findall(reply)

    salutation = bool(_SALUTATION.search(first))
    signature = bool(re.search(signature_pattern, tail, re.I))
    closing = bool(_CLOSING[lang_reply].search(tail))
    frame_detail = "; ".join(x for x, ok in (
        ("no salutation in first line: %s" % first[:50], salutation),
        ("no signature in last lines", signature),
        ("no %s closing" % ("German" if lang_reply == "de" else "English"), closing)) if not ok)

    subject_words = topic_words(email)
    # Categories reviewed by a person must not answer the question at all, so
    # requiring a subject word there pushes the model to invent an answer.
    topic_applies = topic_required and bool(subject_words) and not open_question
    low = reply.lower()
    topic_ok = (not topic_applies) or any(w[:max(4, len(w) - 2)] in low for w in subject_words)

    known = _norm(sources + " " + email)
    unquoted = [q.strip() for q in _QUOTE.findall(reply) if _norm(q) not in known]

    def row(i, ok, detail="", applies=True):
        rule = dict((r[0], r[1]) for r in EMAIL_RULES)[i]
        if i == "length":
            rule = "no more than %d words" % max_words
        return {"id": i, "rule": rule, "ok": bool(ok), "applies": applies, "detail": detail}

    return [
        row("frame", salutation and signature and closing, frame_detail),
        row("length", words <= max_words, "%d words" % words),
        row("topic", topic_ok, "" if topic_ok else "none of these subject words in the reply: " +
            ", ".join(subject_words), applies=topic_applies),
        row("dates", not unsupported,
            "not in any source: " + ", ".join("%d %s" % (d, MONTH_NAMES[m]) for d, m in unsupported)
            if unsupported else ""),
        row("quoted", not unquoted, "not in any source: " + ", ".join('"%s"' % q for q in unquoted)
            if unquoted else ""),
        row("decision", decision is None, decision or ""),
        row("referral", (not refer) or _REFER.search(reply), "", applies=refer),
        row("language", lang_email == lang_reply, "email %s, reply %s" % (lang_email, lang_reply)),
        row("identifiers", not ids, ", ".join(ids)),
    ]


def passed(checks: List[Dict[str, Any]]) -> int:
    return sum(1 for c in checks if c["ok"])


def all_passed(checks: List[Dict[str, Any]]) -> bool:
    return all(c["ok"] for c in checks)


def score(checks: List[Dict[str, Any]]) -> str:
    return "%d/%d" % (passed(checks), len(checks))
