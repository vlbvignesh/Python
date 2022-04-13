import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
import os

def soup(url):
    thepage = urllib.request.urlopen(url)
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
surl="https://www.pallisalai.com/2021/05/geography-online-mock-test-1-english.html";
soup1= soup(surl)
#print(soup1.prettify())
#print(soup1.text)
#print(list(soup1.children))

testvar1= soup1.find(class_="form")
question = testvar1.find_all('li')
answers=testvar1.find_all(value="0")
#for rec7 in question:

   # if rec7[0] is "The feature of Federal system of Indian Constitution is inspired by the constitution of"


 #print(answers)
myfile1 = open('xyz.txt', 'w')
myfile1.write(testvar1.text.replace("\n\n","").strip())
myfile1.close()

# Using readlines()
file1 = open('xyz.txt', 'r')
Lines = file1.readlines()

count = 0
flag=1
# Strips the newline character
for line in Lines:
    count += 1
    flag=count+5
#    if(count==(flag))

    print("Line{}: {}".format(count, line.strip()))
