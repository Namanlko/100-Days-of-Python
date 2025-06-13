# 1. Default Agrumments:
def average1(a, b, c=1):
  print("The average is", (a + b + c) / 2)

average1(2,3)

# 2. Tuple Agrumments:
def average2(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  return sum / len(numbers)

print(average2(1,2))
print(average2(1,2,3))
print(average2(1,2,3,4))
print(average2(1,2,3,4,5))

# 3. Dictionary Agrumments:
def name(**name):
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])
  
name(mname="Buchanan", lname="Barnes", fname="James")