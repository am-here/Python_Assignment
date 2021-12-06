while(1):
    ch = eval(input("1. Pattern 1.\n2. Pattern 2.\n3. Pattern 3.\n\nEnter choice: "))
    if ch == 1:
        n = eval(input("Enter size: "))
        s, e = 1, n
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s == j or e == j:
                    print("$", end=" ")
                elif i == 1 or i == n or j == 1 or j == n:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            s += 1
            e -= 1
            print()
        break
    elif ch == 2:
        s = ord('A')
        n = input("Enter the end character(not greater than 'Z'): ")
        while(n < 'A' or n > 'Z'):
            print("Wrong Input!")
            n = input("Enter the end character(not greater than 'Z'): ")
        n = ord(n)
        e = n
        sp = -1
        for i in range(s, n+1):
            for j in range(s, e+1):
                print(chr(j), end=" ")
            for j in range(1, sp+1):
                print(" ", end=" ")
            for j in range(e, s-1, -1):
                if j != n:
                    print(chr(j), end=" ")
            sp += 2
            e -= 1
            print()
        break
    elif ch == 3:
        s = 1
        e = eval(input("Input the end number: "))
        sp = e
        for i in range(e):
            sp -= 1
            for j in range(sp):
                print(" ", end=" ")
            for j in range(s):
                print(j+1, end=" ")
            s += 1
            print()
        break
    else:
        print("\nInvalid Input!\nTry Again!\n")
        break
