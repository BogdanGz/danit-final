import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("PORT", "8080"))
POD_IP = os.getenv("POD_IP", "unknown")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = f"OK\npod_ip={POD_IP}\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body.encode())))
            self.end_headers()
            self.wfile.write(body.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return

def main():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Listening on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()
