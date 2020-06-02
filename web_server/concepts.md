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





