class Shape:
    def __init__(self, shape):
        self.shape = shape


class Rectangle(Shape):
    length = 1
    breath = 1

    def __init__(self, length, breath, shape):
        self.length = length
        self.breath = breath
        super().__init__(shape)

    def calc_area(self):
        return self.length*self.breath

    def Rect_Details(self):
        return f"\n**Details of Rectangle:**\nLength: {self.length},\nBreath: {self.breath},\nShape: {self.shape}, and\nArea: {self.calc_area()}"


class Triangle(Shape):
    base = 1
    height = 1

    def __init__(self, base, height, shape):
        self.base = base
        self.height = height
        super().__init__(shape)

    def calc_area(self):
        return self.base*self.height/2

    def Tring_Details(self):
        return f"\n**Details of Triangle:**\nBase: {self.base},\nHeight: {self.height},\nShape: {self.shape}, and\nArea: {self.calc_area()}"


shape = input("Enter shape: ")
length = int(input("Enter LENGTH of Rectangle: "))
breath = int(input("Enter BREATH of Rectangle: "))
base = int(input("Enter BASE of Triangle: "))
height = int(input("Enter HEIGHT of Triangle: "))
sh = Shape(shape)
r = Rectangle(length, breath, shape)
t = Triangle(base, height, shape)
print(r.Rect_Details())
print(t.Tring_Details())
