import numpy as np
n = eval(input("Enter size of 1D array: "))
A = np.zeros(n, dtype=int)
for i in range(n):
    A[i] = eval(input("Enter Element: "))
while(1):
    key = eval(input("\nEnter key: "))
    ch = eval(input(
        "\n1. Linear Search.\n2. Binary Search.\n3. Exit\nEnter choice: "))
    if ch == 1:
        flag = 0
        for i in range(n):
            if A[i] == key:
                print("\nElement found at", i+1)
                flag = 1
        if not flag:
            print("\nElement not found")
    elif ch == 2:
        for i in range(n-1):
            for j in range(n-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        l = 0
        u = n-1
        flag = 0
        while l <= u:
            mid = (l+u)//2
            if A[mid] == key:
                print("\nElement found at", mid+1)
                flag = 1
                break
            elif A[mid] > key:
                u = mid-1
            else:
                l = mid+1
        if not flag:
            print("\nElement not found")
    elif ch == 3:
        print("\nThank You!")
        break
    else:
        print("\nInvalid Input!")
