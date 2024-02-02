# 
# Title: dec_trade_strat.py
# Author: John M. Kimball
# Date: December 28, 2023
# Description: This program is code from a Medium article at: 
# https://medium.com/gitconnected/an-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc
#

# IMPORTING PACKAGES

import pandas as pd
import requests
import pandas_ta as ta
import matplotlib.pyplot as plt
from termcolor import colored as cl
import math 
from yahoo_fin import stock_info as si

plt.rcParams['figure.figsize'] = (20,10)
plt.style.use('fivethirtyeight')

# EXTRACTING HISTORICAL DATA

def get_historical_data(symbol, start_date, interval):
    url = "https://api.benzinga.com/api/v2/bars"
    querystring = {"token":"YOUR API KEY","symbols":f"{symbol}","from":f"{start_date}","interval":f"{interval}"}

    hist_json = requests.get(url, params = querystring).json()
    df = pd.DataFrame(hist_json[0]['candles'])
    
    return df

aapl = get_historical_data('AAPL', '1993-01-01', '1W')
aapl.tail()

#
#

from yahoo_fin import stock_info as si
import time
from random import randint

# This is a helper function to calculate the difference between two dates in business days (trading days).
def get_past_business_days_delta_str(current_date_str, business_day_delta):
    target_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d")
    delta_date = target_date + (business_day_delta * US_BUSINESS_DAY)
    delta_date_str = datetime.datetime.strftime(delta_date, "%Y-%m-%d")
    return delta_date_str

# The next function loads the list of stcok symbols that are on my watch list 
def load_jmk_symbols():
    jmk_df = pd.read_csv('jmk_watch_list.csv')
    symbols = jmk_df['Symbol'].to_numpy()
    return symbols

# This function loads the the daily historic price information for one stock using the Yahoo Finance library
def load_historic_data(symbol):
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")
    #  Get last 2 years of data
    start_date = today - (522 * US_BUSINESS_DAY)
    start_date_str = datetime.datetime.strftime(start_date, "%Y-%m-%d")
    try:
        # Download data from Yahoo Finance
        df = si.get_data(symbol, start_date=start_date_str, end_date=today_str, index_as_date=False)
        return df
    except:
        print('Error loading stock data for ' + symbol)
        return None
