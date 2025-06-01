# 1. Relational Operator:
a = 18
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

# 2. If Statement:
a = 45
if(a>18):
  print("You can drive")
  print("Yes")

# 3. If Else Statement:
applePrice = 10
budget = 200
if (budget - applePrice > 50):
  print("Alexa, add 1 kg Apples to the cart.")
else:
  print("Alexa, do not add Apples to the cart.")

# 4. If Elif Else Statement:
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

# 5. Nested If Elif Else Statement:
num = 18
if (num < 0):
  print("Number is negative.")
elif (num > 0):
  if (num <= 10):
    print("Number is between 1-10")
  elif (num > 10 and num <= 20):
    print("Number is between 11-20")
  else:
    print("Number is greater than 20")
else:
  print("Number is zero")
