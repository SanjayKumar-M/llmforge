"""
Create a Shape class:

It should have an area() method that returns 0 (as a default).
Create Rectangle and Circle classes that inherit from Shape.
Override the area() method in each class to calculate the correct area.
Instantiate objects of each class and print their areas.

"""

class Shape:
    def area(self):
        # Default area for generic shape
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Store rectangle length
        self.width = width    # Store rectangle width

    def area(self):
        # Rectangle area = length * width
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Store circle radius
        self.pi = 3.14        # Use pi value

    def area(self):
        # Circle area = pi * r * r
        return self.pi * self.radius ** 2


# Create objects and print areas
rect = Rectangle(length=10, width=5)
print("Rectangle area:", rect.area())  # Output: 50

cir = Circle(radius=7)
print("Circle area:", cir.area())      # Output: ~153.86

