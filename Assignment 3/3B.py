import math
import cmath

A, B, C = eval(input("Enter values of A, B and C in Ax^2+Bx+C=0: "))
D = B**2 - 4*A*C

if D > 0:
    print("Roots are Real and Distinct.\nRoot 1:", (-B+math.sqrt(D)) /
          (2*A), ".\nRoot 2:", (-B-math.sqrt(D))/(2*A), ".")

elif D == 0:
    print("Roots are Real and Equal.\nRoot 1:",
          (-B)/(2*A), ".\nRoot 2:", (-B)/(2*A), ".")

else:
    print("Roots are Imaginary and Distinct.\nRoot 1: ", (-B)/(2*A), " + ",
          (cmath.sqrt(D))/(2*A), "\nRoot 2: ", (-B)/(2*A), " - ", (cmath.sqrt(D))/(2*A), sep="")
