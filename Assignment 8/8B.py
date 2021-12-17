from math import sqrt


def isperfect(num):
    return (num == int(sqrt(num))**2 and num)


def sumofsquares(num):
    for i in range(1, int(sqrt(num))):
        if(isperfect(num-(i**2))):
            return True
    return False


print(sumofsquares(int(input("Enter Number: "))))