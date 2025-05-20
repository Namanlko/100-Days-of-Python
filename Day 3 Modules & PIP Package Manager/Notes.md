# Day 3: Modules & PIP Package Manager

### What is Modules?

Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python.

    1. Built in Modules
    2. External Modules

### What is Built in Modules? 

Built-in modules are ready to import and use and ships with the python interpreter. There is no need to install such modules explicitly.

### What is External Modules?

Externals modules are imported from a third party file or can be installed using a package manager like pip. Since this code is written by someone else, we can install different versions of a same module with time.

### What is Pip Package Manager?

Pip is a package manager for python. We can use pip to install a module on our system. 

**Ex:** ```
pip install pandas ```

We use the import syntax to import a module in Python. Here is an example code:

```
import pandas 
#Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) #This will display first few rows from the words.csv file. 
``` 
**Note:** Similarly we can install other modules and look into their documentation for usage instructions.