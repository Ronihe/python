from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
    <pre>
{}
  </pre>

'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. the length of the message
        length = int(self.headers.get("COntent-length", 0))

        # 2. read the correct amount of data from the request
        data = self.rfile.read(length).decode()
        print(memory)

        # 3. extract the message field from the request data
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store it in memory.
        memory.append(message)

        # 4. send the message back as the response
        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Then encode and send the form.
        # Send the form with the messages in it.
        mesg = form.format("\n".join(memory))

        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
