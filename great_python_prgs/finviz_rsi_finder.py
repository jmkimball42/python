import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date

today = date.today()

symbol = 'IAU'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'TSN'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'SPY'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'CPRT'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'AMT'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'ABBV'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'PG'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)



symbol = 'SBUX'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'IRM'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'GOOG'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'EBAY'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'DIS'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)


symbol = 'EXR'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'XLF'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'FREL'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'RJF'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'BK'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'MSCI'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'SGH'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)

symbol = 'CSCO'

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


y = fundamentals.tail(20)
h = y.head(1)
hd="_rsi.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)