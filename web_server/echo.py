from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        print(self.path)

        # Now, write the response body.
        # using a string slice to remove the first character (which is always a slash), and then encoding the resulting string into bytes, then writing that to the HTTP response body.
        self.wfile.write(self.path[1:].encode())


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
