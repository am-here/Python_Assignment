import numpy as np
SIZE = eval(input("Enter size of STACK: "))
STACK = np.zeros(SIZE, dtype=int)
top = -1
while(1):
    ch = eval(input("\n1. PUSH\n2. POP\n3. DISPLAY\n4. Exit\nEnter choice: "))
    if ch == 1:
        if top == SIZE - 1:
            print("Stack Overflow")
        else:
            value = eval(input("\nEnter value to be pushed: "))
            top += 1
            STACK[top] = value
    elif ch == 2:
        if top == -1:
            print("Stack Underflow")
            break
        else:
            print("\nPopped value:", STACK[top])
            top -= 1
    elif ch == 3:
        print("\nSTACK\n\n")
        if top == -1:
            print("[Empty]\n")
        else:
            for i in range(top, -1, -1):
                print("|", STACK[i], "|\n|___|")
    elif ch == 4:
        print("\nThank You!")
        break
    else:
        print("\nInvalid Input!")
