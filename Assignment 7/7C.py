W = input("Input: ").split(',')
n = len(W)
for i in range(n-1):
    for j in range(n-i-1):
        if W[j] > W[j+1]:
            W[j], W[j+1] = W[j+1], W[j]
print("Output:", end=" ")
for i in range(n):
    if(i != n-1):
        print(W[i], end=",")
    else:
        print(W[i], end="")
