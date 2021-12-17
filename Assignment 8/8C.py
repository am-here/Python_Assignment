def rotateList(l, k):
    if k < 0:
        return l
    k %= len(l)
    return l[len(l)-k:]+l[0:len(l)-k]


for i in rotateList(input().split(' '), int(input())):
    print(i, end=' ')
