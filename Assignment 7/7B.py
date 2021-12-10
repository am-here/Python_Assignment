s = input("Input: ")
n = eval(s.split(' ', 1)[0])
sent = (s.split(' ', 1)[1]).split('. ')
if(len(sent) != n):
    print("Invalid Input")
else:
    print("Output:")
    for i in sent:
        print(i.upper())
