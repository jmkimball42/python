# News App
# pip install requests

# I need to output this with a date_time stamp.  Should be able to do this with a shell script and a scheduled job.

import requests
from bs4 import BeautifulSoup
link = "https://www.theguardian.com/world"
headers={"Content-Type":"text"}
response = requests.request("GET", link, headers=headers)
parser = BeautifulSoup(response.text, "html.parser")
for x in parser.find_all("div", class_="fc-item__content"):
    title = x.find("h3")
    print("Title:", title.text)
    url = x.find("a")
    print("URL:", url["href"])
    print ("\n")
