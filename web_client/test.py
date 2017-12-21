from http.server import HTTPServer,BaseHTTPRequestHandler
import os


def html():
    path = "friends.htm"
    page = open(path)
    page = page.read()
    page = bytes(page,encoding="utf-8")
    return page

class Handler(BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(html())

if __name__=='__main__':  
    address = ('localhost',80)
    http = HTTPServer(address,Handler)
    http.serve_forever()

