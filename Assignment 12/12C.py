class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"X-Coordinate:{self.x} and Y-Coordinate:{self.y}"

    def translate(self, x, y):
        self.x += y
        self.y += x


x = int(input("Enter X: "))
y = int(input("Enter Y: "))
p = Point(x, y)
print(p.display())
p.translate(x, y)
print(p.display())
