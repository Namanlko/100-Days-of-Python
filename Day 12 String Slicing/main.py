# 1. String slicing is a technique in Python used to extract a portion of a string by specifying a range of indices. It allows you to access a substring from a string using a start index, an end index, and optionally a step value.

# 2. Example 1.
# Define a string variable 'fruit' with the value "Mango"
fruit = "Mango"

# Get the length of the string "Mango" (which is 5) and store it in mangoLen
mangoLen = len(fruit)
# Print the length of the string
print(mangoLen)  # Output: 5

# Slice from index 0 to 3 (includes 0, 1, 2, 3 but excludes 4), gives "Mang"
print(fruit[0:4])  # Output: "Mang"

# Slice from index 1 to 3 (includes 1, 2, 3 but excludes 4), gives "ang"
print(fruit[1:4])  # Output: "ang"

# Slice from start (index 0) to 4 (includes 0, 1, 2, 3, 4), gives "Mango"
print(fruit[:5])  # Output: "Mango"

# Slice from index 0 to -3 (equivalent to len(fruit)-3=2), gives "Man"
print(fruit[0:-3])  # Output: "Man"

# Same as above, explicitly using len(fruit)-3=2, gives "Man"
print(fruit[:len(fruit)-3])  # Output: "Man"

# Slice from index -1 (last character) to -3 (len(fruit)-3=2), but since -1 is after -3, gives empty string
print(fruit[-1:len(fruit)-3])  # Output: ""

# Slice from index -3 (3rd from end, 'n') to -1 (excludes last character), gives "ng"
print(fruit[-3:-1])  # Output: "ng"

# 3. Example 2.
text = "Hello, World!"

# Basic slicing
print(text[0:5])  # Output: "Hello" (from index 0 to 4)
print(text[7:12]) # Output: "World" (from index 7 to 11)

# Omitting start or end
print(text[:5])   # Output: "Hello" (from start to index 4)
print(text[7:])   # Output: "World!" (from index 7 to end)

# Using step
print(text[::2])  # Output: "Hlo ol!" (every second character)
print(text[::-1]) # Output: "!dlroW ,olleH" (reverses the string)

# Negative indices
print(text[-6:-1]) # Output: "World" (from 6th last to 2nd last character)

# Quick Quiz:
# nm = "Harry"
# print(nm[-4:-2])
# @codewithharry
