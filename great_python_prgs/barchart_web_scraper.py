import requests
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

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'PSX'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/PSX/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'PG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/PG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'ABBV'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/ABBV/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()
symbol = 'TSN'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/TSN/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'SBUX'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SBUX/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'BK'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/BK/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'SPY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SPY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'CPRT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CPRT/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'IRM'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/IRM/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'AMT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/COR/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'XLY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/XLY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'IWM'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/IWM/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'GOOG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/GOOG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'EBAY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/EBAY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'DIS'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/DIS/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'VFC'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/VFC/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'LUV'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/LUV/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()


symbol = 'MCD'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MCD/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'MSFT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSFT/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'FANG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/FANG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'ODFL'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/ODFL/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'MS'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MS/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'EXR'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/EXR/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'XLE'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/XLE/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'BK'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/BK/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'CSCO'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CSCO/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'SLB'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SLB/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'LLY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/LLY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'MSCI'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'WY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'MSFT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'LSI'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'ANET'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'SGH'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'WH'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()

symbol = 'LKQ'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()


symbol = 'TMO'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSCI/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()


symbol = 'RJF'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/RJF/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)

atr_14 = fundamentals[1].iloc[0,3]
rsi_14 = fundamentals[2].iloc[0,0]
hd="_atr_n_rsi_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(atr_14)
str_dictionary1 = repr(rsi_14)
file.write("14 day ATR and RSI = " + str_dictionary + str_dictionary1 + "\n")
file.close()