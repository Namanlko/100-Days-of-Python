# 1. Lists & List Indexing:
marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

# 2. Negative Indexing in List.
print(marks[-3])            # Negative index
print(marks[len(marks)-3])  # Positive index
print(marks[5-3])           # Positive index
print(marks[2])             # Positive index

# 3. If Condition with List.
if "6" in marks:
  print("Yes")
else:
  print("No")

# 4. Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

# 5. Loops in List
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)