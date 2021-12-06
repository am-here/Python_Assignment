def rev_num(n):
    rev = 0
    while n != 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return rev


n = eval(input("Enter value of n: "))
if rev_num(n) == n:
    print(n, "is a Palindrome Number")
else:
    print(n, "is not a Palindrome Number")
