year = eval(input("Enter Year: "))
if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(year, "is a leap Year")
else:
    print(year, "is not a leap Year")
