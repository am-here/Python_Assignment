import numpy as np
a = eval(input("Enter size of 1D array: "))
One_D = np.zeros(a, dtype=int)
for i in range(a):
    One_D[i] = eval(input("Enter Element: "))
m = eval(input("Enter rows of 2D array: "))
n = eval(input("Enter columns of 2D array: "))
Two_D = np.zeros([m, n], dtype=int)
for i in range(m):
    for j in range(n):
        Two_D[i, j] = eval(input("Enter Element: "))

while(1):
    ch = eval(input("1. Get the largest element from your 1D Array.\n2. Get the smallest element from your 1D Array.\n3. Get the largest element from your 2D Array.\n4. Get the smallest element from your 2D Array.\nEnter choice: "))
    if ch == 1:
        m = One_D[0]
        for i in range(a):
            m = max(m, One_D[i])
        print("Maximum Number:", m)
        # break
    elif ch == 2:
        m = One_D[0]
        for i in range(a):
            m = min(m, One_D[i])
        print("Minimum Number:", m)
        # break
    elif ch == 3:
        mm = Two_D[0, 0]
        for i in range(m):
            for j in range(n):
                mm = max(mm, Two_D[i, j])
        print("Maximum Number:", mm)
        # break
    elif ch == 4:
        mm = Two_D[0, 0]
        for i in range(m):
            for j in range(n):
                mm = min(mm, Two_D[i, j])
        print("Minimum Number:", mm)
        # break
    else:
        print("\nInvalid Input!")
        break
