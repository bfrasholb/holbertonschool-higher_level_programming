#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Route handling based on path
        if self.path == "/":
            self._send_text_response("Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(data)

        elif self.path == "/status":
            self._send_json_response({"status": "OK"})

        elif self.path == "/info":
            self._send_json_response({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })

        else:
            self._send_404()

    def _send_text_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, data):
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
