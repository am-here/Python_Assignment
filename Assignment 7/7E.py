def wellbracketed(s):
    depth = 0
    for i in s:
        if i == '(':
            depth += 1
        if i == ')':
            depth -= 1
        if depth < 0:
            return False
    return(depth == 0)


print(wellbracketed(input("Input: ")))
