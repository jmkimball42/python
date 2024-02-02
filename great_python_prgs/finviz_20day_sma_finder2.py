# Code for 20 day SMA

import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date

today = date.today()

symbol = 'KLAC'

# Set up scraper
url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]

# Reshape dataframe to get two columns dataframe and change column names
columns = fundamentals.values.reshape(-1,2)
fundamentals = pd.DataFrame(columns)
fundamentals['Fundamentals'] = fundamentals[0]
fundamentals['Values'] = fundamentals[1]
fundamentals = fundamentals.drop(fundamentals.columns[[0,1]], axis=1)

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd

h.to_csv(csvnm, index=True)

symbol = 'MP'

# Set up scraper
url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]

# Reshape dataframe to get two columns dataframe and change column names
columns = fundamentals.values.reshape(-1,2)
fundamentals = pd.DataFrame(columns)
fundamentals['Fundamentals'] = fundamentals[0]
fundamentals['Values'] = fundamentals[1]
fundamentals = fundamentals.drop(fundamentals.columns[[0,1]], axis=1)

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd

h.to_csv(csvnm, index=True)

ymbol = 'LRCX'

# Set up scraper
url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]

# Reshape dataframe to get two columns dataframe and change column names
columns = fundamentals.values.reshape(-1,2)
fundamentals = pd.DataFrame(columns)
fundamentals['Fundamentals'] = fundamentals[0]
fundamentals['Values'] = fundamentals[1]
fundamentals = fundamentals.drop(fundamentals.columns[[0,1]], axis=1)

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd

h.to_csv(csvnm, index=True)