from http.server import HTTPServer, BaseHTTPRequestHandler

class GreeterHandler(BaseHTTPRequestHandler):
    do_GET = lambda self: (
        self.send_response(200),
        self.send_header("Content-type", "text/html"),
        self.end_headers(),
        self.wfile.write(b"Hello from Neha!, today is saturday")
    )

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), GreeterHandler)
    print("Server running on port 8080...")
    server.serve_forever()