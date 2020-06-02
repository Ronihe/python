https://classroom.udacity.com/courses/ud303/lessons/6ff26dd7-51d6-49b3-9f90-41377bff4564/concepts/75becdb9-da2a-4fbf-9a30-5f3ccd1aa1d6

## server:       
A server is just a program that accepts connections from other programs on the network.

when you start the server program, it wiats for the clients to connect to it.

ex. demo server waiting for your web browser to ask for a page.     
when a connection comes, the erver runs a piece f code - like callng a func to handle each incoming connection.

a connection is like a phone call, like a channel through which the client and server can talk to each other.       
web clients can send requests and servers send resp backs.

## URI:
uniform resource identifier. aka web address.


parts of URI:

URI is a name for a resource.

example:
```commandline
https://en.wikipedia.org/wiki/fish

https is the scheme
en.wikipedia.org is the hostname
/wiki/fish is the path
```
### Scheme:
The first part of a URI is the scheme, which tells the client how to go about accessing the resource. Some URI schemes you've seen before include http, https, and file. File URIs tell the client to access a file on the local filesystem. HTTP and HTTPS URIs point to resources served by a web server.

[the official list](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)
```commandline
mailto is used for links to email addresses. data is used to put a piece of hardcoded data directly into a web page, for instance a small image. magnet is used for links to some file-sharing services such as BitTorrent. However, there is no such thing as a postal URI; if you want to send postal mail from the Web you still need to print it out and put it in the mailbox yourself.
```
 ### hostname:
 
 You'll often see web addresses written as just a hostname in print. But in the HTML code of a web page, you can't write <a href="www.google.com">this</a> and get a working link to Google. A hostname can only appear after a URI scheme that supports it, such as http or https. In these URIs, there will always be a :// between the scheme and hostname.

We'll see more about hostnames later on in the lesson. By the way, not every URI has a hostname. For instance, a mailto URI just has an email address: mailto:spam@example.net is a well-formed mailto URI. This also reveals a bit more about the punctuation in URIs: the : goes after the scheme, but the // goes before the hostname. Mailto links don't have a hostname part, so they don't have a //.

```commandline
Why is it called a hostname? In network terminology, a host is a computer on the network; one that could host services.

```
IP address: every piece of work of network traffic on the internet on the internet is labeled with the IP addresses of the sending and receiving computers.
DNS: domain name system, a set of servers maintained by the ISPs (internet service providers)p and other network servers. your operating system's network configration uses DNS. which is a set of servers maintained by the ISP.

#### Localhost:
The IPv4 address 127.0.0.1 and the IPv6 address ::1 are special addresses that mean "this computer itself" — for when a client (like your browser) is accessing a server on your own computer. The hostname localhost refers to these special addresses.


#### ports:
http://localhost:8000/. This URI has a port number of 8000. But most of the web addresses you see in the wild don't have a port number on them. This is because the client usually figures out the port number from the URI scheme.

HTTP URIs imply a port number of 80, whereas HTTPS URIs imply a port number of 443.

Your Python demo web server is running on port 8000. Since this isn't the default port, you have to write the port number in URIs for it.

 IP addresses distinguish computers; port numbers distinguish programs on those computers.

```commandline
Why do we use port 8000 instead of 80 for the demo server? For historical reasons, operating systems only allow the administrator (or root) account to listen on ports below 1024. This is fine for production web servers, but it's not convenient for learning.

```


### path:
In an HTTP URI (and many others), the next thing that appears is the path, which identifies a particular resource on a server. A server can have many resources on it — such as different web pages, videos, or APIs. The path tells the server which resource the client is looking for.

When you write a URI without a path, such as http://udacity.com, the browser fills in the default path, which is written with a single slash. That's why http://udacity.com is the same as http://udacity.com/ (with a slash on the end).

### Relative URI references

Take a look at the HTML source for the demo server's root page. Find one of the <a> tags that links to a file. In mine, I have a file called cliffsofinsanity.png, so there's an <a> tag that looks like this:
```commandline

<a href="cliffsofinsanity.png">cliffsofinsanity.png</a>

```
### Other URI parts

- https://en.wikipedia.org/wiki/Oxygen
- https://en.wikipedia.org/wiki/Oxygen#Discovery

If you follow these links in your browser, it will fetch the same page from Wikipedia's web server. But the second one displays the page scrolled to the section about the discovery of oxygen. The part of the URI after the # sign is called a fragment. The browser doesn't even send it to the web server. It lets a link point to a specific named part of a resource; in HTML pages it links to an element by id.

#### GET request
```commandline
127.0.0.1 - - [01/Jun/2020 15:21:37] "GET / HTTP/1.1" 200 -

```
*/* is the path
*HTTP/1.1* is the protocol of the request.

### http resp:
1. status line:
```commandline
HTTP/1.0 200 OK     
HTTP/1.1 301 Moved Permanently
```

2. headers:
each header is a line with a keyword
ex: 
    location:
    content-type:
 
 cookies: a web feature to let the servers save data on the browser
 
 To set a cookie, the server sends the Set-Cookie header. The browser will then send the cookie data back in a Cookie header on subsequent requests. You'll see more about cookies later in this course.
 
 
3. resp body:


# http.server Python module

Note: http.server is not recommended for production. It only implements basic security checks. But it is a first step to understand the lower level behavior of a Web server.

## Servers and handlers
`HTTPServer` class and `request handler` class

- httpServer: how to listen on a port and accept HTTP request from clients. whenever it receives a request, it hands that request off to the second part -  a request handler -  which is dffierent from every web service.

## http response encode():
http resp could contain any kind of data, not only text.
self.wfile.write method in the handler class expects to be given a bytes objects.
encode() the string to bytes object, which is suitable over the network
decode() is the opposite

## queries and quoting
The query part of the URI is the part after the ? mark. Conventionally, query parameters are written as key=value and separated by & signs.

### URL quoting
HTTP URLs aren't allowed to contain spaces or certain other characters. So if you want to send these characters in an HTTP request, they have to be translated into a "URL-safe" or "URL-quoted" format.

## FORMS

#### Idempotence
Vocabulary word of the day: idempotent. An action is idempotent if doing it twice (or more) produces the same result as doing it once. "Show me the search results for 'polar bear'" is an idempotent action, because doing it a second time just shows you the same results. "Add a polar bear to my shopping cart" is not, because if you do it twice, you end up with two polar bears.

POST requests are not idempotent. If you've ever seen a warning from your browser asking you if you really mean to resubmit a form, what it's really asking is if you want to do a non-idempotent action a second time.

```commandline
By the way, the names of HTTP headers are case-insensitive. So there's no difference between writing Content-Length or content-length or even ConTent-LeNgTh … except, of course, that humans will read your code and be confused by that last one.

```

### post method
The code for a do_POST method will need to do some pretty different things from a do_GET method.

Inside do_POST, our code can read the request body by calling the self.rfile.read method. self.rfile is a file object, like the self.wfile we saw earlier — but rfile is for reading the request, rather than writing the response.
```commandline
However, self.rfile.read needs to be told how many bytes to read … in other words, how long the request body is.

```
### headers are strings or missing
- Instead, we'll use the .get dictionary method to get the header value safely.


## Post-Redirect-Get
There's a very common design pattern for interactive HTTP applications and APIs, called the PRG or Post-Redirect-Get pattern. A client POSTs to a server to create or update a resource; on success, the server replies not with a 200 OK but with a 303 redirect. The redirect causes the client to GET the created or updated resource.

## CONCURRENCY
Being able to handle two ongoing tasks at the same time is called concurrency, and the basic http.server.HTTPServer doesn't have it. It's pretty straightforward to plug concurrency support into an HTTPServer, though. The Python standard library supports doing this by adding a mixin to the HTTPServer class. A mixin is a sort of helper class, one that adds extra behavior the original class did not have. To do this, you'll need to add this code to your bookmark server:

```commandline
import threading
from socketserver import ThreadingMixIn

class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."
```
Then look at the bottom of your bookmark server code, where it creates an HTTPServer. Have it create a ThreadHTTPServer instead:

```commandline
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
```
## Others:
### Static content and more

The Web was originally designed to serve documents, not to deliver applications. Even today, a large amount of the data presented on any web site is static content — images, HTML files, videos, downloadable files, and other media stored on disk.

Specialized web server programs — like Apache, Nginx, or IIS — can serve static content from disk storage very quickly and efficiently. They can also provide access control, allowing only authenticated users to download particular static content.

### Routing and load balancing

Some web applications have several different server components, each running as a separate process. One thing a specialized web server can do is dispatch requests to the particular backend servers that need to handle each request. There are a lot of names for this, including request routing and reverse proxying.

Some web applications need to do a lot of work on the server side for each request, and need many servers to handle the load. Splitting requests up among several servers is called load balancing.

## https:
When a browser and a server speak HTTPS, they're just speaking HTTP, but over an encrypted connection. The encryption follows a standard protocol called Transport Layer Security, or TLS for short. TLS provides some important guarantees for web security:
- privacy: It keeps the connection private by encrypting everything sent over it. Only the server and browser should be able to read what's being sent.
- authenticity: It lets the browser authenticate the server. For instance, when a user accesses https://www.udacity.com/, they can be sure that the response they're seeing is really from Udacity's servers and not from an impostor.
- integrity: It helps protect the integrity of the data sent over that connection — checking that it has not been (accidentally or deliberately) modified or replaced.










