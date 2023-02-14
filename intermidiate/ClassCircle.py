''' Construct a class Circle that represents a Circle.


The class should support the following functionalities:-
perimeter() -> returns the perimeter of the circle
area() -> returns the area of the circle


Assume Π (pi) = 3.14 for calculations.
You may define any properties in the class as you see appropriate.'''

class Circle:
    # Define properties here
    PI = 3.14
    # Define constructor here
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        return 2*Circle.PI*self.radius
    # Complete the function

    def area(self):
        return Circle.PI*self.radius*self.radius
# Complete the function


a = Circle(3)  # Radius = 3
print(a.perimeter() )# 18.84
print(a.area()) # 28.26