ch = input("Enter a character: ")
if(ord(ch)>=65 and ord(ch)<=90):
    print("'", ch, "' is an uppercase character")
elif(ord(ch)>=97 and ord(ch)<=122):
    print("'", ch, "' is a lowercase character")
else:
    print("'", ch, "' is not a Valid Input")
