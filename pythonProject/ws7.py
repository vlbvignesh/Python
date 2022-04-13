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

def enquiry(answers):
    if len(answers) == 0:
       return 0
    else:
       return 1


# surl="https://www.tnpsctricks.com/geography-model-test-1-in-english/";
surl="https://www.tnpsctricks.com/indian-polity-model-test-1-english/"
soup1= soup(surl)
#print(soup1.prettify())
#print(soup1.text)
#print(list(soup1.children))
testvar1=soup1.find(id="mtq_question_container-1")
testvar2= testvar1.find_all(class_="mtq_question_text")
testvar3= testvar1.find_all(class_="mtq_answer_text")
testvar4=testvar1.find_all(class_="mtq_marker mtq_correct_marker")
#print(testvar4)

#question=""
#for i in range(0,5):
   # for j in range(0,3):
        #print(+i,+j )
count=0
question=""
answers=""

flg=0
ansrotflg=0
for rec1 in testvar2:
    flg += 1
    if rec1.find('ol'):
        # print("OL TAG FOUND::::::::::::::::::::::::::" +format(flg) )
        ansrotflg += 4
    else:
        question+= rec1.text+"\n"
        # print("QUES FOUND::::::::::::::::::::::::::" + format(flg)+f"    :::"+rec1.text+"\n")
        #question = re.sub('[\n]+', '', question)
        ansflg=0

        for rec2 in testvar3:
          if ansflg==4:
             break
          else:
              answers += testvar3[ansrotflg].text+"\n"
           #   print(format(testvar3[5].text))
           #    print("ANS FOUND::::::::::::::::::::::::::" + format(flg)+f"    :::"+testvar3[ansrotflg].text+"\n")
          ansflg+=1
          ansrotflg+=1

quesarr=question.split("\n")
answers = answers.split("\n")

#print(answers)
count=0
myfile1 = open('xyz.txt', 'w')
questionrnge=1
for i in range(len(quesarr)):
  # print(format(questionrnge)+") "+quesarr[i])
  #  if quesarr[i].find('ol'):
  #     print("OL TAG FOUND::::::::::::::::::::::::::"+format(i))
   if "\n" in quesarr[i] or '\r' in quesarr[i]:
     #  print(format("i is::"+format(i)))
       quesarr[i]=re.sub('[\n]+', '\n', quesarr[i])
       myfile1.write(format(questionrnge) + ") " +quesarr[i].replace("\n\n",""))
   else:
    myfile1.write(format(questionrnge) + ") " + quesarr[i] + "\n")
    questionrnge+=1
    for j in range(0,4):
         # print(f"" + answers[count].strip())
         myfile1.write(answers[count]+"\n")
         count += 1
myfile1.close()
     #  if (i == 0) and (j>0):
     #      count += 0
      # else:
      #     count += 1
      # if answers[count]!='null':
      #  print(f""+answers[count])
      # print(f"please ********************i::" ,i)



#print(answers)
   #      test =print(rec1,rec2)
     #    print(test)
    #question+=rec1[0]
