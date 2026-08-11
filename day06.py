# Day 6 Practice - Lists & Tuples

# List Practice
fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

fruits.append("Orange")
fruits.insert(1, "Grapes")
fruits.remove("Banana")

print("Updated List:", fruits)

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
print("Sliced List:", fruits[1:])

fruits.sort()
print("Sorted List:", fruits)

fruits.reverse()
print("Reversed List:", fruits)

# Tuple Practice
marks = (85, 90, 95)

print("\nTuple:", marks)
print("First Mark:", marks[0])
print("Highest Mark:", max(marks))
print("Total Marks:", sum(marks))

maths, science, english = marks

print("\nMaths:", maths)
print("Science:", science)
print("English:", english)

print("\nDay 6 Practice Completed!")
