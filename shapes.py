import math

class Shape:
    pass

    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    
class Circle(Shape):
    
    def __init__(self, radius: float | int) -> None:
        self.radius = radius
        
        
    def area(self) -> float | int:
        return math.pi * self.radius ** 2
    
    
    def perimeter(self) -> float | int:
        return 2 * math.pi * self.radius
    
    
class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        
        self.length = length
        self.width = width
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        
        return self.width == other.width and self.length == other.length
    
        
    def area(self) -> int:
        return self.length * self.width
    
    def perimeter(self) -> int:
        return (self.length * 2) + (self.width * 2)
    
    
class Square(Rectangle):
    def __init__(self, side_legnth: int) -> None:
        super().__init__(side_legnth, side_legnth)