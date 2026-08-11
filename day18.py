#Day 18 --> *args, **kwargs and scope of a variable

#Variable length arguments --> we can define any number of positional arguments
#python stores these arguments by default in tuples
#we use * notation to define variable length arguments
'''
def sample(args):
    """usage of variable length arguments"""
    print(args)
    print(type(args))

args = 1
sample(args)
'''
'''
def add(*a):
    """adds only integers and floats from the given collection"""
    result = 0
    for i in a:
        if type(i) in [int,float]:
            result += i
    return result
print(add(1,4,'codegnan',2.3,34,2.5,2+4j))
'''

# keyword variable length arguments --> Any number of keyword arguments can be passed to the function
#arguments are stored in dictionary
#we call it kwargs and we denote it with **
'''
def sample(**kwargs):
    """usage of keyword variable length arguments"""
    print(kwargs)
    print(type(kwargs))

sample()
sample(name="pavan",age=20,course="AAI")
'''
'''
def grocery(**items):
    """Grocery list"""
    print(items)
    for key,value in items.items():
        print(f"{key}:{value}")

grocery(name='milk',price=35,quantity=1000,brand='abc')
'''
'''
def bmi_checker(**details):
    bmi = details['weight'] / (details['height']**2)
    print(f"Your bmi value is {bmi}")
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Healty")
    elif 25 <= bmi <= 29.9:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")

bmi_checker(name = 'pavan',weight = 70,height = 1.6)
'''

#Scope of the variable
#the field where the variable can be accessible
#they are Local Variables, Global Variables, Global Keyword usage, enclosing variables (non local keyword)

#Local Variable
#the variables are defined to that function and cannot be accesed outside the function
'''
def fname():
    """usage of local variables"""
    name = "codegnan" #local variable
    return name

print(fname())
print(name)
'''

#Global Variable
#The global variables are initialized outside the functions and is accessible through the entire program and in all functions
'''
name = 'codegnan' #this is a global scope variable accessible all over the program
def uname():
    """Global Scope of the variable"""
    name = "Pavan"
    return name

print(uname())
print(name)
'''
'''
count = 15
def update_hello():
    "Usage of global variable"""
    global count
    count = count + 10
    return count
print(update_hello())
print(f"updated value of count is {count}")
'''

#Enclosing Scope --> non local keyword --> nested functions
'''
def outer():
    """Outer function"""
    count = 10
    def inner():
        nonlocal count
        count = count + 5
        return count
    print(inner())
    return count
print(outer())

#LEGB --> local scope,enclosing scope,global,built-ins
#built in scope --> builtin function can be used as variables but it overrides it behaviour
#(should be avoided)

len = 34 #overrides its functionality and is now just a variable
print(len)
'''


