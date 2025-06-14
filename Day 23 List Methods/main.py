# 1. List Data Type:
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

# 2. Append Function:
l.append(7)
print(l)

# 3. Sort Function:
l.sort(reverse=True)
print(l)

# 4. Reverse Function:
l.reverse()
print(l)

# 5. Index Function: Return the index of first occurence of a given number.
print(l.index(11))

# 6. Count Function: Return the count of how my times a number occured.
print(l.count(1))

# 7. Copy Function: Return the copy of the list.
m = l.copy()
print(m)

# 8. It is creating a reference of l. If we are updating the value of m then it will reflect in l as well.
m = l
m[0] = 0
print(l)

# 9. Insert Function: l.insert(index, value): It will insert the given value to the given index.
l.insert(1, 899)
print(l)

# 10. Here we are concatinating two lists. Elements of list m will be added at the end of list l. Same thing we can do with the help of extend function.
m = [900, 1000, 1100]
k = l + m
print(k)

# 11. Extend Function: It is used to extend a list with the element of given list. All the elements of given list will be inserted at the list of list.
n = [1,2,3,4,5]
l.extend(n)
print(l)