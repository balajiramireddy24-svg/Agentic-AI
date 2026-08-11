#Day 15 -- assert , nested loops

#assert keyword --> mainly used for debugging in python
#it checks if the given condition is valid
#if the condition is false it raises an AssertionError

'''
syntax 

assert condition "Error Message" #error message is user degined
'''
'''
x = [1,2,3,4]
assert 3 in x , "not present in x"
x = x + 2
print(f"Updated value is {x}")
'''

#nested loops --> pattern generations
#a nested loop is a loop placed inside another loop
'''
syntax

for i in range(10):
    for j in range(10):
        #statement(s)
        ...
'''
#for every outer inner loop is completely executed
#outer loop controls rows and inner loop controls columns
'''
for i in range(3):
    for j in range(2):
        print(f'value of i is {i}, value of j is {j}')
'''

#number patterns, row based number patterns, column based number pattersn, triangle

#should print
'''
1 2 3
4 5 6
7 8 9

for i in range(3):
    for j in range(1,4):
        print(3 * i + j,end = ' ') #without using extra variable
    print()

z = 1
for i in range(1,4):
    for j in range(1,4):
        print(z,end = " ") #with using extra variable
        z += 1
    print()
'''

#solid rectangle
'''
* * * *
* * * *
* * * *

for i in range(1,4):
    for j in range(1,5):
        print("*",end = " ")
    print()
'''

'''
*
* * 
* * * 
* * * *
'''
'''
for i in range(1,5):
    print("*" * i)

#inverted triangle
* * * *
* * *
* *
* 
#
1
2 3
4 5 6
7 8 9 10
#
A
B C
D E F 
G H I J
K L M N O 
P Q R S T U
'''
