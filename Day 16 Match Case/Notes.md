# Day 16: Match Case Statement
Match Case statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.


**Syntax:**
```python
match variable_name:
    case ‘pattern1’ : //Statement1
    case ‘pattern2’ : //Statement2
    …            
    case ‘pattern n’ : //Statement n
    case _: //Default Value
```

**Example:**
```python
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
```
### Output:
```
x % 2 == 0 and case is 4
```