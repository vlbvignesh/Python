import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata


#surl = "https://www.flipkart.com/search?q=machine+learning+books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=machine+learning+books%7CBooks&requestId=54d80e7f-eb45-4c66-bf19-bdb1a2715156&as-searchtext=machine%20lear"
surl="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
soup1= soup(surl)



seven_day = soup1.find(id="detailed-forecast")
forecast_items = seven_day.find_all(class_="col-sm-2 forecast-label")
#tonight = forecast_items[2]
#print(forecast_items)

for file0 in soup1.find(id="detailed-forecast")
for file in file0.find(class_="col-sm-2 forecast-label"):
 print(" {}"+file.text)
  #  for file1 in soup1.findAll(class_="col-sm-2 forecast-label"):



