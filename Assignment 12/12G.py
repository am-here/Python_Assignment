class Square:
    def __init__(self, square):
        self.square = square

    def evaluate(self):
        try:
            return float(self.square)**2
        except Exception:
            return False


num = Square(input('Enter a number: '))
if num.evaluate() == False:
    print('Invalind number given!')
else:
    print('Square of the given number:', num.evaluate())
