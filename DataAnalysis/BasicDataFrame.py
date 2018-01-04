import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style

# get datetime as year/month/day
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 8, 22)

# create dataframe fromthe dates defined above
# this will pull data for Exxon fromthe Yahoo Finance API, storing the data in
# the df variable 
df = web.DataReader("XOM", "yahoo", start, end)

# print dataset
print(df)

# another option to print the dataset i to just print the head
# this will just print the first 5 elements of the dataset 
# useful for debugging
print(df.head())

style.use('fivethirtyeight')

df['High'].plot()

plt.legend()
plt.show()
