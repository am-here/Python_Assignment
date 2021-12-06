x = eval(input("Enter value of x: "))
n = eval(input("Enter value of n: "))
y = 1
for i in range(n):
    y *= x
print("y = x^n = ", x, "^", n, " = ", y, sep="")
