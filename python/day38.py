'''
Regular Expression   --> re module   -->re,findall re.match(),re.fullname(),re.fulliter(),
re.sub(),re.split(),re.compile(),re.escaple()

re.compile()  --->when we want use the pattern multiple times we can compile the patttern and use it multiple times'''
'''

import re

data =  "Codegnan Marks its 8 Anniversary ,founded in 2018"

pattern = re.compile(r'\d+')
print(pattern)
result= pattern.findall(data)
print(result)
f= pattern.search(data)
print(f)
print(f.group())
pattern = re.findall(r'[A-z]\w+',data)
print(pattern)

#re.escape() --->we use to escape special characters such as (.,*,?..) to terat as noraml character 
#adds backslash before special charcters 
import re

file_name ="data.txt"
g=re.escape(file_name)
print(g)


#Form Validation using re -->Email Validation, Mobile Number Validation ,PANValidation ,Aadhra Validation 

#balajiramireddy@gmail.com ,c,alc1246@gmail.com
user= input("Enter the email id:")
a=re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', user)
print(a)

#Mobile Number Validation 
import re

user =input("Enter the mobile Number ")
b=re.fullmatch(r'[6-9]\d{9}',user)
print(b)
print(b.group())

#PAN Validation 
import re 

user = input("Enter the pan Number ")
s=re.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]{1}',user)
print(s)

#Aadhra Validation  ,PIN Validation 6 digits ,Username Validation (aplphabets ,_,number, no special charaters ) 
import re 
user = input("Enter the Aadhara Number :")
d=re.fullmatch(r'[0-9]{11}\d+',user )
print(d)
'''
#Username Validation (aplphabets ,_,number, no special charaters
import re 

user = input("Enter the User Name :")
s=re.fullmatch(r'[A-Z a-z 0-9 _]{16}$+',user)
print(s)
if s:
    print("Valid User Nmae ")