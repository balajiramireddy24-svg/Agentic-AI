# Day 7 Practice - Sets & Dictionaries

# Set Practice
languages = {"Python", "Java", "Python", "C++"}

print("Languages:", languages)

languages.add("JavaScript")
languages.update(["Go", "Rust"])

print("\nUpdated Set:", languages)

backend = {"Python", "Go", "Java"}

print("\nCommon Languages:", languages.intersection(backend))
print("All Languages:", languages.union(backend))

# Dictionary Practice
student = {
    "name": "Pavan",
    "age": 23,
    "course": "Agentic AI"
}

print("\nStudent Details")
print("Name:", student["name"])
print("Course:", student.get("course"))

student["age"] = 24
student["city"] = "Hyderabad"

print("\nUpdated Dictionary:")
print(student)

print("\nKeys:", student.keys())
print("Values:", student.values())

student.pop("city")

print("\nAfter Removing City:")
print(student)

print("\nDay 7 Practice Completed!")
