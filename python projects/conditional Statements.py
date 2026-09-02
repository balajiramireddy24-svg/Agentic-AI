# Nested System
marks = int(input("Enter marks: "))

if marks > 100 or marks >0:
    if marks >= 90:
        print("Grade: A")
        print("Remark: Outstanding!")
    elif marks >= 80:
            print("Grade: B")
            print("Remark: Excellent!")
    elif marks >= 70:
                print("Grade: C")
                print("Remark: Good")
    elif marks >= 60:
                    print("Grade: D")
                    print("Remark: Fair, needs improvement")
    elif marks >= 50:
                        print("Grade: E")
                        print("Remark: Poor, needs serious improvement")
    elif marks >= 0:
                            print("Grade: F")
                            print("Remark: Failed, needs to reappear")
else:
    print("Invalid marks entered")
Grade: B
Remark: Excellent!
# Even-Odd Checker 

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 =0 :
         print("Negative Even Number")
    else:
         print("Negative Odd Number")
    elif num == 0:
    print("Zero is neither odd or even")
    if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
            
else:
    print("Inavlid")
Even Number
# 3. Season Identifier

month = int(input("Enter month number: "))

if month > 1 or month > 12:
    if month == 12 or month == 1 or month == 2:
        print("Season: Winter")
    elif month == 3 or month == 4 or month == 5:
        print("Season: Spring")
    elif month == 6 or month == 7 or month == 8:
        print("Season: Summer")
    else:
        print("Season: Autumn")
else:
    print("Invalid month entered")
Season: Spring
 
