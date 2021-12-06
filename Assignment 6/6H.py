import numpy as np
M = eval(input("Enter order of 2D array: "))
A = np.zeros([M, M], dtype=int)
for i in range(M):
    for j in range(M):
        A[i, j] = eval(input("Enter Element: "))
print("\nOriginal Matrix\n")
for i in range(M):
    for j in range(M):
        print(A[i, j], end='\t')
    print()
N = (M-2)*(M-2)
B = np.zeros([N], dtype=int)
k = 0
for i in range(1, M-1):
    for j in range(1, M-1):
        B[k] = A[i, j]
        k += 1
for i in range(N-1):
    for j in range(N-i-1):
        if B[j] > B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]
k = 0
for i in range(1, M-1):
    for j in range(1, M-1):
        A[i, j] = B[k]
        k += 1
print("\nRearranged Matrix\n")
for i in range(M):
    for j in range(M):
        print(A[i, j], end='\t')
    print()
sum = 0
print("\nDiagonal Elements\n")
for i in range(M):
    for j in range(M):
        if i == j or i+j == M-1:
            print(A[i, j], end='\t')
            sum += A[i, j]
        else:
            print(' ', end='\t')
    print()
print("\nSum of diagonal =", sum)
