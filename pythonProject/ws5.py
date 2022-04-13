import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
import os
import requests
def soup(url):
    thepage = urllib.request.urlopen(url)
    r=requests.get(url)
    print(r.status_code)
 #   print((r.json()))
 #   cont = json.loads(r.content.decode())
 #   print(cont)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata



#surl="https://www.tnpscguru.in/2019/11/Mughals-TNPSC-History-Questions-Answers.html"
#soup1= soup(surl)
#print(soup1.prettify())
#print(soup1.getText)

#testvar= soup1.findAll(id="wrapper")
#print(testvar[0].text)


#surl="https://www.tamilmixereducation.com/2019/05/history-free-online-test.html";
surl="https://www.freeonlinetest.in/reslt/general-knowledge/indian-polity/1";
soup1= soup(surl)

#print(soup1.prettify())
#print(soup1.text)
print(soup1.prettify())

#testvar1= soup1.find_all("p")
#print(testvar1)
