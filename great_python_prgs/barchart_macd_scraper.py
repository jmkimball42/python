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


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'AAPL'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/AAPL/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'CSCO'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CSCO/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'PG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/PG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'PSX'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/PSX/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'TSN'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/TSN/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'CSCO'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CSCO/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'FANG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/FANG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'SGH'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SGH/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'WH'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/WH/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'QQQ'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/QQQ/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'ABBV'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/ABBV/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'RJF'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/RJF/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'SPY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SPY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'MSFT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MSFT/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'GOOG'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/GOOG/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'ALE'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/ALE/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'SBUX'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/SBUX/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'AMZN'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/AMZN/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'IRM'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/IRM/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'CPRT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CPRT/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'FREL'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/FREL/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'XLF'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/XLF/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'XLY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/XLY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'LKQ'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/LKQ/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'BK'
# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/BK/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'MCD'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/MCD/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'BX'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/BX/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'JKHY'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/JKHY/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()

symbol = 'CFLT'

# Set up scraper
url = ("https://www.barchart.com/etfs-funabrds/quotes/CFLT/technical-analysis")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = soup(webpage, "html.parser")

# Locate fundamentals table
fundamentals = pd.read_html(str(html), header=1, index_col=0)


macd_14 = fundamentals[2].iloc[0,3]
hd="_macd_14"
csvnm= symbol + "_" + str(today) + hd + ".txt"
file = open(csvnm, "w")
str_dictionary = repr(macd_14)
file.write("14 day MACD = " + str_dictionary + "\n")
file.close()













