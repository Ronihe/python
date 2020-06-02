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

### path:
In an HTTP URI (and many others), the next thing that appears is the path, which identifies a particular resource on a server. A server can have many resources on it — such as different web pages, videos, or APIs. The path tells the server which resource the client is looking for.

When you write a URI without a path, such as http://udacity.com, the browser fills in the default path, which is written with a single slash. That's why http://udacity.com is the same as http://udacity.com/ (with a slash on the end).

