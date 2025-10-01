import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * math.pow(self.radius, 2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return self.base * self.height
    
    def calculate_perimeter(self):
        return (2 * self.base) + (2 * self.height)


class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side
    
    def calculate_perimeter(self):
        return 4 * self.side


class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return (self.base * self.height / 2)
    
    def calculate_perimeter(self):
        return self.base + self.height + self.calculate_hypotenuse()
    
    def calculate_hypotenuse(self):
        return math.pow(self.base * self.base + self.height * self.height, 0.5)
    
    def determine_triangle_type(self):
        if ((self.base == self.height) and (self.base == self.calculate_hypotenuse()) and 
            (self.height == self.calculate_hypotenuse())):
            print("Es un triángulo equilátero")
        elif ((self.base != self.height) and (self.base != self.calculate_hypotenuse()) and 
              (self.height != self.calculate_hypotenuse())):
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


figure1 = Circle(2)
figure2 = Rectangle(1, 2)
figure3 = Square(3)
figure4 = RightTriangle(3, 5)

print(f"El área del círculo es = {figure1.calculate_area()}")
print(f"El perímetro del círculo es = {figure1.calculate_perimeter()}")
print()
print(f"El área del rectángulo es = {figure2.calculate_area()}")
print(f"El perímetro del rectángulo es = {figure2.calculate_perimeter()}")
print()
print(f"El área del cuadrado es = {figure3.calculate_area()}")
print(f"El perímetro del cuadrado es = {figure3.calculate_perimeter()}")
print()
print(f"El área del triángulo es = {figure4.calculate_area()}")
print(f"El perímetro del triángulo es = {figure4.calculate_perimeter()}")
figure4.determine_triangle_type()