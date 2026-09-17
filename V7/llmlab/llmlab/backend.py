"""Model backends. Standard library only.

Three routes, in order of preference:

  OllamaBackend        native Ollama API on 127.0.0.1:11434
  OpenAICompatBackend  llama.cpp server / LM Studio / vLLM on /v1
  SimulatedBackend     no model; deterministic text produced by llmlab

The simulated backend allows the exercises to run on a computer without a
model service. Every result it produces carries simulated=True, and the
command line and the browser interface state this with each result.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from .checks import language

DEFAULT_OLLAMA = os.environ.get("LLMLAB_OLLAMA", "http://127.0.0.1:11434")
DEFAULT_OPENAI = os.environ.get("LLMLAB_OPENAI", "http://127.0.0.1:8080/v1")
DEFAULT_MODEL = os.environ.get("LLMLAB_MODEL", "gemma3:4b")


@dataclass
class Result:
    """One model call and the figures reported for it."""

    text: str
    prompt_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    seconds: float = 0.0
    model: str = ""
    endpoint: str = ""
    simulated: bool = False
    notes: List[str] = field(default_factory=list)
    # Set only by count_prompt_tokens: tokens the chat template added around
    # the text. The model receives them; the user does not type them.
    wrapper_tokens: Optional[int] = None

    def as_dict(self) -> Dict[str, Any]:
        d = {
            "text": self.text,
            "prompt_tokens": self.prompt_tokens,
            "output_tokens": self.output_tokens,
            "seconds": round(self.seconds, 2),
            "model": self.model,
            "endpoint": self.endpoint,
            "simulated": self.simulated,
            "notes": list(self.notes),
        }
        if self.wrapper_tokens is not None:
            d["wrapper_tokens"] = self.wrapper_tokens
        return d


def _post(url: str, payload: dict, timeout: int = 300) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def _get(url: str, timeout: int = 5) -> dict:
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


class Backend:
    name = "base"
    simulated = False

    def __init__(self, model: str = DEFAULT_MODEL, endpoint: str = ""):
        self.model = model
        self.endpoint = endpoint

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        raise NotImplementedError

    def request(
        self, prompt: str, system: str = "", temperature: float = 0.0,
        seed: Optional[int] = None, num_ctx: Optional[int] = None, max_tokens: int = 300,
    ) -> Tuple[str, Dict[str, Any]]:
        """The URL and JSON body this backend sends for a call."""
        return "in-process", {"prompt": prompt, "system": system}

    def count_prompt_tokens(self, text: str) -> Result:
        """Token count as reported by the model server."""
        return self.generate(text, temperature=0.0, max_tokens=1)


class OllamaBackend(Backend):
    name = "ollama"

    def __init__(self, model: Optional[str] = None, endpoint: Optional[str] = None):
        super().__init__(model or DEFAULT_MODEL, (endpoint or DEFAULT_OLLAMA).rstrip("/"))

    @staticmethod
    def probe(endpoint: Optional[str] = None) -> Optional[List[str]]:
        """Return the list of installed model names, or None if unreachable."""
        try:
            tags = _get((endpoint or DEFAULT_OLLAMA).rstrip("/") + "/api/tags", timeout=3)
            return [m["name"] for m in tags.get("models", [])]
        except Exception:
            return None

    def request(self, prompt, system="", temperature=0.0, seed=None, num_ctx=None, max_tokens=300):
        options: Dict[str, Any] = {"temperature": temperature, "num_predict": max_tokens}
        if seed is not None:
            options["seed"] = seed
        if num_ctx is not None:
            options["num_ctx"] = int(num_ctx)
        payload: Dict[str, Any] = {"model": self.model, "prompt": prompt, "stream": False,
                                   "options": options}
        if system:
            payload["system"] = system
        return self.endpoint + "/api/generate", payload

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        url, payload = self.request(prompt, system, temperature, seed, num_ctx, max_tokens)
        t0 = time.time()
        try:
            data = _post(url, payload)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            raise RuntimeError("Ollama returned %s: %s" % (e.code, body))
        except Exception as e:
            raise RuntimeError("Could not reach Ollama at %s (%s)" % (self.endpoint, e))
        notes = []
        pt = data.get("prompt_eval_count")
        if not pt:
            notes.append(
                "The server reported no prompt token count for this call. This "
                "usually means it reused a cached copy of an identical prompt prefix."
            )
        return Result(
            text=(data.get("response") or "").strip(),
            prompt_tokens=pt,
            output_tokens=data.get("eval_count"),
            seconds=time.time() - t0,
            model=self.model,
            endpoint=url,
            notes=notes,
        )

    def _raw_count(self, text: str) -> Optional[int]:
        """Prompt tokens for `text` with the chat template switched off."""
        data = _post(
            self.endpoint + "/api/generate",
            {
                "model": self.model,
                "prompt": text,
                "raw": True,
                "stream": False,
                "options": {"temperature": 0.0, "num_predict": 1},
            },
        )
        return data.get("prompt_eval_count")

    def count_prompt_tokens(self, text: str) -> Result:
        """The text as the model's tokenizer counts it, and separately the
        tokens the chat template adds around it.

        Ollama's ordinary count includes the template: role markers and, on
        some models, a default system prompt. Raw mode leaves the template
        out. A one-letter probe measures the start-of-text marker that some
        tokenizers add even in raw mode, and that marker is subtracted.
        """
        templated = self.generate(text, temperature=0.0, max_tokens=1)
        total = templated.prompt_tokens
        try:
            raw, probe = self._raw_count(text), self._raw_count("a")
        except Exception:
            raw = probe = None
        if not (total and raw and probe):
            templated.notes.append(
                "This count includes the chat template. The text alone could not "
                "be counted separately on this call."
            )
            return templated
        text_tokens = max(1, raw - max(0, probe - 1))
        templated.prompt_tokens = text_tokens
        templated.wrapper_tokens = max(0, total - text_tokens)
        return templated


class OpenAICompatBackend(Backend):
    """llama.cpp --server, LM Studio, vLLM, or Ollama's own /v1 interface."""

    name = "openai-compatible"

    def __init__(self, model: Optional[str] = None, endpoint: Optional[str] = None):
        super().__init__(model or DEFAULT_MODEL, (endpoint or DEFAULT_OPENAI).rstrip("/"))

    @staticmethod
    def probe(endpoint: Optional[str] = None) -> Optional[List[str]]:
        try:
            data = _get((endpoint or DEFAULT_OPENAI).rstrip("/") + "/models", timeout=3)
            return [m.get("id", "?") for m in data.get("data", [])]
        except Exception:
            return None

    def request(self, prompt, system="", temperature=0.0, seed=None, num_ctx=None, max_tokens=300):
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload: Dict[str, Any] = {"model": self.model, "messages": messages,
                                   "temperature": temperature, "max_tokens": max_tokens,
                                   "stream": False}
        if seed is not None:
            payload["seed"] = seed
        return self.endpoint + "/chat/completions", payload

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        url, payload = self.request(prompt, system, temperature, seed, num_ctx, max_tokens)
        t0 = time.time()
        try:
            data = _post(url, payload)
        except Exception as e:
            raise RuntimeError("Could not reach %s (%s)" % (self.endpoint, e))
        usage = data.get("usage") or {}
        try:
            text = data["choices"][0]["message"]["content"].strip()
        except Exception:
            text = json.dumps(data)[:500]
        notes = []
        if num_ctx:
            notes.append(
                "This route has no per-request setting for the context window. The "
                "window is the one the server was started with."
            )
        return Result(
            text=text,
            prompt_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            seconds=time.time() - t0,
            model=self.model,
            endpoint=url,
            notes=notes,
        )

    def count_prompt_tokens(self, text: str) -> Result:
        """This route has no raw mode, so the template cannot be separated."""
        r = self.generate(text, temperature=0.0, max_tokens=1)
        r.notes.append(
            "This route cannot count the text without the chat template, so the "
            "number includes role markers and any default system prompt."
        )
        return r


# --------------------------------------------------------------------------
# Simulated backend
# --------------------------------------------------------------------------

_WORD = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def approx_tokens(text: str) -> List[str]:
    """A deterministic approximation of subword tokenisation.

    Splits at whitespace and punctuation, then breaks words longer than five
    characters every four characters. This is not a byte-pair encoder. Actual
    counts come from the model server; this segmentation is used for display
    and for the simulated route.
    """
    out: List[str] = []
    for piece in _WORD.findall(text):
        if len(piece) <= 5 or not piece.isalpha():
            out.append(piece)
        else:
            head, rest = piece[:4], piece[4:]
            out.append(head)
            while rest:
                out.append(rest[:4])
                rest = rest[4:]
    return out


# The fact planted by the context lab and the question that asks for it.
NEEDLE = re.compile(r"by 12:00 on (\d{1,2} [A-Z][a-z]+ \d{4})")
NEEDLE_QUESTION = "by which date must the portfolio be submitted"

_SIM_CATEGORY = (
    ("third_party", r"\b(flatmate|fellow student|friend|on (his|her) behalf)\b"),
    ("extension", r"\b(extend|extension|illness|influenza|ill|sick|doctor|krank)\b"),
    ("grade", r"\b(grade|mark|points|note)\b"),
    ("other", r"\b(sample|interviews?|analysis)\b"),
)


def _simulated_email(prompt: str, system: str) -> str:
    """Stand-in replies for the student-email task.

    A first draft without recorded lessons contains one typical error for its
    category; a revision request or a system prompt with lessons produces a
    reply that passes the checks. This reproduces the structure of stages
    three to five, not the behaviour of any particular model.
    """
    m = re.search(r"Email:\n\n(.*?)(?:\n\n(?:Write the reply|Your draft reply)|\Z)", prompt, re.S)
    email = m.group(1) if m else prompt.replace("Answer this email:", "")
    low = email.lower()
    if "Classify the email" in prompt:
        for label, pattern in _SIM_CATEGORY:
            if re.search(pattern, low):
                return label
        return "information"

    fixed = "did not pass these checks" in prompt or "Lessons recorded from earlier runs" in system
    german = language(email) == "de"
    lines = [l.strip() for l in email.strip().splitlines() if l.strip()]
    sender = lines[-1] if lines else ""
    if sender.lower().startswith("matriculation") and len(lines) > 1:
        sender = lines[-2]
    name = sender.split()[0] if sender and len(sender.split()) <= 3 else ""

    if re.search(_SIM_CATEGORY[0][1], low):
        body = ("we cannot give any information about other students. Each student "
                "must contact the module team personally.")
    elif re.search(_SIM_CATEGORY[1][1], low):
        body = ("thank you for letting us know. Extensions are decided by the "
                "examination office (pruefungsamt@example.edu), not by the module team. "
                "Please send your application with the medical certificate before the "
                "deadline on 15 January 2027." if fixed else
                "thank you for letting us know, and get well soon. We will extend your "
                "portfolio deadline by one week, to 22 January 2027. Please send us the "
                "medical certificate.")
    elif re.search(_SIM_CATEGORY[2][1], low):
        body = ("the module team does not discuss grades by email. You can inspect your "
                "examination in the review session on 5 March 2027, 13:00-15:00, room "
                "G40-212. Requests to change a grade go in writing to the examination "
                "office (pruefungsamt@example.edu)." if fixed else
                "we have looked at question 4 again and we will raise your grade to 3.0.")
    elif re.search(_SIM_CATEGORY[3][1], low):
        subj = re.search(r"^(?:Subject|Betreff):\s*(.+)$", email, re.M)
        body = ("thank you for your email%s. A member of the module team will reply to "
                "your question personally." % (' "%s"' % subj.group(1).strip() if subj else ""))
    elif "slides" in low:
        body = ("the slides for each session are uploaded to the learning platform by "
                "18:00 on the day before the session." if "slides for each session" in system
                else "The module team will confirm this separately.")
    elif german:
        body = ("die Literaturliste finden Sie auf der Lernplattform im Kurs \"EDU-204 "
                "2026/27\" im Ordner \"Week 0\". Die Sprechstunde ist dienstags von 14:00 "
                "bis 15:30 Uhr in Raum G40-212.")
        if not fixed:
            german = False
            body = ("the reading list is in the folder \"Week 0\" on the learning platform. "
                    "Office hours are on Tuesdays, 14:00-15:30, room G40-212.")
    else:
        body = ("the written examination takes place on 9 February 2027, 10:00-12:00, in "
                "lecture hall H3. Registration in the campus portal is required and closes "
                "on 12 December 2026.")
        if not fixed:
            return "Dear %s,\n\n%s" % (name or "student", body)

    if german:
        return "Guten Tag%s,\n\n%s\n\nMit freundlichen Grüßen\nEDU-204 module team" % (
            " " + sender if sender else "", body)
    return "Dear %s,\n\n%s\n\nKind regards,\nEDU-204 module team" % (name or "student", body)


class SimulatedBackend(Backend):
    """No model. Deterministic text derived from the prompt, labelled as such.

    It reproduces the structural behaviour the exercises examine:
      * temperature 0 gives the same answer every time; above 0 it does not
      * text beyond the context window is not available to the answer
      * a stored instruction, a revision request or recorded lessons change
        the reply in the student-email task
    """

    name = "simulated"
    simulated = True

    def __init__(self, model: str = "simulated", endpoint: str = "in-process"):
        super().__init__(model, endpoint)

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        t0 = time.time()
        full = (system + "\n" + prompt) if system else prompt
        toks = approx_tokens(full)
        kept = len(toks)
        truncated = False
        window_text = full
        if num_ctx and len(toks) > int(num_ctx):
            kept = int(num_ctx)
            # The window keeps the end and drops the start. The text is cut by
            # characters so that words are not split.
            cut = int(len(full) * (1.0 - kept / float(len(toks))))
            window_text = full[cut:]
            truncated = True

        salt = "" if temperature <= 0.0 else str(seed if seed is not None else time.time_ns())
        h = hashlib.sha256((prompt + system + salt).encode("utf-8")).hexdigest()
        pick = int(h[:8], 16)

        if NEEDLE_QUESTION in prompt.lower():
            found = NEEDLE.search(window_text)
            if found:
                text = found.group(1)
            else:
                text = ["31 January 2027", "15 February 2027", "1 March 2027"][pick % 3]
        elif ("Classify the email" in prompt or "Write the reply" in prompt
              or "did not pass these checks" in prompt or prompt.startswith("Answer this email:")
              or "EDU-204" in system):
            text = _simulated_email(prompt, system)
        else:
            openers = [
                "There are three points to separate here.",
                "The answer depends on what the task is for.",
                "Begin with what the reader has to be able to do afterwards.",
                "Two conditions have to hold before this is worth doing.",
            ]
            middles = [
                "First, name the decision. Second, name who is affected by it. "
                "Third, write down what would change the assessment.",
                "Set out the constraint before the method, because the constraint "
                "determines which method is preferable.",
                "Distinguish the part that has to be defensible from the part that "
                "only has to be usable.",
            ]
            closers = [
                "State the limits of this in writing before anyone acts on it.",
                "Record the date and the reason for the decision.",
                "Check the claim above against a source before using it.",
            ]
            text = " ".join(
                [
                    openers[pick % len(openers)],
                    middles[(pick >> 8) % len(middles)],
                    closers[(pick >> 16) % len(closers)],
                ]
            )

        notes = ["Simulated: no model was called. llmlab produced this text."]
        if truncated:
            notes.append(
                "%d of %d tokens fell outside the %d-token window and were not "
                "available to the answer." % (len(toks) - kept, len(toks), int(num_ctx))
            )
        return Result(
            text=text,
            prompt_tokens=len(toks),
            output_tokens=len(approx_tokens(text)),
            seconds=time.time() - t0,
            model="simulated",
            endpoint="in-process (nothing left this machine)",
            simulated=True,
            notes=notes,
        )


# --------------------------------------------------------------------------
# Selection
# --------------------------------------------------------------------------

_SIZE_RE = re.compile(r"(\d+(?:\.\d+)?)b\b", re.IGNORECASE)
_TOKEN_RE = re.compile(r"[a-z0-9.]+")
# Tag components that mark variants the labs should not select by default:
# vision models add template overhead that distorts token counts, base
# (non-instruction-tuned) models do not reliably follow a system prompt, and
# embedding models cannot generate text.
_SKIP = {"vl", "vision", "llava", "base", "pt", "embed"}


def _family(name: str) -> str:
    """'gemma3:12b' -> 'gemma', 'llama3.1:8b' -> 'llama'."""
    m = re.match(r"[a-z]+", name.lower())
    return m.group(0) if m else name.lower()


def _fallback_model(names: List[str], prefer: str = "") -> str:
    """Choose a model when DEFAULT_MODEL is not installed.

    Prefers the default model's family, then the smallest instruction-tuned
    text model, sized from a ':<N>b' tag. Falls back to the first name if
    filtering leaves nothing, or to the first filtered name if none has a
    parseable size.
    """
    plain = [n for n in names if not (set(_TOKEN_RE.findall(n.lower())) & _SKIP)] or names
    pool = [n for n in plain if prefer and _family(n) == _family(prefer)] or plain
    sized = [(n, float(m.group(1))) for n in pool for m in [_SIZE_RE.search(n)] if m]
    return min(sized, key=lambda t: t[1])[0] if sized else pool[0]


def detect(model: Optional[str] = None, prefer: str = "auto") -> Backend:
    """Pick a backend. Order: Ollama, OpenAI-compatible, simulated."""
    model = model or DEFAULT_MODEL
    if prefer == "simulated":
        return SimulatedBackend()
    if prefer in ("auto", "ollama"):
        names = OllamaBackend.probe()
        if names is not None:
            chosen = model if model in names else (_fallback_model(names, model) if names else model)
            return OllamaBackend(chosen)
        if prefer == "ollama":
            raise RuntimeError("No Ollama service at %s." % DEFAULT_OLLAMA)
    if prefer in ("auto", "openai"):
        names = OpenAICompatBackend.probe()
        if names is not None:
            chosen = model if model in names else (_fallback_model(names, model) if names else model)
            return OpenAICompatBackend(chosen)
        if prefer == "openai":
            raise RuntimeError("No OpenAI-compatible server at %s." % DEFAULT_OPENAI)
    return SimulatedBackend()


def survey() -> Dict[str, Any]:
    """What is reachable, for `llmlab check` and the browser interface."""
    ollama = OllamaBackend.probe()
    openai = OpenAICompatBackend.probe()
    return {
        "ollama": {"endpoint": DEFAULT_OLLAMA, "models": ollama, "up": ollama is not None},
        "openai": {"endpoint": DEFAULT_OPENAI, "models": openai, "up": openai is not None},
        "default_model": DEFAULT_MODEL,
    }
