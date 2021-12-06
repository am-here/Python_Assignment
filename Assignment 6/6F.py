import numpy as np
SIZE = eval(input("Enter size of QUEUE: "))
QUEUE = np.zeros(SIZE, dtype=int)
rear = -1
front = -1
while(1):
    ch = eval(input("\n1. ENQUE\n2. DELQUE\n3. DISPLAY\n4. Exit\nEnter choice: "))
    if ch == 1:
        if rear == SIZE - 1:
            print("\nQUEUE Overflow")
        else:
            value = eval(input("\nEnter value to be pushed: "))
            if front == rear + 1:
                front = -1
                rear = -1
            if front == -1 and rear == -1:
                front = 0
            rear += 1
            QUEUE[rear] = value
    elif ch == 2:

        if front == -1:
            print("\nQUEUE Underflow")
        else:
            print("\nPopped value:", QUEUE[front])
            if front == rear:
                rear = -1
                front = -1
            else:
                front += 1
    elif ch == 3:
        print("\nQUEUE: ", end=' ')
        if front == -1:
            print("\n[Empty]")
        else:
            for i in range(front, rear+1):
                print(QUEUE[i], end=' ')
        print()
    elif ch == 4:
        print("\nThank You!")
        break
    else:
        print("\nInvalid Input!")
