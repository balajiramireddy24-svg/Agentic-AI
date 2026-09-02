#Day 16 --> Advanced Pattens

'''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5

temp = 1
for i in range(1,6):
    for j in range(1,i + 1):
        print(j,end = " ")
    print()
'''
'''
A
A B
A B C
A B C D
A B C D E

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end = " ")
    print()
'''
'''
     *
    * * 
   * * * 
  * * * * 
 * * * * *

z = 5
for i in range(1,z+1):
    for j in range(1,z+1):
        if j <= z-i:
            print(" ",end = "")
        else:
            print("*",end = " ")
    print()
'''
#task 
'''
     *
    * * 
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''