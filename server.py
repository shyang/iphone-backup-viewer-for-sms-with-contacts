#! /usr/bin/env python3

from http.server import HTTPServer, CGIHTTPRequestHandler

class RequestHandler(CGIHTTPRequestHandler):
    def is_cgi(self):
        self.cgi_info = '/', 'viewer.py'
        return self.path == '/'

httpd = HTTPServer(('127.0.0.1', 9000), RequestHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

