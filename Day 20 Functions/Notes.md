# Day 20: Python Functions
Function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

- Built In Functions
- User Defined Functions
 

 ### Built In Functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

```python
1. min()
2. max() 
3. len() 
4. sum() 
5. type() 
6. range() 
7. dict() 
8. list() 
9. tuple() 
10. set()
11. print()
```

### User Defined Functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

**Syntax:**
```python
def function_name(parameters):
  pass
  # Code and Statements
```
 
- Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
 - Any parameters and arguments should be placed within the parentheses.
 - Rules to naming function are similar to that of naming variables.
 - Any statements and other code within the function should be indented.

### Calling a Function:

We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

**Example:**
```python
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```
**Output:**
```
Hello, Sam Wilson
```