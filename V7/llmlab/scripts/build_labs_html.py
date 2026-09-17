"""Build masterclass_ai_in_teaching_v6_labs.html from saved lab results.

Run from the folder V6/llmlab after producing results, for example:

    python scripts/run_all_labs.py --model gemma3:12b --out-dir results/gemma3-12b
    python scripts/lab6_ladder.py --model gemma3:12b --set emails=7 --out results/gemma3-12b/lab6_ladder.json
    python scripts/build_labs_html.py --results results/gemma3-12b

The script copies ../masterclass_ai_in_teaching_v6.html, embeds the JSON
results and adds an interactive result panel below each lab description.
Simulated results are refused unless --allow-simulated is given, because the
page states that its outputs come from a model.
"""

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
V6 = ROOT.parent

LAB_FILES = {"tokens": "lab1_tokens.json", "context": "lab2_context.json", "vary": "lab3_vary.json",
             "steer": "lab4_steer.json", "ground": "lab5_ground.json", "ladder": "lab6_ladder.json",
             "route": "lab7_route.json"}

# Where the result panels go: after the lab description box whose badge matches.
ANCHORS = [
    ('<span class="badge">Lab 5</span>', ["ground"]),
    ('<span class="badge">Lab 7</span>', ["route"]),
    ('<span class="badge">Labs 1–3</span>', ["tokens", "context", "vary"]),
    ('<span class="badge">Labs 4 &amp; 6</span>', ["steer", "ladder"]),
]

CSS = r"""
/* ---------- v6 labs: result panels ---------- */
.res{border:1px solid var(--green);border-left:5px solid var(--green);border-radius:0 11px 11px 0;
     background:#fff;margin:14px 0 22px;max-width:100%}
.res>.rhd{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:11px 15px;
          background:linear-gradient(100deg,var(--green-s),#fff 75%);border-bottom:1px solid var(--line)}
.res .rt{font-weight:680;color:#14513e;font-size:.95rem}
.res .pillm{font-size:.7rem;border-radius:999px;padding:2px 9px;border:1px solid var(--line);background:#fff;color:var(--dim)}
.res .pillm.real{border-color:var(--green);color:#14513e;background:var(--green-s);font-weight:700}
.res .pillm.sim{border-color:var(--red);color:#6d2a1e;background:var(--red-s);font-weight:700}
.res .rbody{padding:12px 15px}
.res .q{margin:0 0 10px;font-size:.88rem;color:var(--ink);font-weight:600;max-width:100%}
.res .m{font-size:.74rem;color:var(--mute);margin:3px 0}
.res p{max-width:100%}
.reveal{background:var(--violet);color:#fff;border:0;border-radius:7px;padding:7px 13px;font:inherit;
        font-size:.8rem;font-weight:650;cursor:pointer;min-height:36px}
.reveal:hover{background:#56397f}
.reveal.ghost{background:#fff;color:var(--violet);border:1px solid var(--violet-m)}
.hiddenpart{display:none}.hiddenpart.on{display:block;animation:fade .25s ease}
@keyframes fade{from{opacity:0;transform:translateY(-3px)}to{opacity:1;transform:none}}
.cols{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin:10px 0}
.outbox{border:1px solid var(--line);border-radius:9px;background:#fbfcfe;padding:9px 11px;min-width:0}
.outbox h5{margin:0 0 4px;font-size:.78rem;color:var(--blue);text-transform:none}
.outbox .m{font-size:.7rem;color:var(--mute);margin-bottom:5px}
.outbox pre,.res pre{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Consolas,monospace;
     font-size:.76rem;line-height:1.45;background:var(--sunk);border-radius:6px;padding:8px 10px;margin:4px 0;
     max-height:340px;overflow:auto}
.modelout{white-space:pre-wrap;font-size:.84rem;color:var(--ink);border-left:3px solid var(--green);
          padding:5px 0 5px 10px;margin:4px 0;background:#fff}
.ok{color:var(--green);font-weight:650}.no{color:var(--red);font-weight:650}.na{color:var(--mute)}
.chk{list-style:none;margin:6px 0 0;padding:0;font-size:.76rem}
.chk li{padding:1px 0}
.tabs{display:flex;flex-wrap:wrap;gap:4px;margin:6px 0 0;border-bottom:2px solid var(--line)}
.tab{background:var(--sunk);border:1px solid var(--line);border-bottom:0;border-radius:7px 7px 0 0;
     padding:6px 11px;font:inherit;font-size:.78rem;color:var(--dim);cursor:pointer}
.tab[aria-selected="true"]{background:#fff;color:var(--blue);font-weight:700;border-color:var(--blue-m);
     box-shadow:0 2px 0 #fff}
.tabpanel{border:1px solid var(--line);border-top:0;border-radius:0 0 8px 8px;padding:10px 12px;background:#fff}
.sel{font:inherit;font-size:.82rem;border:1px solid var(--blue-m);border-radius:7px;padding:6px 9px;background:#fff;max-width:100%}
.bars{margin:8px 0}
.bar2{display:grid;grid-template-columns:150px 1fr 60px;gap:8px;align-items:center;font-size:.76rem;margin:3px 0}
.bar2 .track{background:var(--sunk);border-radius:999px;height:12px;overflow:hidden;border:1px solid var(--line)}
.bar2 .fill{height:100%;background:var(--blue);border-radius:999px;transition:width .5s ease}
.bar2 .fill.alt{background:var(--violet)}.bar2 .fill.good{background:var(--green)}.bar2 .fill.bad{background:var(--red)}
.interp{border-left:4px solid var(--green);background:var(--green-s);border-radius:0 7px 7px 0;
        padding:9px 12px;margin-top:10px;font-size:.84rem;color:#14513e}
.chips2{display:flex;flex-wrap:wrap;gap:3px;margin:6px 0}
.chips2 span{font-family:ui-monospace,Consolas,monospace;font-size:.7rem;padding:1px 5px;border-radius:4px;
            background:var(--blue-s);border:1px solid var(--blue-m);color:#1d3557}
.chips2 span:nth-child(even){background:var(--violet-s);border-color:var(--violet-m);color:#4b3573}
.rtable{width:100%;border-collapse:collapse;font-size:.76rem;min-width:520px}
.rtable th,.rtable td{border:1px solid var(--line);padding:5px 7px;vertical-align:top;text-align:left}
.rtable th{background:var(--sunk);color:var(--blue)}
.rtable td.ready{color:var(--green);font-weight:700}.rtable td.review{color:var(--amber);font-weight:700}
.rtable tr.pick{cursor:pointer}.rtable tr.pick:hover td{background:var(--blue-s)}
.step{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:8px 0}
.roundlbl{font-size:.76rem;color:var(--mute)}
mark.hl{background:#fff1b8;padding:0 2px;border-radius:3px}
.same{outline:2px solid var(--green);outline-offset:-2px}
.flow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:.74rem;margin:6px 0}
.flow span{border:1px solid var(--line);border-radius:6px;padding:3px 8px;background:#fff}
.flow span.on{border-color:var(--violet);background:var(--violet-s);color:#4b3573;font-weight:700}
.flow i{color:var(--mute);font-style:normal}
.ob{display:flex;gap:8px;align-items:flex-start;font-size:.8rem;margin:5px 0;padding:6px 8px;border:1px solid var(--line);border-radius:7px;background:#fff}
.ob input{margin-top:3px}
.ob .ans{display:none;color:var(--dim)}.ob .ans.on{display:inline}
.resnav{border:1px solid var(--green);border-radius:10px;background:var(--green-s);padding:11px 15px;margin:14px 0;font-size:.86rem;color:#14513e;max-width:74ch}
.resnav a{color:#14513e;font-weight:650;margin-right:10px}
"""

JS = r"""
(function(){
  "use strict";
  var DATA = JSON.parse(document.getElementById("labdata").textContent);
  var META = DATA.meta;

  function el(tag, attrs){
    var n = document.createElement(tag);
    for (var k in (attrs||{})){
      if (k === "class") n.className = attrs[k];
      else if (k === "text") n.textContent = attrs[k];
      else if (k.slice(0,2) === "on") n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k]);
    }
    function add(c){
      if (c == null) return;
      if (Array.isArray(c)) { c.forEach(add); return; }
      n.appendChild(c.nodeType ? c : document.createTextNode(String(c)));
    }
    for (var i = 2; i < arguments.length; i++) add(arguments[i]);
    return n;
  }
  function fill(node){
    var kids = [];
    (function flat(c){ if (c == null) return; if (Array.isArray(c)) c.forEach(flat); else kids.push(c); })(Array.prototype.slice.call(arguments, 1));
    node.replaceChildren.apply(node, kids);
  }
  function pre(t){ return el("pre", {text: t || ""}); }
  function det(label, content, open){
    var d = el("details", {class: "more"}, el("summary", {text: label}), el("div", {class: "mbody"}, content));
    if (open) d.open = true;
    return d;
  }
  function out(t){ return el("div", {class: "modelout", text: t || "(empty)"}); }
  function checks(list){
    return el("ul", {class: "chk"}, (list||[]).map(function(c){
      var na = c.applies === false;
      return el("li", {class: na ? "na" : (c.ok ? "ok" : "no")},
        (na ? "○ not required: " : (c.ok ? "✓ " : "✗ ")) + c.rule + (!c.ok && c.detail ? " — " + c.detail : ""));
    }));
  }
  function score(list){ var p = 0; (list||[]).forEach(function(c){ if (c.ok) p++; }); return p + "/" + (list||[]).length; }
  function bar(label, value, max, cls, suffix){
    var pct = max ? Math.min(100, 100 * value / max) : 0;
    var f = el("div", {class: "fill " + (cls||"")});
    f.style.width = pct.toFixed(1) + "%";
    return el("div", {class: "bar2"}, el("span", {text: label}), el("div", {class: "track"}, f), el("span", {text: String(value) + (suffix||"")}));
  }
  function revealBlock(question, buttonText, content){
    var hidden = el("div", {class: "hiddenpart"}, content);
    var btn = el("button", {class: "reveal", type: "button", onclick: function(){
      var on = hidden.classList.toggle("on");
      btn.textContent = on ? "Hide" : buttonText;
      btn.classList.toggle("ghost", on);
    }}, buttonText);
    return el("div", {}, el("p", {class: "q", text: question}), btn, hidden);
  }
  function tabs(items){
    var bar_ = el("div", {class: "tabs", role: "tablist"});
    var panel = el("div", {class: "tabpanel"});
    var buttons = items.map(function(it, i){
      var b = el("button", {class: "tab", type: "button", role: "tab", "aria-selected": i === 0 ? "true" : "false",
        onclick: function(){
          buttons.forEach(function(x){ x.setAttribute("aria-selected", "false"); });
          b.setAttribute("aria-selected", "true");
          panel.replaceChildren(it.render());
        }}, it.label);
      bar_.appendChild(b);
      return b;
    });
    panel.appendChild(items[0].render());
    return el("div", {}, bar_, panel);
  }
  function mark(text, needle){
    var span = el("div", {class: "modelout"});
    if (!needle || !text || text.indexOf(needle) < 0){ span.textContent = text || ""; return span; }
    text.split(needle).forEach(function(part, i, arr){
      span.appendChild(document.createTextNode(part));
      if (i < arr.length - 1) span.appendChild(el("mark", {class: "hl", text: needle}));
    });
    return span;
  }
  function frame(res, title, body){
    var sim = res.simulated;
    return el("div", {class: "res", id: "res-" + res.lab},
      el("div", {class: "rhd"},
        el("span", {class: "rt", text: "Results · " + title}),
        el("span", {class: "pillm " + (sim ? "sim" : "real"), text: sim ? "SIMULATED — no model output" : "model output"}),
        el("span", {class: "pillm", text: META.model}),
        el("span", {class: "pillm", text: META.date}),
        el("span", {class: "pillm", text: "llmlab " + META.version})),
      el("div", {class: "rbody"}, body,
        det("Interpretation (composed from the measured values)", el("div", {class: "interp", text: res.reading}), true),
        det("Materials sent to the model", (res.materials||[]).map(function(m){ return el("div", {}, el("b", {text: m.label}), pre(m.text)); }))));
  }

  var R = {};

  R.tokens = function(res){
    var runs = res.runs;
    var main = runs[0];
    var body = [];
    body.push(revealBlock("How many tokens does the model count for the two sentences together, and how many does the chat template add?",
      "Show the counts", el("div", {class: "bars"},
        bar("text tokens", main.prompt_tokens || 0, (main.prompt_tokens||0) + (main.wrapper_tokens||0)),
        bar("template tokens", main.wrapper_tokens || 0, (main.prompt_tokens||0) + (main.wrapper_tokens||0), "alt"),
        el("div", {class: "m", text: main.text ? "" : ""}))));
    if (runs.length >= 3){
      var en = runs[1], de = runs[2];
      var max = Math.max(en.prompt_tokens||0, de.prompt_tokens||0);
      body.push(revealBlock("Which sentence needs more tokens: the English or the German one?", "Compare",
        el("div", {},
          el("div", {class: "bars"}, bar("English", en.prompt_tokens||0, max), bar("German", de.prompt_tokens||0, max, "alt")),
          el("div", {class: "cols"},
            el("div", {class: "outbox"}, el("h5", {text: "English: " + en.prompt}), el("div", {class: "m", text: "approximate segmentation (local, not the tokenizer)"}),
              el("div", {class: "chips2"}, (en.chips||[]).map(function(c){ return el("span", {text: c}); }))),
            el("div", {class: "outbox"}, el("h5", {text: "German: " + de.prompt}), el("div", {class: "m", text: "approximate segmentation (local, not the tokenizer)"}),
              el("div", {class: "chips2"}, (de.chips||[]).map(function(c){ return el("span", {text: c}); })))))));
    }
    return frame(res, "Lab 1 · Tokens", body);
  };

  R.context = function(res){
    var w = res.runs[0], n = res.runs[1];
    var body = [];
    body.push(el("div", {class: "bars"},
      el("div", {class: "m", text: "Prompt length reported by the server for the wide run, and the two window sizes:"}),
      bar("prompt (tokens)", w.prompt_tokens||0, Math.max(w.prompt_tokens||0, 8192)),
      bar("wide window", w.window, Math.max(w.prompt_tokens||0, 8192), "good"),
      bar("narrow window", n.window, Math.max(w.prompt_tokens||0, 8192), "bad")));
    body.push(revealBlock("§ 1 states the deadline 15 January 2027. What does the model answer when only the last " + n.window + " tokens of the prompt fit into the window?",
      "Show both answers",
      el("div", {class: "cols"},
        el("div", {class: "outbox"}, el("h5", {text: w.label}), el("div", {class: "m", text: "tokens processed: " + w.prompt_tokens + " · " + (w.correct ? "date found" : "date not found")}), mark(w.text, "15 January 2027"), el("div", {class: w.correct ? "ok" : "no", text: w.correct ? "✓ correct" : "✗ incorrect"})),
        el("div", {class: "outbox"}, el("h5", {text: n.label}), el("div", {class: "m", text: "tokens processed: " + n.prompt_tokens + " · " + (n.correct ? "date found" : "date not found")}), mark(n.text, "15 January 2027"), el("div", {class: n.correct ? "ok" : "no", text: n.correct ? "✓ correct" : "✗ incorrect"})))));
    body.push(det("Full prompt as sent (identical in both runs)", pre(w.prompt)));
    return frame(res, "Lab 2 · Context window", body);
  };

  R.vary = function(res){
    var groups = {};
    res.runs.forEach(function(r){ var k = r.label.split(" · ")[1]; (groups[k] = groups[k] || []).push(r); });
    var keys = Object.keys(groups);
    var list = el("div", {});
    var select = el("select", {class: "sel", onchange: function(){ show(select.value); }},
      keys.map(function(k){ return el("option", {value: k, text: k}); }));
    function show(k){
      var rs = groups[k];
      var distinct = {};
      rs.forEach(function(r){ distinct[r.text] = (distinct[r.text]||0) + 1; });
      fill(list,
        el("p", {class: "q", text: rs.length + " requests · " + Object.keys(distinct).length + " distinct output" + (Object.keys(distinct).length === 1 ? "" : "s")}),
        rs.map(function(r, i){
          var dup = distinct[r.text] > 1;
          return el("div", {class: "outbox" + (dup ? " same" : ""), style: "margin:6px 0"},
            el("h5", {text: "Request " + (i+1) + (dup ? " · identical to another request" : " · unique")}), out(r.text));
        }));
    }
    show(keys[0]);
    var body = [
      el("div", {class: "outbox"}, el("h5", {text: "Prompt (identical in all requests)"}), pre(res.runs[0].prompt)),
      el("p", {class: "q", style: "margin-top:10px", text: "Select a setting. Outputs with a green frame are character-identical to at least one other output."}),
      select, list];
    return frame(res, "Lab 3 · Temperature and seed", body);
  };

  R.steer = function(res){
    var body = [];
    body.push(el("div", {class: "bars"}, res.runs.map(function(r){
      var p = r.checks.filter(function(c){ return c.ok; }).length;
      return bar(r.label.split(" · ")[0] + " · rules met", p, r.checks.length, p === r.checks.length ? "good" : "", "/" + r.checks.length);
    })));
    body.push(tabs(res.runs.map(function(r){
      return {label: r.label, render: function(){
        return el("div", {},
          r.system ? el("div", {}, el("b", {text: "System prompt"}), pre(r.system)) : el("div", {class: "m", text: "No system prompt."}),
          el("b", {text: "User message"}), pre(r.prompt),
          el("b", {text: "Model output"}), out(r.text),
          checks(r.checks));
      }};
    })));
    return frame(res, "Lab 4 · Rules in the request or in the system prompt", body);
  };

  R.ground = function(res){
    var a = res.runs[0], b = res.runs[1];
    var hl = false;
    var colA = el("div", {}), colB = el("div", {});
    function draw(){
      colA.replaceChildren(hl ? mark(a.text, "2027") : out(a.text));
      colB.replaceChildren(hl ? mark(b.text, "2027") : out(b.text));
    }
    draw();
    var btn = el("button", {class: "reveal ghost", type: "button", onclick: function(){ hl = !hl; draw(); btn.textContent = hl ? "Remove highlighting" : "Highlight the year 2027"; }}, "Highlight the year 2027");
    var body = [
      revealBlock("Can the answer generated with the source be distinguished from the answer without it by reading alone? Read both before the source is shown.",
        "Show both answers",
        el("div", {},
          el("div", {class: "cols"},
            el("div", {class: "outbox"}, el("h5", {text: "Answer X"}), colA),
            el("div", {class: "outbox"}, el("h5", {text: "Answer Y"}), colB)),
          btn, " ",
          revealBlock("Which answer had the source in its prompt?", "Show which is which",
            el("div", {},
              el("p", {text: "Answer X: " + a.label + (a.declined ? " (declined to answer)" : "") + ". Answer Y: " + b.label + "."}),
              det("Prompt of answer X", pre(a.prompt)), det("Prompt of answer Y", pre(b.prompt))))))];
    return frame(res, "Lab 5 · Grounding", body);
  };

  R.route = function(res){
    var r = res.runs[0];
    var body = [
      el("div", {class: "outbox"}, el("h5", {text: "Active route"}), pre(r.text)),
      el("p", {class: "q", style: "margin-top:10px", text: "Which obligations does this route remove? Mark your assessment, then show the answer for each item."}),
      (r.notes||[]).map(function(n){
        var removed = /no transfer to a processor/.test(n);
        var ans = el("span", {class: "ans", text: removed ? " → Partly removed: no processor agreement needed; a lawful basis is still required." : " → Not removed: applies on every route."});
        return el("label", {class: "ob"}, el("input", {type: "checkbox", onchange: function(){ ans.classList.add("on"); }}), el("span", {}, n, ans));
      })];
    return frame(res, "Lab 7 · Deployment route", body);
  };

  R.ladder = function(res){
    var runs = res.runs;
    var names = ["prompt", "skill", "harness", "loop", "wiki"];
    var flow = el("div", {class: "flow"});
    function drawFlow(i){
      flow.replaceChildren();
      ["1 Prompt", "2 Skill prompt", "3 Harness", "4 Loop", "5 Wiki"].forEach(function(s, j){
        if (j) flow.appendChild(el("i", {text: "→"}));
        flow.appendChild(el("span", {class: j === i ? "on" : "", text: s}));
      });
    }
    function singleStage(r){
      return el("div", {},
        el("p", {class: "q", text: "Artefact: " + (r.artefact||"")}),
        r.system ? det("System prompt as sent", pre(r.system)) : el("div", {class: "m", text: "No system prompt."}),
        det("User message as sent", pre(r.prompt), true),
        revealBlock("Which of the nine checks does the reply pass?", "Show the model's reply and the checks",
          el("div", {}, out(r.text), checks(r.checks))),
        (r.notes||[]).filter(function(n){ return !/Simulated/.test(n); }).map(function(n){ return el("div", {class: "m", text: n}); }));
    }
    function multiStage(r, idx){
      var wrap = el("div", {});
      var detail = el("div", {});
      var itemsByName = {};
      (r.items||[]).forEach(function(it){ itemsByName[it.label.split(" · ")[0]] = it; });
      var cols = r.table.columns;
      var tbl = el("table", {class: "rtable"},
        el("thead", {}, el("tr", {}, cols.map(function(c){ return el("th", {text: c}); }))),
        el("tbody", {}, r.table.rows.map(function(row){
          return el("tr", {class: "pick", title: "show this email", onclick: function(){ select.value = row[0]; showItem(row[0]); }},
            row.map(function(c){ var s = String(c); return el("td", {class: (s === "ready" || s === "review") ? s : "", text: s}); }));
        })));
      var select = el("select", {class: "sel", onchange: function(){ showItem(select.value); }},
        r.table.rows.map(function(row){ return el("option", {value: row[0], text: row[0]}); }));
      function showItem(name){
        var it = itemsByName[name];
        if (!it){ detail.replaceChildren(); return; }
        var blocks = it.blocks;
        var email = blocks[0];
        var rest = blocks.slice(1);
        var prompts = rest.filter(function(b){ return /prompt/.test(b.label); });
        var answers = rest.filter(function(b){ return !/prompt/.test(b.label); });
        var pos = 0;
        var stepBox = el("div", {});
        var lbl = el("span", {class: "roundlbl"});
        function drawStep(){
          var b = answers[pos];
          lbl.textContent = "step " + (pos+1) + " of " + answers.length;
          stepBox.replaceChildren(el("b", {text: b.label}), /model answer/.test(b.label) ? pre(b.text) : out(b.text));
          prev.disabled = pos === 0; next.disabled = pos === answers.length - 1;
        }
        var prev = el("button", {class: "reveal ghost", type: "button", onclick: function(){ if (pos > 0){ pos--; drawStep(); } }}, "◀ previous");
        var next = el("button", {class: "reveal", type: "button", onclick: function(){ if (pos < answers.length - 1){ pos++; drawStep(); } }}, "next ▶");
        drawStep();
        detail.replaceChildren(
          el("div", {class: "cols"},
            el("div", {class: "outbox"}, el("h5", {text: "Email " + name}), pre(email.text)),
            el("div", {class: "outbox"}, el("h5", {text: "Model output, step by step"}), el("div", {class: "step"}, prev, next, lbl), stepBox)),
          el("b", {text: "Final checks (" + score(it.checks) + ")"}), checks(it.checks),
          det("Prompts sent for this email (" + prompts.length + ")", prompts.map(function(p){ return el("div", {}, el("b", {text: p.label}), pre(p.text)); })));
      }
      showItem(r.table.rows[0][0]);
      wrap.appendChild(el("p", {class: "q", text: r.text || ""}));
      wrap.appendChild(el("p", {class: "m", text: "Artefact: " + (r.artefact||"")}));
      wrap.appendChild(el("div", {style: "overflow-x:auto"}, tbl));
      wrap.appendChild(el("p", {class: "q", style: "margin-top:10px", text: "Select an email (or click a row) to follow classification, draft and revisions:"}));
      wrap.appendChild(select);
      wrap.appendChild(detail);
      (r.files||[]).forEach(function(f){ wrap.appendChild(det(f.name, pre(f.text))); });
      if (r.system) wrap.appendChild(det("System prompt used at this stage", pre(r.system)));
      (r.notes||[]).filter(function(n){ return !/Simulated/.test(n); }).forEach(function(n){ wrap.appendChild(el("div", {class: "m", text: n})); });
      return wrap;
    }
    var stageBox = el("div", {});
    var stageSel = el("div", {class: "tabs", role: "tablist"});
    var btns = runs.map(function(r, i){
      var b = el("button", {class: "tab", type: "button", role: "tab", "aria-selected": i === 0 ? "true" : "false", onclick: function(){
        btns.forEach(function(x){ x.setAttribute("aria-selected", "false"); });
        b.setAttribute("aria-selected", "true");
        drawFlow(i);
        stageBox.replaceChildren(r.items ? multiStage(r, i) : singleStage(r));
      }}, r.label);
      stageSel.appendChild(b);
      return b;
    });
    drawFlow(0);
    stageBox.appendChild(runs[0].items ? multiStage(runs[0], 0) : singleStage(runs[0]));
    return frame(res, "Lab 6 · Five stages of prompting (student emails)", [flow, stageSel, el("div", {class: "tabpanel"}, stageBox)]);
  };

  document.querySelectorAll("[data-labres]").forEach(function(slot){
    var name = slot.getAttribute("data-labres");
    var res = DATA.labs[name];
    if (!res){ slot.appendChild(el("div", {class: "panel warn", text: "No saved result for lab '" + name + "'."})); return; }
    try { slot.appendChild(R[name](res)); }
    catch (e) { slot.appendChild(el("div", {class: "panel warn", text: "Result for lab '" + name + "' could not be displayed: " + e})); }
  });
})();
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the labs version of the masterclass page from saved results.")
    ap.add_argument("--results", default="results/gemma3-12b", help="folder with lab1_tokens.json ... lab7_route.json")
    ap.add_argument("--source", default=str(V6 / "masterclass_ai_in_teaching_v6.html"))
    ap.add_argument("--target", default=str(V6 / "masterclass_ai_in_teaching_v6_labs.html"))
    ap.add_argument("--allow-simulated", action="store_true")
    args = ap.parse_args()

    folder = pathlib.Path(args.results)
    labs, missing = {}, []
    for name, fn in LAB_FILES.items():
        p = folder / fn
        if not p.exists():
            missing.append(fn)
            continue
        labs[name] = json.loads(p.read_text(encoding="utf-8"))
    if missing:
        print("missing result files in %s: %s" % (folder, ", ".join(missing)), file=sys.stderr)
        return 1
    simulated = [n for n, r in labs.items() if r.get("simulated")]
    if simulated and not args.allow_simulated:
        print("simulated results for: %s. Run the labs with a model service, or pass --allow-simulated."
              % ", ".join(simulated), file=sys.stderr)
        return 1

    models = sorted({run.get("model") for r in labs.values() for run in r["runs"] if run.get("model")} - {""})
    mtime = max((folder / fn).stat().st_mtime for fn in LAB_FILES.values())
    import datetime
    meta = {"model": ", ".join(models) or "unknown",
            "date": datetime.datetime.fromtimestamp(mtime).strftime("%d %B %Y"),
            "version": __import__("llmlab").__version__ if str(ROOT) in sys.path else "2.0.0"}
    data = json.dumps({"meta": meta, "labs": labs}, ensure_ascii=False).replace("</", "<\\/")

    h = pathlib.Path(args.source).read_text(encoding="utf-8")
    h = h.replace("</style>", CSS + "\n</style>", 1)
    h = h.replace("<title>AI in Teaching — Tools, Strategies and Reflection · EU GREEN Masterclass</title>",
                  "<title>AI in Teaching — Lab Results · EU GREEN Masterclass</title>", 1)
    h = h.replace('<span class="fact">v6 &middot; September 2026</span>',
                  '<span class="fact">v6 &middot; September 2026</span>\n      <span class="fact" style="border-color:#0f7a5a;color:#14513e"><b>lab results</b> &middot; %s &middot; %s</span>'
                  % (meta["model"], meta["date"]), 1)

    nav = ('<div class="resnav"><b>This version contains the results of all seven lab exercises</b>, produced with '
           '<b>%s</b> on %s via Ollama on the local computer (not simulated). Each result panel shows the prompts as '
           'sent and the model outputs; buttons reveal answers, tabs and drop-down lists switch between runs, stages and emails.<br>'
           '%s</div>') % (meta["model"], meta["date"], " ".join(
               '<a href="#res-%s">%s</a>' % (n, t) for n, t in (
                   ("tokens", "Lab 1"), ("context", "Lab 2"), ("vary", "Lab 3"), ("steer", "Lab 4"),
                   ("ground", "Lab 5"), ("ladder", "Lab 6"), ("route", "Lab 7"))))
    marker = '<div class="labcall">\n  <div class="hd"><span class="badge">Lab · setup</span>'
    if marker not in h:
        print("setup box not found", file=sys.stderr)
        return 1
    h = h.replace(marker, nav + "\n\n" + marker, 1)

    for badge, names in ANCHORS:
        i = h.find(badge)
        if i < 0:
            print("anchor not found: %s" % badge, file=sys.stderr)
            return 1
        start = h.rfind('<div class="labcall">', 0, i)
        # the lab description box ends at the first closing </div> at its own nesting level
        depth, j = 0, start
        for m in re.finditer(r"<div\b|</div>", h[start:]):
            depth += 1 if m.group(0).startswith("<div") else -1
            if depth == 0:
                j = start + m.end()
                break
        slots = "\n" + "\n".join('<div data-labres="%s"></div>' % n for n in names) + "\n"
        h = h[:j] + slots + h[j:]

    h = h.replace("</body>", '<script type="application/json" id="labdata">%s</script>\n<script>%s</script>\n</body>'
                  % (data, JS), 1)
    pathlib.Path(args.target).write_text(h, encoding="utf-8")
    print("written: %s (%d KB; model %s; results from %s)" % (args.target, len(h.encode("utf-8")) // 1024,
                                                               meta["model"], folder))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    raise SystemExit(main())
