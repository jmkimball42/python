import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date

today = date.today()

symbol = 'NOW'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/NOW/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

rsi_14 = fundamentals[2].iloc[0,0]
rsi_20 = fundamentals[2].iloc[1,0]
hd="_rsi_14_n_rsi_20"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(rsi_14)
str_dictionary1 = repr(rsi_20)
file.write("14 day RSI and 20 day RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'SGH'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/NOW/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

rsi_14 = fundamentals[2].iloc[0,0]
rsi_20 = fundamentals[2].iloc[1,0]
hd="_rsi_14_n_rsi_20"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(rsi_14)
str_dictionary1 = repr(rsi_20)
file.write("14 day RSI and 20 day RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()












