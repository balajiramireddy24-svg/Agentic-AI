'''
Tokenes -->Operators,Datattypes   -->Control Flow Statement  -->POP    --> Modules -->OOP
Regulsr expressions   -->Data Analyis (numpy,pandas ,data Visualition )  ->>Web Scraping &Virtual Assitiance 
'''
#Regular Expression -->It is a special squenece of characters which helps in parttern matching ,Its helps  to match ,search ,find ,extract or erplace given pattern
#It is Widely used in text processing,text Analiyes
#WEb Development 
'''
import re
#we use representation as r'
a='\n'
print(a)
b=r'\n'   #Here we have Used the representation of raw string r' \n  is treared as a character of (\  and n)
print(b)
print(len(b))

#search().match(),findall(),compile().........


#for suppose you have receied order as Oder ID:  34512
from re import search
import re


string = "order ID :34512"
result=re,search(r' \d' ,string)
print(result)
print(result.group())
result= re.search(r'\d+',string)
print(result)
print(result.group())

#Extract the age of User from data 
data="My Name is Balaji and  My Age is 22,I live in Vijayawada"
age=re.search(r'\d+',data)
print(age ) # it returns the match Object
print(age.start())   #it returns the Starting of the Object
print(age.end())   # It returns the Ending of the object 
print(age.span())   #It  returns the starting and Ending of the Object
print(age.group())

#re.match()  --> It is Used to match only the beginning of the patttern 



import re

greeting="Hello Agentic"
result=re.match(r'Hello',greeting)
print(result)  #it returns None for unmatched Object
if result:
    print("Matchinh is Found :{result.group()}")
else:
    print("Match Not found ")

#re.search()  --> It checks for the first matched pattern
import re
f =re.search(r'[A-Z]',greeting)
print(f)
print(f.group())
g=re.search(r'[A-Z]\w', greeting)
print(g)
h=re.search(r'[A-Z]\w+',greeting)
print(h)
print(h.group())
j=re.search(r'[A-Z]\w+',greeting)
print(j)
print(j.group())


#re.findall()   --> It returns  all the matched pattern and returns list

import re

f=re.findall(r'[A-Z]\w+',greeting)
print(f)
f=re.findall(r'[A-z]\w+',greeting)
print(f)


import re


a="Python 35 Agent 25 GENAI"

f=re.findall(r'\d+',a)
print(f)
#f=re.findall(r'[A-z]\w+',a)
f=re.findall(r'[A-Z][a-z]\w+',a)
print(f)


b="Balaji 22 Ramireddy 9349 Arjun 21 "
f=re.findall(r'\d+',b)
print(f)
f=re.findall(r'[A-Z]',b)
print(f)
f= re.findall(r'[A-Z][a-z]',b)
print(f)



#re.findall()   --->match the complete iteration along with position  

import re


ids= "23 45 36 codegnan"
g=re.findall(r'\d+',ids)
#g=re.searchg=re.findall(r'\d+',ids)
#g=re.findall(r'\d+',ids)
#print(g)
#g=re.findall(r'[A-z]\w+',ids)
#print(g)
#print(type(g))
for i in g:
    print(i.group(),i.start(),i.end())
#print(*g)


#re.fullmatch() --> where we want to have the entire matching  pattern 

import re


data="Codegnan is in Hyderabad,Vijayawada and vizag,contact number is 1234567890"
result=re.fullmatch(r'\d{2}',data)   #need pattern applicable for entrie string it returns None 
#result=re.findall(r'\d{10}',data)
#result=re.fullmatch(r'\d{10}',1234567890)
print(result)
#print(result.group())
'''


#res.sub()  --> where can replace the original pattern
#re.split()  -->where we can specfiy the split pattern 
import re 
t="I Love Food Codegnan Food Balaji Food "
f=re.sub(r'Food','Water',t)
print(f)
h=re.sub(r'\s','*',t)
print(h)


a="Agents GENAI RAG Python"
k=re.split(r'[,;]',a)
print(k)