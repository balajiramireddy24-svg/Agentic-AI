#Day 17 -- Recap of controls blocks, Exception handling and Introduction to Procedure oriented Programming
#BMI use case, using control block statements
#bmi --> body mass index, bmi = weight (kgs)/ (height**2)(meters)
'''
while True:
    print("\t1. Check BMI \n\t2. Exit \n\tSelect 1 or 2:")
    n = int(input())
    print()
    if n == 1:
        name = input("Enter your name:")
        while True:
            try:
                weight = float(input("Enter weight in kgs:"))
                height = float(input("Enter height in meters:"))
                if weight < 0 and height < 0:
                    print("Enter only positive values")
                else:
                    bmi = weight / (height ** 2)
                    if bmi < 18.5:
                        print("Underweight")
                    elif 18.5 <= bmi <= 24.9:
                        print("Healty")
                    elif 25 <= bmi <= 29.9:
                        print("Overweight")
                    elif bmi >= 30:
                        print("Obesity")
                    print()
                    break
            except ValueError:
                print("Make sure to enter only valid input")
            except ZeroDivisionError:
                print("Do Not enter zeros for weight and height")
    elif n == 2:
        break
'''
# POP --> Procedure oriented Programming --> functions
#Funtions --> A function is a block of code (statements) which perform a specific task
#it is a reusable code --> for readability,reusability and easy to maintain
#user defined functions --> def
#Built in function --> python by default
#Anonymous functions --> lambda (map,filter,reduce)
#recursive functions --> factorial, fibonacci, --> decorators

'''
functions

syntax

def fname(parameters): --> function header
    """ Doc string (Description of function) """
    statements(s) --> body of function
    return value(s)...


fname(arguments) --> function call
'''
#sample function
'''
def add(a,b):
    """returns the sum of a and b"""
    return a + b

result = add(1,2)
print(result)
'''
#what surprised me : i didnt know functions could have doc strings until now
'''
parameters --> categories
1. positional arguments --> count of arguments to be matched
2. defualt arguments --> we can make arguments as defualt
3. keyword arguments --> order/keyword name to be matched
4. variable length arguments(*args) --> we can pass any number of positional arguments can be given
5. keyword variable length arguments (**kwargs) --> we can pass any number of keyword arguments
'''

#positional arguments --> the parameter count should definately match the count of arguments in function call
#default arguments:
'''
a default argument usually is when a user does not mention a value in arguments, it takes a default set argument
you can have multiple default parameters in a function
but default parameters should follow the non default arguments,
which means if the default argument is present
all the parameters can be default
if not the default arguments should follow the non default arguments
'''

#keyword arguments -->
#either the order of the parameters should match, or else the keyword names should match
