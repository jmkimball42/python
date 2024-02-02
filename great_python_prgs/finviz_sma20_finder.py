import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date

today = date.today()

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("tsn_today_sma20.csv", index=True)


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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'TSLA'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'QCOM'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)
symbol = 'DE'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)
symbol = 'SM'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'AAPL'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'ABR'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'XLY'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'XLE'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'PSX'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'CVX'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)


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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'IWM'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'QQQ'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)


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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'MCD'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'MSFT'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)


symbol = 'MS'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'FANG'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'SKY'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'PRU'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'PLD'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'LPX'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'XLB'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'DRI'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'SLB'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'NOC'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'NOW'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'VFC'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'BUG'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'CIBR'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'IHAK'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'WH'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'WH'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)


symbol = 'JKHY'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'ADSK'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'REGN'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'STT'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'LKQ'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'SYY'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'AMZN'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'ULTA'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'DFS'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'NVDA'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'WY'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'CNP'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'ANET'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'LSI'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'TMO'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'ADP'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'APH'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'CBRE'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'PAYX'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'SLB'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'BX'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'CFLT'

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
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

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

#fundamentals.to_csv("iau_9_22_21.csv", index=True)
y = fundamentals.tail(5)
h = y.head(1)
hd="_sma20.csv"
csvnm= symbol + "_" + str(today) + hd
#print(csvnm)
h.to_csv(csvnm, index=True)
#h.to_csv("iau_today_sma20.csv", index=True)

symbol = 'NXPI'

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

symbol = 'DDOG'

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