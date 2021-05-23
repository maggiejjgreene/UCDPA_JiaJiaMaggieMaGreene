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

import pandas as pd
climate_change = pd.read_csv("climate_change.csv")
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col="date")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["relative_temp"])
ax.set_xlabel("Time")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
seventies = climate_change["1970-01-01":"1979-12-31"]
ax.plot(seventies.index, seventies["co2"])
plt.show()

import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.plot(climate_change.index, climate_change["co2"], color="blue")
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change["relative_temp"], color = 'red')
plt.show()


def plot_timeseries(axes, x, y, color, xlabel, ylabel):
 axes.plot(x, y, color=color)
 axes.set_xlabel(xlabel)
 axes.set_ylabel(ylabel, color=color)
 axes.tick_params('y', colors=color)
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")
plt.show()

fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["relative_temp"])
ax.annotate(">1 degree", xy=[pd.Timestamp("2015-10-06"), 1])
plt.show()

fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], 'red',"Time (years)", "Relative temp (Celsius)")
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1 ), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={"arrowstyle":"->", "color":"gray"})
plt.show()

