def append_Middle(s1, s2):
    return (s1[:len(s1)//2]+s2+s1[len(s1)//2:])


print(append_Middle(input("String s1: "), input("String s2: ")))
