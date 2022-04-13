import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata


surl = "https://www.flipkart.com/search?q=machine+learning+books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=machine+learning+books%7CBooks&requestId=54d80e7f-eb45-4c66-bf19-bdb1a2715156&as-searchtext=machine%20lear"
soup1 = soup(surl)

edatas = " "
count = soup1.findAll("a", {"class" : "s1Q9rs"})
print(len(count))
print("gettext::: {}"+soup1.getText())
print("title::: {}"+soup1.title)

for record in soup1.findAll("div", {"class" : "_3Djpdu"}):
    print(" {}".format(record.text))
  # for record1 in  record.findAll("div" , {"class" : "_4ddWXP"}):
#       for record2 in  record1.findAll("div" , {"class" : "s1Q9rs"}):
           #print(len(count))
         # title = record2.text.replace(',' , '..' )

     # edatas = edatas + "\n" +title
     #print(edatas)


