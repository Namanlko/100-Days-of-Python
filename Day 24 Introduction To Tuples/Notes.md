# Day 24: Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

**Example 1:**
```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```
**Output:**
```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```

**Example 2:**
```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```
**Output:**
```
('Abhijeet', 18, 'FYBScIT', 9.8)
```

### Tuple Indexing:
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

**Example:**
```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]              
 ```

### Accessing Tuple Items:
 
**1. Positive Indexing:**
As we have seen that tuple items have index, as such we can access items using these indexes.

**Example:**
```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])
print(country[1])
print(country[2])
```
**Output:**
```
Spain
Italy
India
 ```

**2. Negative Indexing:**
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

**Example:**
```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
```
**Output:**
```
Germany
India
Italy
 ```

## Check for Item:
We can check if a given item is present in the tuple. This is done using the `in` keyword.

**Example 1:**
```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
  ```
**Output:**
```
Germany is present.
 ```

**Example 2:**
```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
  ```
**Output:**
```
Russia is absent.
 ```

## Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

**Syntax:**
```python
Tuple[start : end : jumpIndex]
```
**Note:** Jump Index is optional. We will see this in given examples.

**Example:**
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
```
**Output:**
```
('mouse', 'pig', 'horse', 'donkey')
('bat', 'mouse', 'pig', 'horse', 'donkey')
```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. 

**Note:** The element of the end index provided will not be included.

**Example:**
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
```
**Output:**
```
('pig', 'horse', 'donkey', 'goat', 'cow')
('horse', 'donkey', 'goat', 'cow') 
```
When no end index is provided, the interpreter prints all the values till the end.

**Example:**
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
```
**Output:**
```
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
```
When no start index is provided, the interpreter prints all the values from start up to the end index provided. 

**Example:**
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
```
**Output:**
```
('cat', 'bat', 'pig', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')
```
Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed. 

**Example:**
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
```
**Output:**
```
('dog', 'pig', 'goat')
```
Here, Jump index is 3. Hence it prints every 3rd element within given index.