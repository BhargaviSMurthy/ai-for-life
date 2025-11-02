"""Small local HTTP entrypoint.

This uses Python's standard library WSGI server so no extra dependencies
are required. It listens on the port defined by the PORT environment
variable (defaults to 8080).

Endpoints
- GET / -> plain text welcome
- GET /health -> JSON status
- POST /predict -> echoes JSON body (placeholder)
"""

from wsgiref.simple_server import make_server
import os
import json
import sys


def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")

    if path == "/":
        status = "200 OK"
        headers = [("Content-Type", "text/plain; charset=utf-8")]
        start_response(status, headers)
        return ["ai-for-life backend - running\n".encode("utf-8")]

    if path == "/health":
        status = "200 OK"
        headers = [("Content-Type", "application/json; charset=utf-8")]
        start_response(status, headers)
        body = {"status": "ok", "service": "ai-for-life"}
        return [json.dumps(body).encode("utf-8")]

    if path == "/predict" and method.upper() == "POST":
        try:
            try:
                length = int(environ.get("CONTENT_LENGTH", 0))
            except Exception:
                length = 0
            body = environ['wsgi.input'].read(length) if length else b""
            payload = json.loads(body.decode('utf-8')) if body else {}
        except Exception:
            status = "400 Bad Request"
            start_response(status, [("Content-Type", "application/json")])
            return [json.dumps({"error": "invalid json"}).encode('utf-8')]

        # Placeholder: echo back payload under `prediction`
        status = "200 OK"
        start_response(status, [("Content-Type", "application/json")])
        return [json.dumps({"prediction": None, "input": payload}).encode("utf-8")]

    status = "404 Not Found"
    start_response(status, [("Content-Type", "text/plain")])
    return [b"Not Found"]


def run(port: int = None):
    # Accept port from function arg, CLI arg, or PORT env var. Default 8080.
    if port is None:
        if len(sys.argv) > 1:
            try:
                port = int(sys.argv[1])
            except Exception:
                port = None
    port = port or int(os.environ.get("PORT", "8080"))
    host = "0.0.0.0"
    print(f"Starting ai-for-life backend on http://{host}:{port} (Ctrl-C to stop)")
    with make_server(host, port, app) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped")


if __name__ == "__main__":
    run()
