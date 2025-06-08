# 1. For Loop on String:
name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")

 # 2. For Loop on List:   
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

# 3. For Loop with Range Function: 
for k in range(5):
  print(k + 1)

# 4. For Loop with Range Function (2 Parameters): 
for k in range(1, 20001):
  print(k)

# 5. For Loop with Range Function (3 Parameters): 
for k in range(1, 12, 3):
  print(k)