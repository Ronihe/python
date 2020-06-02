from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    """
    Create a subclass of http.server.BaseHTTPRequestHandler. This is your handler class.
    """

    def do_GET(self):
        """
        The method for GET requests has to be called do_GET.

        Inside the method, call built-in methods of the handler class to read the HTTP request and write the response.
        Returns:

        """
        # First, send a 200 OK http status response.
        self.send_response(200)

        # Then send headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # write response
        self.wfile.write("Hello, HTTP!\n".encode())


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
