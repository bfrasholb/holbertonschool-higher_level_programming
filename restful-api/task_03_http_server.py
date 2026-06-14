#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json(data)

        elif self.path == "/status":
            # IMPORTANT: must be plain text, not JSON
            self._send_text("OK")

        else:
            self._send_404()

    def _send_text(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
