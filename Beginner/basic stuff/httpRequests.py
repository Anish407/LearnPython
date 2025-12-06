import requests

response= requests.get("http://api.open-notify.org/astros.json")

jsonResponse = response.json()

print(jsonResponse)
for person in jsonResponse['people']:
    print(f"{person['name']} is on the {person['craft']}")