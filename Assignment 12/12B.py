from math import pi


class Circle:
    radius = 1.0

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calc_area(self):
        return pi * self.radius ** 2


cir = Circle(int(input("Enter radius: ")))
print(cir.get_radius())
print(cir.calc_area())
