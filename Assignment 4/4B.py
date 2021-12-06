n = eval(input("Enter value of n: "))
a = 0
b = 1
c = 0
for i in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c
