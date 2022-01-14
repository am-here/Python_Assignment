file = open('C:\codes\Third Sem\Python Lab\Assignment 11/text.txt', 'r')
for line in file.readlines():
    print(line, end="")
file.close()
