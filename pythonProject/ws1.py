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
surl="https://www.tnpscthervupettagam.com/quiz-detail/?q=96d2b6c7d57a153dce69fa29a94b7020795a674f"
soup1 = soup(surl)
#print(soup1)
edatas = " "

for rec1 in soup1.findAll(class_="question-num"):
   # print(rec1)
   for rec2 in rec1.findAll("li",class_="question-paper"):
  #     for rec3 in rec2.find(class_="pb-2"):
          # for rec4 in rec2.find(class_="qust-part"):
               print(rec2)



#table = soup1.find('div', attrs={'class' :"question"})
#print("table pretify 1{}"+table.getText())

for record in soup1.findAll("div", {"class" : "question"}):
    print("test {}".format(record.text))
# for record in soup1.findAll("div", {"class" : "_3Djpdu"}):
 #print(" {}".format(record.text))




#for record in soup1.findAll("div", {"class" : "_3Djpdu"}):
 #print(" {}".format(record.text))
  # for record1 in  record.findAll("div" , {"class" : "_4ddWXP"}):
#       for record2 in  record1.findAll("div" , {"class" : "s1Q9rs"}):
           #print(len(count))
         # title = record2.text.replace(',' , '..' )

     # edatas = edatas + "\n" +title
     #print(edatas)


