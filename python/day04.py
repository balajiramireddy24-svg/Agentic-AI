# Day 4 Practice - Operators & Input

name = input("Enter your name: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"\nHello, {name}!")

print("\nArithmetic Operations")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("\nComparison Operations")
print("Are both numbers equal?", num1 == num2)
print("Is first number greater?", num1 > num2)

print("\nLogical Operations")
print((num1 > 0) and (num2 > 0))
print((num1 > 10) or (num2 > 10))

print("\nThank you for trying my Day 4 practice program!")
