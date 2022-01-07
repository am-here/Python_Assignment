a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
try:

    if not (a.isdigit() and b.isdigit()):
        raise Exception
    print(int(a)+int(b))
except:
    print("Non-number value is given as input!")
