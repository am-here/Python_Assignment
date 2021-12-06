print("All the special numbers within range 100 to 999 are:")
for i in range(100, 1000):
    n = i
    sum = 0
    while n != 0:
        d = n % 10
        fact = 1
        for j in range(1, d+1):
            fact *= j
        sum += fact
        n //= 10
    if i == sum:
        print(i, end=" ")
