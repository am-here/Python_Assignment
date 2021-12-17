def matmult(A, B):
    ans = []
    for i in range(len(A)):
        temp = []
        for j in range(len(B[0])):
            temp.append(0)
        ans.append(temp)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ans[i][j] += A[i][k] * B[k][j]
    return ans


def take_input():
    r = int(input("Number of rows: "))
    c = int(input("Number of columns: "))
    ans = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(int(input()))
        ans.append(temp)
    return ans


print("Enter details of 1st Matrix: ")
A = take_input()
print("Enter details of 2nd Matrix: ")
B = take_input()
if(len(A[0]) != len(B)):
    print("Invalid Input")
    exit()
print("Answer: ", matmult(A, B))
