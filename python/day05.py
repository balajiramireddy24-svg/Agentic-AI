# Day 5 Practice - String Operations

text = input("Enter a sentence: ")

print("\nOriginal Text:", text)

# Basic String Methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Length:", len(text))

# Indexing & Slicing
print("\nFirst Character:", text[0])
print("Last Character:", text[-1])
print("First 5 Characters:", text[:5])

# Searching
print("\nIndex of 'a':", text.find("a"))
print("Number of 'a':", text.count("a"))

# Replace
new_text = text.replace("Python", "Agentic AI")
print("\nAfter Replace:", new_text)

# Split & Join
words = text.split()
print("\nWords:", words)

joined = "-".join(words)
print("Joined with '-':", joined)

# Checking
print("\nStarts with 'P':", text.startswith("P"))
print("Ends with '.':", text.endswith("."))
print("Contains 'AI'?", "AI" in text)

# Removing Spaces
print("\nWithout extra spaces:", text.strip())

print("\nDay 5 Practice Completed!")
