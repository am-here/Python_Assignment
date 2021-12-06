u = eval(input("Enter number of units: "))
if(u < 201):
    cost = 0.5*u
elif(u < 401):
    cost = 100+0.65*u
elif(u < 601):
    cost = 200+0.80*u
else:
    cost = 300+1.0*u
print("Amount to be paid:", cost)
