#Day 22 --> Modules

#Modules --> user defined module --> create, accessing
#Built in modules --> os, sys, random, math, platform, collection, itertools...Etc
#A module is a python file
# to access a module we use the keyword import

#import my_module
'''
print(dir(my_module)) #use dir to get available methods and attributes
#accessing from module

print(my_module.greet("pavan"))

my_module.names.update({'place':'hyd','age':7})
print(my_module.names)

#accessing method/attributes using from keyword
#from my_module import greet
print(greet('agents'))
print(names) #nameerror as we did not import it
from my_module import greet,names

print(names)
print(display) #again raises a name error

""" this is my module"""
#to access all methods/attributes we use * 
#recommended only for userdefined/simple modules

from my_module import *

print(greet('saketh'))
names.update({"course":"AAA"})
print(names)
# y = fun()
# print(next(y))
print(__name__)
print(__doc__)
'''
'''
import math
print(dir(math))
print(math.__doc__) #it gives description about the module
print(math.ceil(2.1)) #it returns the next higher value --> int
print(math.floor(2.1)) #it returns the lower value of given value --> int
print(math.e) #returns experimental value
print(math.factorial()) #returns the factorial of the number
'''
# and some other methods like fmod, modf, pow, truncate,pi, log2,log10,log, etc

#os module 
#provides functions to interact with operating system
'''
import os
#print(len(dir(os)))

print(os.getcwd()) #returns the current working directory
print(os.chdir('/home/workspace/my-project')) #changes the current working directory
print(os.getcwd()) 
print(os.listdir()) #lists out all the objects in the directory
for i in os.listdir():
    print(i)

# print(os.mkdir('sample'))  #creates a directory
print(os.rmdir('sample')) #removes a directory
'''
'''
import sys
print(sys.path) #gives complete root path
'''

#random module --> to generate random data

import random,time
print(len(dir(random)))

print(random.random())

#used for otp generation

for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(1) #used for time intervals


