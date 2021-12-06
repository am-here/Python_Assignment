import numpy as np
n = eval(input("Enter size of 1D array: "))
A = np.zeros(n, dtype=int)
B = np.zeros(n, dtype=int)
for i in range(n):
    A[i] = eval(input("Enter Element: "))
for i in range(n):
    B[i] = A[i]
while(1):
    ch = eval(input(
        "\n1. Bubble Sort.\n2. Selection Sort.\n3. Insertion Sort.\n4. Quit.\nEnter choice: "))
    if ch == 1:
        for i in range(n-1):
            for j in range(n-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
    elif ch == 2:
        for i in range(0, n-1):
            pos = i
            for j in range(i+1, n):
                if A[pos] > A[j]:
                    pos = j
            A[i], A[pos] = A[pos], A[i]
    elif ch == 3:
        for i in range(1, n):
            pos = i-1
            val = A[i]
            while pos >= 0 and val < A[pos]:
                A[pos+1] = A[pos]
                pos -= 1
            A[pos+1] = val
    elif ch == 4:
        print("Thank You!")
        break
    else:
        print("\nInvalid Input!")
    print(A)
    for i in range(n):
        A[i] = B[i]
    print("Back to previous values .....", A)
