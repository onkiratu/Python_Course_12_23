# Attributes and Methods 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Using methods
my_circle = Circle(5)
print(my_circle.area())
