# 1. Function Example 1.
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

a = 9
b = 8
calculateGmean(a, b)

# 2. Function Example 2.
def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

c = 8
d = 74
isGreater(c, d)

# 3. Pass Statement: Pass statement is a no operation statement. It does nothing when executed. It's used as a placeholder in blocks of code where a statement is syntactically required but you don't want to do anything yet.

def isLesser(a, b):
  pass
  