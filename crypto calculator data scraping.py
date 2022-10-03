#Code by PythonP
from bs4 import BeautifulSoup
import requests

def calculateCrypto(type,USD):
    if(type == "ETH"):
        typeString = "ethereum"
    if(type == "BTC"):
        typeString = "bitcoin"
    if(type == "LTC"):
        typeString = "litecoin"

    url = "https://bitflyer.com/en-us/"+ typeString +"-chart"#url for crypto charts
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "lxml")
    source=soup.find_all("div", attrs={"class" : "p-currencyInfo__price c-text--number"})
    
    OneCryptoCostwspaces=source[0].text
    #print(OneBtcCostwspaces)
    OneCryptoCost=OneCryptoCostwspaces.replace(" ", "")
    OneCryptoCost=OneCryptoCost.replace("*USD", "")
    OneCryptoCost=OneCryptoCost.replace(",", "")
    OneCryptoCost = float(OneCryptoCost.strip())
    # price = price[:-7] # this removes the last 7 characters from your string 

    oranti = OneCryptoCost / USD
    cryptoDue = 1 / oranti
    #print(OneCryptoCost)
    return(cryptoDue)


print(calculateCrypto("BTC", 100))