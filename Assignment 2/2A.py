x, y = eval(input("Enter 2 variables: "))
while 1:
    ch = eval(input(
        "1. Swap using 2 variables\n2. Swap using 3 variables\nEnter your choice: "))
    if(ch == 1):
        x, y = y, x
        print("Variable 1 =", x, "\nVariable 2 =", y)
        break
    elif(ch == 2):
        t = x
        x = y
        y = t
        print("Variable 1 =", x, "\nVariable 2 =", y)
        break
    else:
        print("Invalid Input")
