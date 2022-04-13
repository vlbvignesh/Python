import re
import urllib
import urllib.request
from urllib.parse import urlparse

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





surl="https://www.winmeen.com/indian-polity-online-model-test/"
soup1= soup(surl)

def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


urldtl =[""]
for a  in soup1.find_all('a',href=True):
    var1=format(a['href'])
    if("https://www.tnpsctricks.com/indian-polity-model-test" in var1):
      # print(var1)
      if("english" in var1):
          urldtl.append(format(str(var1)))

      #    for j in range(0, 3):
print(f" Url List::",urldtl[8])
for k in range(1,len(urldtl)):
    print(f"url::"+urldtl[k])
    soup2 = soup(urldtl[k])
    testvar1 = soup2.find(id="mtq_question_container-1")
    testvar2 = testvar1.find_all(class_="mtq_question_text")
    testvar3 = testvar1.find_all(class_="mtq_answer_text")

    question=""
    answers=""
    flg=0
    ansrotflg=0

    for rec1 in testvar2:

        if rec1.find('ol') or rec1.find('ul'):
           print("OL TAG FOUND::::::::::::::::::::::::::" +format(flg) )
           ansrotflg += 4
        else:
           flg += 1
           question+= rec1.text+"\n"
           print("QUES FOUND::::::::::::::::::::::::::" + format(flg)+f"    :::"+rec1.text+"\n")
           #question = re.sub('[\n]+', '', question)
           ansflg=0
           for rec2 in testvar3:
               if ansflg==4:
                  break
               else:
                  answers += testvar3[ansrotflg].text+"\n"
           #   print(format(testvar3[5].text))
                  print("ANS FOUND::::::::::::::::::::::::::" + format(flg)+f"    :::"+testvar3[ansrotflg].text+"\n")
                  ansflg+=1
                  ansrotflg+=1

    quesarr=question.split("\n")
    answers = answers.split("\n")
    print(f"quesarr********", quesarr)
    print(f"ANSWER********",answers)

    count = 0
    myfile1 = open('xyz'+format(k)+'.txt', 'w',encoding="utf-8")
    questionrnge = 1
    print("LENGTH QUESTION:::::"+format(len(quesarr)))
    for i in range(len(quesarr)-1):
        myfile1.write(format(questionrnge) + ") " + quesarr[i] + "\n")
        questionrnge += 1
        for j in range(0, 4):
            print(f"count::"+format(count)+ answers[count].strip())
            myfile1.write(answers[count] + "\n")
            count += 1
    myfile1.close()