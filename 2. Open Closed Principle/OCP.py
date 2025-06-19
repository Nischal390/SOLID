from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
def calculate_total_area(shapes):
    total_area = sum(shape.area() for shape in shapes)
    return total_area

shapes = [Rectangle(4,5), Circle(3)]
total_area = calculate_total_area(shapes)
print(total_area)