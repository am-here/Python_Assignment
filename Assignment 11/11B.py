def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open('C:\codes\Third Sem\Python Lab\Assignment 11/prime_numbers.txt', 'a')
n = int(input("Enter value of n: "))
i = 2
while n:
    if(isprime(i)):
        file.write(str(i)+"\n")
        n -= 1
    i += 1
file.close()
