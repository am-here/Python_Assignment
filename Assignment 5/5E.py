n = eval(input("Enter a number: "))
size = 0
dup = n
# calculating number of digits in the number
while dup != 0:
    size += 1
    dup //= 10
print("The new numbers formed after shifting of digits are: ")
print(n, end=" - ")
flag = 0
s = n
for i in range(size):
    dup = s
    f_dig = dup % 10  # first number
    r_num = dup//10  # remaining number
    s = f_dig*pow(10, (size-1))+r_num
    if i != size-1:
        print(s, end=" - ")
    # prime checking
    for j in range(2, s):
        if (s % j) == 0:
            flag += 1
            break
if not flag:
    print("[", n, " is a Circular Prime]", sep='')
else:
    print("[", n, " is not a Circular Prime]", sep='')
