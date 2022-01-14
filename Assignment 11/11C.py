file = open(
    'C:\codes\Third Sem\Python Lab\Assignment 11/fibbonacci_series.txt', 'a')
n = int(input("Enter value of n: "))
a = 0
b = 1
for i in range(n):
    file.write(str(a)+"\n")
    c = a+b
    a = b
    b = c
file.close()
