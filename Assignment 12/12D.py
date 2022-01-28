from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calc_area(self):
        return pi * self.radius ** 2


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def calc_area(self):
        return 2 * pi * self.radius * self.height


r = int(int(input("Enter Radius: ")))
h = int(int(input("Enter Height: ")))
cir = Circle(r)
c = Cylinder(r, h)
print("Area of Circle:", cir.calc_area())
print("Area of Cylinder:", c.calc_area())
