def wellbracketed(s):
    b = 0
    for i in s:
        if i == '(':
            b += 1
        if i == ')':
            b -= 1
        if b < 0:
            return False
    return(b == 0)


print(wellbracketed(input("Input: ")))
