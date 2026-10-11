import os, http.server, socketserver
PORT = int(os.environ.get('PORT', 10000))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), handler) as httpd:
    print(f'Serving on port {PORT}')
    httpd.serve_forever()