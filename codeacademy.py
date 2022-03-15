import datetime
import requests
from bs4 import BeautifulSoup
#stock 1
URL = "https://ca.finance.yahoo.com/quote/DOGE-USD?p=DOGE-USD&.tsrc=fin-srch"
webpage_response = requests.get(URL)
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
results = soup.find_all(id = "quote-summary")
stock_name = soup.find('h1', attrs={"data-reactid":"7"})
for result in results:
    previous_close = result.find('span', attrs={"data-reactid":"48"})
    open_price = result.find('span', attrs={"data-reactid":"53"})
    
x = datetime.datetime.now()
#stock2
URL1 = "https://ca.finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-tre-srch"
webpage_response1 = requests.get(URL1)
webpage1 = webpage_response1.content
soup1 = BeautifulSoup(webpage1, "html.parser")
results1 = soup1.find_all(id = "quote-summary")
for result1 in results1:
    open_price1 = result1.find("span", attrs={"data-reactid" :"49"})
stock_name1 = soup1.find("h1", attrs={"D(ib) Fz(18px)"})
previous_close1 = soup1.find("td", attrs={"Ta(end) Fw(600) Lh(14px)"})

    
file = open("mystocks.txt", "a")
file.write(stock_name.text + ":" + previous_close.text + ":" + open_price.text + ":" + str(x.day) + ":" + str(x.strftime("%B")) + ":" + str(x.year) + "\n")
file.write(stock_name1.text + ":" + previous_close1.text + ":" + open_price1.text + ":" + str(x.day) + ":" + str(x.strftime("%B")) + ":" + str(x.year) + "\n")
