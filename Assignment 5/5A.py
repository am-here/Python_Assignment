from math import sqrt
n = eval(input("Enter a number: "))
sq = n*n
dup = n
flag = 0
while n != 0:
    d_sq = sq % 10
    d_n = n % 10
    if(d_sq != d_n):
        flag = 1
        break
    sq //= 10
    n //= 10
if not flag:
    print(dup, "is an automorphic number")
else:
    print(dup, "is not an automorphic number")
