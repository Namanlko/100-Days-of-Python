# 1. Match Case: Match Case is a pattern matching feature introduced in Python 3.10. It's similar to switch statements in other languages, but much more powerful. It allows you to compare a value against different patterns and execute code depending on which pattern matches.

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is Zero.")
    # case with if-condition
    case 4:
        print("Case is 4.")
    case _ if x!=90:
        print(x, "is not 90.")
    case _ if x!=80:
        print(x, "is not 80.")
    case _:
        print(x)