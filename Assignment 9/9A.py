import calculator
import os
while 1:
    print("Please select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Modulo\n"
          "6. Exponents\n")

    select = int(input("Your selected operation: "))

    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number: "))

    if select == 1:
        calculator.add(a, b)
    elif select == 2:
        calculator.substract(a, b)
    elif select == 3:
        calculator.multiply(a, b)
    elif select == 4:
        calculator.divide(a, b)
    elif select == 5:
        calculator.modulo(a, b)
    elif select == 6:
        calculator.exp(a, b)
    else:
        print("Invalid input")
    continuity = input("Do you want to continue? (Y/N): ")
    if(continuity == 'N' or continuity == 'n'):
        break
    os.system('cls')
