class Demo:
    def __init__(self):
        self.stri = ""

    def Get_String(self):
        self.stri = input()

    def Print_String(self):
        print(self.stri.upper())


stri = Demo()
stri.Get_String()
stri.Print_String()
