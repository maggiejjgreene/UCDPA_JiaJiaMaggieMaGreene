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
bank_data = pd.read_csv("BankChurners.csv")
print(bank_data.head())
print(bank_data.shape)
print(bank_data.info())
print(bank_data.describe())
print(bank_data.values)
print(bank_data.columns)
print(bank_data.index)

bank_data.sort_values("Credit_Limit")
bank_data.sort_values("Credit_Limit", ascending=False)
bank_data.sort_values(["Credit_Limit", "Customer_Age"])
bank_data.sort_values(["Credit_Limit", "Customer_Age"], ascending=[True, False])
print(bank_data["Credit_Limit"])
print(bank_data[["Credit_Limit", "Customer_Age"]])
print(bank_data["Customer_Age"].mean())
print(bank_data["Customer_Age"].min())
print(bank_data["Customer_Age"].max())

print(bank_data.groupby("Credit_Limit")["Customer_Age"].mean())
print(bank_data.groupby("Credit_Limit")["Customer_Age"].agg([min, max]))


for x in "niceday":
    print(x)


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
taxi_owners = pd.read_pickle("taxi_owners.p")
print(taxi_owners.info())
taxi_veh = pd.read_pickle("taxi_vehicles.p")
print(taxi_veh.info())

taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")
print(taxi_own_veh.columns)

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=("_own", "_veh"))
print(taxi_own_veh.columns)

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))
print(taxi_own_veh['fuel_type'].value_counts())


import pandas as pd
temp_data = pd.read_csv("temperatures.csv")
temperatures = temp_data
print(temperatures)

temperatures_ind = temperatures.set_index("city")
print(temperatures_ind)
print(temperatures_ind.reset_index())
print(temperatures_ind.reset_index(drop=True))

cities = ["Moscow", "Saint Petersburg"]
print(temperatures[temperatures["city"].isin(["Moscow","Saint Petersburg"])])
print(temperatures_ind.loc[["Moscow","Saint Petersburg"]])

temperatures_ind = temperatures.set_index(["country","city"])
rows_to_keep = [("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]
print(temperatures_ind.loc[rows_to_keep])
print(temperatures_ind.sort_index())
print(temperatures_ind.sort_index(level=["city"]))
print(temperatures_ind.sort_index(level=["country","city"], ascending=[True, False]))

temperatures_srt = temperatures_ind.sort_index()
print(temperatures_srt.loc["Pakistan":"Russia"])
print(temperatures_srt.loc["Lahore":"Moscow"])
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad")])
print(temperatures_srt.loc[:,"date":"avg_temp_c"])
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"),"date":"avg_temp_c"])

temperatures_bool = temperatures[( temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-01")]
print(temperatures_bool)

temperatures_ind = temperatures.set_index("date").sort_index()
print(temperatures_ind.loc["2010":"2011"])
print(temperatures_ind.loc["2010-08-01":"2011-02-28"])
print(temperatures.iloc[23,1])
print(temperatures.iloc[:5])
print(temperatures.iloc[:,2:4])
print(temperatures.iloc[:5, 2:4])


import pandas as pd
import matplotlib.pyplot as plt
winter_data = pd.read_csv("winter.csv")
print(winter_data.head())
print(winter_data.shape)
print(winter_data.info())

winter_data["Year"].hist()
plt.show()
winter_data["Sport"].hist()
plt.show()
winter_data["Gender"].hist()
plt.show()
winter_data["Medal"].hist()
plt.show()


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


import pandas as pd
data = {'Sym': ['APPL', 'APPL', 'APPL'],
        'Price': [105.00, 117.05, 289.80],
        'Date': ['2015/12/31', '2017/12/01', '2019/12/27']}
positions = pd.DataFrame(data=data)
print(positions)

data = [{'Sym': 'APPL', 'Price': 105.00, 'Date': '2015/12/31'},
        {'Sym': 'APPL', 'Price': 117.05, 'Date': '2017/12/01'},
        {'Sym': 'APPL', 'Price': 289.80, 'Date': '2019/12/27'}]
positions = pd.DataFrame(data=data)
print(positions)

data = [['APPL', 105.00, '2015/12/31'],
        ['APPL', 117.05, '2017/12/01'],
        ['APPL', 289.80, '2019/12/27']]
columns = ['Sym', 'Price', 'Date']
df = pd.DataFrame(data=data, columns=columns)
print(df)


names = ['Apple Inc','Coca-Cola', 'Walmart']
print(names)
prices = [159.54, 37.13, 71.17]
print(prices)
print(names[0])
print(names[1])
print(prices[-1])

names = ['Apple Inc', 'Coca-Cola', 'Walmart']
names_subset = ['Coca-Cola','Walmart']
print(names_subset)
stocks = [names, prices]
print(stocks)
print(stocks[1])
print(stocks[0][1])
print(stocks[1][2])
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)
names.append('Amazon.com')
print(names)
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)
max_price = max(prices)
max_index = prices.index(max_price)
max_stock_name = names[max_index]
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')


import numpy as np
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]
prices_array = np.array(prices)
earnings_array = np.array(earnings)
print(prices_array)
print(earnings_array)
pe_array = np.array(prices)/np.array(earnings)
print(pe_array)
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)
stock_array = np.array([prices, earnings])
print(stock_array)
print(stock_array.shape)
print(stock_array.size)
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)
print(stock_array_transposed.shape)
print(stock_array_transposed.size)
prices = stock_array_transposed[:, 0]
print(prices)
earnings = stock_array_transposed[:, 1]
print(earnings)
company_1 = stock_array_transposed[0, :]
print(company_1)
prices_mean = np.mean(prices)
print(prices_mean)
prices_std = np.std(prices)
print(prices_std)
company_ids = np.arange(1, 8, 1)
print(company_ids)
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)
price_mean = np.mean(prices)
boolean_array = (prices > price_mean)
print(boolean_array)
above_avg = prices[boolean_array]
print(above_avg)













