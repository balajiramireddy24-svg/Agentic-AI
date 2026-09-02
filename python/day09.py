# Day 9 - Revision Practice

student = {
    "name": "Pavan",
    "course": "Agentic AI",
    "skills": ["Python", "Git"],
    "completed_days": {1, 2, 3, 4, 5, 6, 7, 8}
}

print("Student:", student["name"])
print("Course:", student["course"])

student["skills"].append("Problem Solving")

print("\nSkills:")
for skill in student["skills"]:
    print("-", skill)

print("\nDays Completed:", sorted(student["completed_days"]))

message = "learning python every day"

print("\nMessage:", message.title())
print("Length:", len(message))

print("\nDay 9 Revision Completed!")
