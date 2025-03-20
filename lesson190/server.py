from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/lesson190/index.html'
        return super().do_GET()

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving HTTP at http://localhost:{port}/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
