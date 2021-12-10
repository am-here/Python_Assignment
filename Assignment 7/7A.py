a = b = 0
for i in input("Input: "):
    if i.isupper():
        a += 1
    if i.islower():
        b += 1
print("Output:", a, b)
