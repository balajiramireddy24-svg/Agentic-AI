#Day 26 --> file handling and exception handling

#File handling

#store the data --> files(.txt files) --> open()
#file modes --> 'r',w','a'
'''
syntax
open("file_name",'mode') #default mode is usually read mode
'''
'''
file = open('new_file.txt').readline()
print(file)
'''

import os
'''
if os.path.exists('new_file.txt'):
    f = open('new_file.txt').read()
    print(f)
    print(f"file is already present")
else:
    print("file not found")

file_path  = 'new_file.txt'
if os.path.exists(file_path):
    print(f'file size is {os.path.getsize(file_path)} bytes')
    print(f'file absolute path is {os.path.abspath(file_path)}')

#'w' mode --> if a file exists the it overwrites the file, if it doesnot exist then it creates the file and writes the content to the file
a = open('new_file.txt','w')
print(a)
a.write("AAA-HYD-001")
a.write('\nBatch number of agentic ai course')
a.writelines("Agentic Ai is the big thing happening. \t the world is progressing")
a.close()
'''
'''
with open('new_file.txt','r+') as file:
    file.write("yes w+ can allow both read and write")
    print(file.readline())

with open('new_file.txt','a') as f:
    f.write('\nwhen using with keyword to access files, you dont need to specify a close()')
    print(f)

with open('rag.txt','a') as f:
    f.writelines("Agents")

d = os.listdir() #returns the list of all directories and files
for file in d:
    if file.endswith('.txt'):
        print(file)
'''

#Exception Handling
'''
syntax
try:
    base statement() which may raise error
except expected error name:
    statement incase error occurs
finally:
    statements
'''

#type error, value error, index error, arithmetic error, zerodivision error, attribute error
'''
try:
    a,b = map(int,input().split())
    result = a / b
    print(f'result is {result}')
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Only give interger values")
finally:
    print("Anyways this will be printed..")
'''

#exceptions together

try:
    a,b = map(int,input().split())
    result = a / b
    print(f'result is {result}')
except (ZeroDivisionError,ValueError) as e:
    print(f'the error occured is {e}')
