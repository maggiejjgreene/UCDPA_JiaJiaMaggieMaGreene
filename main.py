import requests
data = requests.get("http://api.open-notify.org/iss-now.json")
data2 = data.json()
print(type(data2))
print(data2)
print(data2["iss_position"])
print(data2["message"])
print(data2["timestamp"])

import requests
data = requests.get("http://api.open-notify.org/astros.json")
data2 = data.json()
print(type(data2))
print(data2)
print(data2["number"])
print(data2["message"])
for p in data2["people"]:
    print(p["name"])