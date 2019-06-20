from base64 import encode
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, result

port = 9999

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if '?' in self.path:
            urls = self.path.split('?')
            path = urls[0]
            qs = urls[1].split('&')
            print(path, qs)

        o = urlparse.urlparse(self.path)
        params = parse_qs(result.query)
        print(o, type(o))
        print(params)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html: charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요</h1>', encode('utf-8'))


httpd = HTTPServer(('0.0.0.0'), port).SimpleHTTPRequestHandler)
print('Server running on port:{port}')
