m = eval(input("Enter the value of m: "))
n = eval(input("Enter the value of n: "))
count = 0
print("Composite magic integers are ", end='')
for i in range(m, n+1):
    flag = 0
    # for composite
    for j in range(2, i):
        if (i % j) == 0:
            flag += 1
            break
    # for magic
    num = i
    while(num > 9):
        sum = 0
        while(num != 0):
            sum = sum+(num % 10)
            num //= 10
        num = sum
    if num == 1:
        flag += 1
    # checking for both
    if flag == 2:
        print(i, end=', ')
        count += 1
print("\nFrequency of composite magic integers is ", count)
