import numpy as np
s1 = eval(input("Enter size of P array: "))
P = np.zeros(s1, dtype=int)
for i in range(s1):
    P[i] = eval(input("Enter Element: "))
s2 = eval(input("Enter size of Q array: "))
Q = np.zeros(s2, dtype=int)
for i in range(s2):
    Q[i] = eval(input("Enter Element: "))
R = np.zeros(s1+s2, dtype=int)
k = 0
for i in range(s1+s2):
    if(i < s1):
        R[k] = P[i]
    else:
        R[k] = Q[i-s1]
    k += 1
print("R =", R)
