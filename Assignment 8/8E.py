def middle_3(original):
    if(len(original) % 2 == 0 or len(original) <= 7):
        return "Invalid Input"
    ind = (len(original)-3)//2
    return original[ind:ind+3]


print(middle_3(input()))
