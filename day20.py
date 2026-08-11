# Day 20 --> Recursive Functions and Anonymous Functions

#Recursive Function raises Recursive error
#Recursive Function -->  A function calling itself, where it makes the smaller problem is broken into multiple times
#Depends on two cases --> base case (it indicates when to stop the base condition)
#Recursive Case --> (it makes the problem to repeat itself)
'''
syntax:

def function():
    if base_condition:
        return
    function() #we write out recursive function

function()
'''
'''
def test():
    """Without base Case"""
    return test()

print(test())
'''
#factorial --> the multiplications of numbers and all the numbers less than it till 1
#  5! --> 5 * (5-1) * (5-2) * (5-3) * (5-4)
#factorial using recursion
'''
def factorial(n):
    """factorial of n using recursion"""
    if n < 0:
        print("Factorial Does not exist for Negetive Numbers")
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

print(factorial(-5))
'''
#Sum of natural numbers
'''
def natural_sum(n):
    """Finds the sum of n natural numbers"""
    if n > 0:
        return n + natural_sum(n-1)
    elif n <= 0:
        return 0

print(natural_sum(10))
'''
#Task : Build a simple choice menu
#1. Recursion logic for factorial
#2. Sum of numbers
#3. Bmi Calculator
#4. Fibonacci series
#5. Atm simulation

#Anonymous Functions --> Short defined functions, Nameless functions
#we define them using lambda keyword
#filter() and map()

#create a function to return the area of triangle
'''
def area(length,breadth):
    """return the area of rectangle"""
    return length * breadth

print(area(6,10))
'''

#using anonymous function

#syntax : var_name = lambda parameters : expression
'''
area = lambda length,breadth : length * breadth
print(area(5,6))
'''
'''
#area of square
area = lambda side : side ** 2
print(area(int(input("Enter side of square:"))))
'''
#user registration in a web page --> name
#first name --> input
#last name --> input
'''
#user defined
def fullname():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    return f"{first.title()} {last.title()}"

print(fullname())
#anonymous
full_name = lambda first,last : f"{first.title()} {last.title()}"
print(full_name("pavan","pusapati"))
'''
'''
#to check for even or odd
n = int(input("Enter a number"))
result = lambda n : "Even" if n % 2 == 0 else "Odd"
print(result(n))
'''
'''
#length of a string
name = input("enter a message:")
result = lambda name : len(name)
'''

#filter(),map()
#yeilding the value from the iterable
'''
# list of integers
a = list(map(int,input().split()))
print(a)
#filter only even numbers
b = list(filter(lambda x:x%2 == 0,a))
print(b)
'''
'''
names = ['Pavan','Abhiram','Nihanth','Saikiran','Roshan','Vasanthi','Manimala']

N = list(filter(lambda x : len(x) > 6,names))
print(N)
'''
'''
#map() --> it will apply for every value from multiple idterables 
a = list(map(lambda name:name.uuper(),names))
print(result)
'''
'''
prices = [1000,2500,3500,4000]
final_price = list(map(lambda price : (price - price * 0.1),prices))
print(final_price)
'''

#reduce() --> this makes complete iterable to be a single value --> functools

from functools import reduce

numbers = [1,4,5,7,8]
result = reduce(lambda number,sum : number + sum , numbers)
print(result)