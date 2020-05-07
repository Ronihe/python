# what happens when you type a url in the url bar
# 1. dns look up - ip address
# 2. computer makes a request to a server
# 3. server process the request
# 4. server send response


# http headers
# meta data: additional info about the request and response


# http verbs:
# get : retrieve data, dat passed in query strng, no "side-effects", can be cache, can be bookmarked
# post: same besides have "side-effect", not cached, canoot be bookmarked

# api: application programming interface
# allows you to get data from another application without needing to understand how the application works
# send data back in diferent formats
# ex: github, spotify, google

# request module
import requests

url = "https://icanhazdadjoke.com/"
res = requests.get(url, headers={"Accept": "application/json"})
print(type(res.text), res.text)
print(type(res.json()), res.json()["joke"])
