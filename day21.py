#Day 21 --> List comprehension

#List Comprehension --> In python its a precise / easiest way to create lists
'''
Syntax : [expression for item in iterable]
Iterable --> list,tuple,set,dict or range()
'''
'''
lst = []
for i in range(10):
    lst.append(i)
print(lst)

#using list comprehension
lst = [i**2 for i in range(10)]
print(lst)
'''
'''
#Converting string to uppercase
details = ['saketh','codegnan','data','agents','rag']
new_details = [i.title() for i in details]
print(new_details)
'''
'''
a,*name,c = 1,'saketh','codegnan','data',34
print(a)
print(*name)
print(c)
'''
'''
a = [15,20,25,35]
#update the list with each value by 5
a = [i+5 for i in a]
print(a)

#get the first letter of each object in collection
data = ['codegnan','agents','rag']
letter = [i[0] for i in data]
print(letter)
'''

#list comprehension with if usage
# [expression for item in iterable/range if condition]
'''
#Even number from the collection
collection = list(map(int,input("Enter the values :").split(",")))
print(collection)
result = {i for i in collection if i % 2 == 0}
print(result)
'''
'''
#using filter
collection = list(map(int,input("Enter the values :").split(",")))
result = list(filter(lambda x : x % 2 == 0,collection))
print(result)

#fetch desired values with condition satisfied
collection = list(map(int,input("Enter the values :").split(",")))
final = [i for i in collection if i > 10]
print(final)
'''
'''
#list comprehension with if else conditional
#syntax : [true_value if condition else false_value for item in iterable]

data = [12,3,4,6,7,9]
result = ["Even" if i % 2 == 0 else "Odd" for i in data]
print(result)
'''

#nested list comprehension
#nested --> one inside another (one loop inside another loop)
#[expression for i in iterable1 for j in iterable2]
'''
b = [4,5,6]
c = [7,8,9]
a = [(i,j) for i in b for j in c]
print(a)
'''
'''
#multiplication table
n = int(input("Enter a number:"))
table = [str(n) + " * " + str(i) + " = " + str(n * i) for i in range(1,11) if i != n]

for i in table:
    print(i)
'''

#nested loops with if else in list comprehension

#[true value if condition else false_value for item1 in iterabel for item2 in iterabel]
'''
a = [1,3,5,6,7]
b = [2,4,6,8,9]
c = [x + 5 if x < y else x for x in a for y in b]
print(c)
'''

#tuple comprehension does not exist
#instead when we use () brackets for comprehension, we get a generator object
#generator is a special function that generates one value at a time
#we use yield keyword

#Normal function
'''
def fname():
    """doc string"""
    return value(s)
fname()

def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3

fname()

def fun():
    """Normal function"""
    return [1,2,4,5,6]

print(fun())

a = fun()
for i in a:
    print(i)

def fun():
    """Generator function"""
    yield 1
    yield 2

b = fun()
print(next(b))
print(next(b))
print(next(b))
'''

def display():
    """subjects covered"""
    yield "Python"
    yield "GenAI"
    yield "rag"
    yield "agents"

print(display())
print(type(display()))
d = display()
print(next(d))
print(next(d))
print(next(d))
print(next(d))