import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def perimeter(self):
        pass
    
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, x, y, side1, side2, side3):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
