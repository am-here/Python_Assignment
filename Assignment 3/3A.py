a, b, c = eval(input("Enter 3 numbers: "))
if a >= b:
    if a >= c:
        print("The greatest number among", a, b, "and", c, "is:", a)
    else:
        print("The greatest number among", a, b, "and", c, "is:", c)
else:
    if b >= c:
        print("The greatest number among", a, b, "and", c, "is:", b)
    else:
        print("The greatest number among", a, b, "and", c, "is:", c)
