from math import pi

class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return round(pi * (self.radius ** 2))

    def getPerimeter(self):
        return round(2 * pi * self.radius)



circy = Circle(11)
print(circy.getArea())

circy = Circle(4.44)
print(circy.getPerimeter())
