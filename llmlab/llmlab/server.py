"""A local browser interface. Binds to the loopback address only.

The page it serves makes requests to this process and to nothing else. There
is no content delivery network, no font service, no analytics and no storage.
That is not decoration: the session claims a local route can be shown to be
local, and a page that quietly loaded a stylesheet from elsewhere would make
the claim false.
"""

from __future__ import annotations

import json
import pathlib
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import __version__, backend as be, labs

UI = pathlib.Path(__file__).parent / "ui" / "index.html"

CSP = (
    "default-src 'none'; "
    "style-src 'unsafe-inline'; "
    "script-src 'unsafe-inline'; "
    "img-src data:; "
    "connect-src 'self'; "
    "form-action 'none'; "
    "base-uri 'none'"
)


class Handler(BaseHTTPRequestHandler):
    server_version = "llmlab/" + __version__
    backend_pref = "auto"
    model = None

    def log_message(self, fmt, *args):  # quieter console during a live session
        pass

    def _send(self, code, body: bytes, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, UI.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/survey":
            s = be.survey()
            b = be.detect(self.model, prefer=self.backend_pref)
            s["active"] = {
                "backend": b.name,
                "model": b.model,
                "endpoint": b.endpoint,
                "simulated": b.simulated,
            }
            s["labs"] = [
                {"name": n, "block": labs.BLOCK_MAP.get(n, "")} for n in labs.ORDER
            ]
            s["version"] = __version__
            self._send(200, json.dumps(s).encode("utf-8"))
        else:
            self._send(404, b'{"error":"not found"}')

    def do_POST(self):
        if self.path != "/api/lab":
            self._send(404, b'{"error":"not found"}')
            return
        try:
            n = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(n) or b"{}")
            name = payload.get("lab", "tokens")
            params = payload.get("params") or {}
            pref = payload.get("backend") or self.backend_pref
            b = be.detect(payload.get("model") or self.model, prefer=pref)
            res = labs.run(name, b, params)
            self._send(200, json.dumps(res, ensure_ascii=False).encode("utf-8"))
        except Exception as e:  # a failed lab should explain itself, not 500 silently
            body = json.dumps(
                {
                    "error": str(e),
                    "hint": "Run `python -m llmlab check` in the terminal, or "
                    "switch the route to Simulated in the header.",
                }
            ).encode("utf-8")
            self._send(400, body)


def serve(host="127.0.0.1", port=8765, model=None, prefer="auto", open_browser=True):
    Handler.backend_pref = prefer
    Handler.model = model
    httpd = ThreadingHTTPServer((host, port), Handler)
    url = "http://%s:%d/" % (host, port)
    b = be.detect(model, prefer=prefer)
    print("\n  llmlab %s" % __version__)
    print("  interface   %s" % url)
    print("  route       %s · %s · %s"
          % (b.name, b.model, "simulated" if b.simulated else b.endpoint))
    print("  stop        Ctrl+C\n")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("  stopped\n")
    finally:
        httpd.server_close()
