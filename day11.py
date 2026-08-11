#Day 11 -- Control statements
#statements in program that control the execution of a program
#conditional statements --> (if,else,elif)
#Repitition statements --> (loops)
#jumping statements --> break,continue,pass,assert

#if statement

money = int(input("Enter the billing value :"))
if money <= 100:
    print(f"now you are eligible to get your items")   
print("check again")

students = ['ram','akash','abhi','mani']
name = input("Enter the student name:").lower()
if name in students:
    marks = 50
    grade = "A"
    print(f'{name} has secured {marks} marks and {grade} Grade')

#Syntax of if else conditional

if condition:
    statement(s)
    ....
    ...
    ..
    .
else:
    statements(s)
    ...
    ..
    .

#vote eligibility

age = int(input("Enter Your age:"))
if age >= 18:
    print(f"Your age is {age} years,Therefore, you are Eligible to Vote")
elif age < 18:
    print(f"Your age is {age}, Therefore you need to wait for {18 - age} to become eligible")
'''

#if-elif conditional
age = int(input("Enter your age:"))
if age >= 18:
    print(f"Your age is {age} years,Therefore, you are Eligible to Vote")
elif 1 < age < 18:
    print(f"Your age is {age}, Therefore you need to wait for {18 - age} to become eligible")
else:
    print("Enter only positive numbers")




















