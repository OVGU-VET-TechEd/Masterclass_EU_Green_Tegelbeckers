"""Model backends. Standard library only.

Three routes, in order of preference:

  OllamaBackend        native Ollama API on 127.0.0.1:11434
  OpenAICompatBackend  llama.cpp server / LM Studio / vLLM on /v1
  SimulatedBackend     no model at all — deterministic stand-in, labelled as such

The simulated backend exists so the session does not stop when someone's
service is not running. It is never presented as a model. Every result it
produces carries simulated=True and the user interface says so.
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
from typing import Any, Dict, List, Optional

DEFAULT_OLLAMA = os.environ.get("LLMLAB_OLLAMA", "http://127.0.0.1:11434")
DEFAULT_OPENAI = os.environ.get("LLMLAB_OPENAI", "http://127.0.0.1:8080/v1")
DEFAULT_MODEL = os.environ.get("LLMLAB_MODEL", "gemma3:4b")


@dataclass
class Result:
    """One model call, with the numbers the session needs to talk about."""

    text: str
    prompt_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    seconds: float = 0.0
    model: str = ""
    endpoint: str = ""
    simulated: bool = False
    notes: List[str] = field(default_factory=list)
    # Set only by count_prompt_tokens: tokens the chat template added around
    # the text, which the model receives and the user never typed.
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
            "notes": self.notes,
        }
        if self.wrapper_tokens is not None:
            d["wrapper_tokens"] = self.wrapper_tokens
        return d


def _post(url: str, payload: dict, timeout: int = 180) -> dict:
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

    def count_prompt_tokens(self, text: str) -> Result:
        """Token count as the model itself counts it, not an approximation."""
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

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        options: Dict[str, Any] = {"temperature": temperature, "num_predict": max_tokens}
        if seed is not None:
            options["seed"] = seed
        if num_ctx is not None:
            options["num_ctx"] = int(num_ctx)
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": options,
        }
        if system:
            payload["system"] = system
        t0 = time.time()
        try:
            data = _post(self.endpoint + "/api/generate", payload)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            raise RuntimeError("Ollama returned %s: %s" % (e.code, body))
        except Exception as e:
            raise RuntimeError("Could not reach Ollama at %s (%s)" % (self.endpoint, e))
        notes = []
        pt = data.get("prompt_eval_count")
        if not pt:
            notes.append(
                "The server reported no prompt token count for this call. That "
                "normally means it reused a cached copy of an identical prefix. "
                "Change one word and run it again."
            )
        return Result(
            text=(data.get("response") or "").strip(),
            prompt_tokens=pt,
            output_tokens=data.get("eval_count"),
            seconds=time.time() - t0,
            model=self.model,
            endpoint=self.endpoint + "/api/generate",
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
        """The text as the model's tokenizer counts it, and separately what
        the chat template adds around it.

        Ollama's ordinary count includes the template — role markers and, on
        some models, a default system prompt — so on a short sentence more
        than half the number can be wrapper. Raw mode leaves the template
        out; a one-letter probe measures the start marker some tokenizers add
        even then, and that is subtracted too.
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
    """llama.cpp --server, LM Studio, vLLM, or Ollama's own /v1 shim."""

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

    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.0,
        seed: Optional[int] = None,
        num_ctx: Optional[int] = None,
        max_tokens: int = 300,
    ) -> Result:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        }
        if seed is not None:
            payload["seed"] = seed
        t0 = time.time()
        try:
            data = _post(self.endpoint + "/chat/completions", payload)
        except Exception as e:
            raise RuntimeError("Could not reach %s (%s)" % (self.endpoint, e))
        usage = data.get("usage") or {}
        text = ""
        try:
            text = data["choices"][0]["message"]["content"].strip()
        except Exception:
            text = json.dumps(data)[:500]
        notes = []
        if num_ctx:
            notes.append(
                "This route has no per-request context-window control. The window "
                "is whatever the server was started with, so the context lab "
                "measures rather than sets it here."
            )
        return Result(
            text=text,
            prompt_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            seconds=time.time() - t0,
            model=self.model,
            endpoint=self.endpoint + "/chat/completions",
            notes=notes,
        )

    def count_prompt_tokens(self, text: str) -> Result:
        """This route has no raw mode, so the template cannot be separated."""
        r = self.generate(text, temperature=0.0, max_tokens=1)
        r.notes.append(
            "This route cannot count the text without the chat template, so the "
            "number includes the wrapper: role markers and any default system "
            "prompt. On a short sentence that can be more than half of it."
        )
        return r


# --------------------------------------------------------------------------
# Simulated backend
# --------------------------------------------------------------------------

_WORD = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def approx_tokens(text: str) -> List[str]:
    """A deterministic stand-in for subword tokenisation.

    Whitespace and punctuation split, then long words broken every four
    characters. This is an approximation of a byte-pair encoder, not one.
    Real counts come from the model; this exists for the offline path and for
    drawing chips before a call is made.
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


class SimulatedBackend(Backend):
    """No model. Deterministic text derived from the prompt, plus honest labels.

    It reproduces three behaviours the session needs to show:
      * temperature 0 gives the same answer every time; above 0 it does not
      * text beyond the context window is not available to the answer
      * an answer can be fluent and wrong at the same time
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
            # A window keeps the end and drops the start. Cut the text itself
            # rather than the chips, so words are not sliced in half.
            cut = int(len(full) * (1.0 - kept / float(len(toks))))
            window_text = full[cut:]
            truncated = True

        # A code word planted by the context lab survives only inside the window.
        found = re.search(r"CODE WORD is ([A-Z]{3,12})", window_text)
        planted_anywhere = re.search(r"CODE WORD is ([A-Z]{3,12})", prompt)

        salt = "" if temperature <= 0.0 else str(seed if seed is not None else time.time_ns())
        h = hashlib.sha256((prompt + system + salt).encode("utf-8")).hexdigest()
        pick = int(h[:8], 16)

        if planted_anywhere and "code word" in prompt.lower():
            if found:
                text = "The code word is %s." % found.group(1)
            else:
                guesses = ["ANCHOR", "MERIDIAN", "SALTIRE", "PARAPET"]
                text = (
                    "The code word is %s. It appears in the opening section of the "
                    "text you supplied." % guesses[pick % len(guesses)]
                )
        else:
            openers = [
                "There are three points worth separating here.",
                "The short answer is that it depends on what the task is for.",
                "Begin with what the reader has to be able to do afterwards.",
                "Two conditions have to hold before this is worth doing.",
            ]
            middles = [
                "First, name the decision. Second, name who is affected by it. "
                "Third, write down what would change your mind.",
                "Set out the constraint before the method, because the constraint "
                "is what makes one method preferable to another.",
                "Distinguish the part that has to be defensible from the part that "
                "only has to be usable.",
            ]
            closers = [
                "State the limits of this in writing before anyone acts on it.",
                "Whatever you decide, record the date and the reason.",
                "Check the claim above against a source before you use it.",
            ]
            text = " ".join(
                [
                    openers[pick % len(openers)],
                    middles[(pick >> 8) % len(middles)],
                    closers[(pick >> 16) % len(closers)],
                ]
            )

        notes = ["No model was called. This text was assembled by llmlab itself."]
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
# Tag components that mark a variant the labs should not land on by accident:
# a vision/multimodal model inflates prompt-token counts with template
# overhead the tokens lab has no way to know about, and a base (non-instruct)
# model does not reliably follow a system prompt, which is the entire point
# of the steer, ground and ladder labs. An embedding model cannot generate
# text at all, and Ollama lists it alongside the others.
_SKIP = {"vl", "vision", "llava", "base", "pt", "embed"}


def _family(name: str) -> str:
    """'gemma3:12b' -> 'gemma', 'llama3.1:8b' -> 'llama'."""
    m = re.match(r"[a-z]+", name.lower())
    return m.group(0) if m else name.lower()


def _fallback_model(names: List[str], prefer: str = "") -> str:
    """DEFAULT_MODEL is not installed — pick something to run the labs with.

    Prefer a model from the default's own family, because that is what the
    workshop series installed and what the labs were tuned on; a participant
    with gemma:2b or gemma4 should land on it, not on whatever else is
    there. Within that, prefer the smallest instruction-tuned, text-only
    model, sized from a ':<N>b' tag, rather than whichever name the service
    happened to list first. A large model picked at random turns every lab
    into a multi-minute wait; on the machine this was written on, the
    untuned fallback picked a 24B vision model over an 8B text one sitting
    right next to it, and the version before that picked an embedding model
    that cannot generate at all. Falls back to the first name if filtering
    leaves nothing, or to the filtered list's first entry if none of it has
    a parseable size.
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
    """What is reachable, for `llmlab check` and the status bar in the browser."""
    ollama = OllamaBackend.probe()
    openai = OpenAICompatBackend.probe()
    return {
        "ollama": {"endpoint": DEFAULT_OLLAMA, "models": ollama, "up": ollama is not None},
        "openai": {"endpoint": DEFAULT_OPENAI, "models": openai, "up": openai is not None},
        "default_model": DEFAULT_MODEL,
    }
