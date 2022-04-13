import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
import os
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

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
surl="https://learn.canvas.net/login/canvas";
soup1= soup(surl)
print(soup1.prettify())
#print(soup1.text)
#print(list(soup1.children))

testvar1= soup1.find(id="main-wrapper")
#print(testvar1)
#for rec in testvar1:
 #   for rec1 in rec:
  #      for rec2 in rec1:
         #   print()
 #print(rec)
containerval = testvar1.find_all('td')

test=""
for rec in containerval:
 #  print(rec)
    #if rec == "\n":
        test+= rec.text
        test=re.sub('[\n]+', '\n', test)


print(f"waste::"+test)
myfile1 = open('xyz.txt', 'w')
myfile1.write(test)
myfile1.close()
#question=containerval.f
#print(containerval)

#answers=testvar1.find_all(value="0")
#for rec7 in question:

   # if rec7[0] is "The feature of Federal system of Indian Constitution is inspired by the constitution of"


#print(answers)


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

 #   print("Line{}: {}".format(count, line.strip()))
#for rec1 in  testvar1:
  # question=testvar1.findALl('li')
 #  print(question)
  #  answers=rec1.find_all('input')
#name="vignesh"

#geek = '{"Question": '{name}', "Answers": ["Python", "C++", "PHP"]}'
#print(json.loads(geek))
#with open(loadjsonfile,'w') as file_test:
 #json.dump(geek_dict,file_test)

#numbers = [10,20,30,40]
#filename11 ='numbers.json'
#with open(filename11,'w') as file_object:
 #json.dump(ques,file_object)
''

    #for test in answers:

            # Writing data to a file

        # Writing to file

#print(test)


#print(f""+wste.replace(' ',''))

#testvar1=testvar.find("id","class":"question"):
#print(testvar1)
#testvar2=testvar1[1]
#print(testvar2)
#for testvar2 in testvar1.
 #for rec in soup1.findAll( id="wrapper"):
  #  for rec1 in rec.find(class_="question"):
   #     print(rec1)