held = eval(input("Enter number of classes held: "))
att = eval(input("Enter number of classes attended: "))
calc = att/held
print("Percentage of classes attended: ",  calc*100, "%", sep='')
med = input("Do you have medical cause? (Y/N): ")
if(med == 'Y' or calc >= 0.75):
    print("You are allowed!")
else:
    print("You are not allowed!")
