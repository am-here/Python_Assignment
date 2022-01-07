from math import sqrt
num = int(input("Enter a number: "))
try:
    if(num < 0):
        raise Exception
    print(sqrt(num))
except:
    print("Negative number entered.")
