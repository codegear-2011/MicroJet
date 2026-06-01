from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    router = None

    def do_GET(self):
        component = self.router.get(self.path)
        if component:
            html = component.render()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run_server(router, host, port):
    Handler.router = router
    server = HTTPServer((host, port), Handler)
    print(f"Atomy running on http://{host}:{port}")
    server.serve_forever()
