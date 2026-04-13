from abc import ABC, abstractmethod

# 1. Abstraction: Creating an Abstract Base Class
class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        """Abstract method that must be implemented by sub-classes."""
        pass

# 2. Inheritance: Rectangle inherits from Polygon
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# 3. Inheritance: Square inherits from Rectangle (a Square is a specific Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        # A square is just a rectangle where width and height are the same
        super().__init__(side, side)

# --- Execution ---
rect = Rectangle(10, 5)
sq = Square(4)

print(f"Rectangle Area: {rect.calculate_area()}") # Output: 50
print(f"Square Area: {sq.calculate_area()}")      # Output: 16
