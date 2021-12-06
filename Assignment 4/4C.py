def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x = eval(input("Enter lower bound of range(inclusive): "))
y = eval(input("Enter upper bound of range(inclusive): "))
print("Prime Numbers between", x, "and", y, "(inclusive) are:")
for i in range(x, y+1):
    if(isprime(i)):
        print(i, end=" ")
