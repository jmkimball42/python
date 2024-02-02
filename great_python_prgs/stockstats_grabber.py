import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stockstats import StockDataFrame

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 10)

symbol = 'AAPL'
start_date = '2021-01-01'
api_key = '3c5c9a5538fd4c22af5e7794b2f0bfcb'
api_url = 'https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&outputsize=5000&apikey=3c5c9a5538fd4c22af5e7794b2f0bfcb'
raw_df = requests.get(api_url).json()
#print (raw_df)
df = pd.DataFrame(raw_df['values']).iloc[::-1].set_index('datetime').astype(float)
df1 = df.copy()    
df1 = df1[df1.index >= start_date]
df1.index = pd.to_datetime(df1.index)
#print (df1)
	



aapl = StockDataFrame(df1)
aapl[['close_50_sma', 'close_100_sma', 'close_200_sma', 'rsi_14' ]]
z = aapl.tail(1)
print (z)

#aapl['rsi_14']
#rsi = aapl.tail(1)''
#print (rsi)


# 


# Try Alpha Advantage instead!

