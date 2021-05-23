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

import pandas as pd
data = pd.read_csv("netflix_titles.csv")
print(data.head())
print(data.shape)
print(data.info())

missingdata = data.isnull()
print(missingdata)

missingdata = data.isnull().sum()
print(missingdata)

cleaned_data = data.fillna(0)
cleaned_missingdata = cleaned_data.isnull().sum()
print(cleaned_missingdata)
print(cleaned_data.info())

new_data = data.dropna(axis=0)
print(data.shape, new_data.shape)
new_data = data.dropna(axis=1)
print(data.shape, new_data.shape)

new_data1 = data.drop_duplicates(subset=["director"])
print(data.shape, new_data1.shape)
new_data1 = data.drop_duplicates(subset=["director", "cast"])
print(data.shape, new_data1.shape)
new_data1 = data.drop_duplicates(subset=["director", "cast", "title"])
print(data.shape, new_data1.shape)

