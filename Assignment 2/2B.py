b = eval(input("Enter Basic Pay: "))
AGP = 50*b/100
merged_basic = b+AGP
DA = 50*merged_basic/100
HRA = 15*merged_basic/100
total = merged_basic+DA+HRA
print("Total Salary:", total)
