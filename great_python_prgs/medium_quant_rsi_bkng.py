import pandas_ta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
import matplotlib.dates as mdates

prices_df = yf.download(tickers='BKNG',
                        start='2019-01-01',
                        end=dt.date.today())

prices_df['stoch_k'] = pandas_ta.stochrsi(close=prices_df['Adj Close'],
                                          length=20).iloc[:,0]

prices_df['stoch_d'] = pandas_ta.stochrsi(close=prices_df['Adj Close'],
                                          length=20).iloc[:,1]

prices_df['bb_lower'] = pandas_ta.bbands(close=prices_df['Adj Close'],
                                         length=20).iloc[:,0]

prices_df['bb_upper'] = pandas_ta.bbands(close=prices_df['Adj Close'],
                                         length=20).iloc[:,2]

# Can I get rsi_14 fronm this?  Do I get it with another Python program
#df['RSI'] = ta.rsi(df["adjclose"], length=14) # Verify with barchart

prices_df['forward_1d'] = prices_df['Adj Close'].pct_change(1).shift(-1)

prices_df.to_csv('medium_quat_rsi_bkng.csv')