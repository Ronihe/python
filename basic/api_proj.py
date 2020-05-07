import sys
import requests

term = input("what joke would you like to hear: ")
url = f"https://icanhazdadjoke.com/search?term={term}"
res = requests.get(url, headers={"Accept": "application/json"})
results = res.json()["results"]

if len(results) == 0:
    print("no jokes")
    sys.exit()

print(f"There are {len(results)} jokes.")
