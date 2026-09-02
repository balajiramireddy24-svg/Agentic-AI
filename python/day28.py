#Day 28 --> Revision --> conditional statements

def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return average, grade


name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = int(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

average, grade = calculate_grade(marks)

print("\n----- Report Card -----")
print("Name:", name)
print("Average:", round(average, 2))
print("Grade:", grade)