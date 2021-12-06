import numpy as np
SIZE = eval(input("Enter size of C_QUEUE: "))
C_QUEUE = np.zeros(SIZE, dtype=int)
rear = -1
front = -1
while(1):
    ch = eval(input("\n1. ENQUE\n2. DELQUE\n3. DISPLAY\n4. Exit\nEnter choice: "))
    if ch == 1:
        if (rear + 1) % SIZE == front:
            print("\nC_QUEUE Overflow")
        else:
            value = eval(input("\nEnter value to be pushed: "))
            if front == -1:
                front = 0
                rear = 0
                C_QUEUE[rear] = value
            else:
                rear = (rear + 1) % SIZE
                C_QUEUE[rear] = value
    elif ch == 2:
        if front == -1:
            print("\nC_QUEUE Underflow")
        else:
            if front == rear:
                print("\nPopped value:", C_QUEUE[front])
                front = -1
                rear = -1
            else:
                print("\nPopped value:", C_QUEUE[front])
                front = (front + 1) % SIZE
    elif ch == 3:
        print("\nC_QUEUE: ", end=' ')
        if front == -1:
            print("\n[Empty]")
        else:
            if (rear >= front):
                for i in range(front, rear + 1):
                    print(C_QUEUE[i], end=' ')
                print()
            else:
                for i in range(front, SIZE):
                    print(C_QUEUE[i], end=' ')
                for i in range(0, rear + 1):
                    print(C_QUEUE[i], end=' ')
                print()
    elif ch == 4:
        print("\nThank You!")
        break
    else:
        print("\nInvalid Input!")
