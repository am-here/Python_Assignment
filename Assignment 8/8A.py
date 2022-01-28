list = input("Your values: ").split(', ')
dict = {}
for i in list:
    dict[int(i)] = list.count(i)
print(dict)
