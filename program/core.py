from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


def run_server(port=8080):
    print("listen at", port)
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()
