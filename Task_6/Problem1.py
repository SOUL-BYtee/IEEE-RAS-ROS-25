import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Input the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.calculate_area()}")
print(f"Perimeter of the circle: {circle.calculate_perimeter()}")