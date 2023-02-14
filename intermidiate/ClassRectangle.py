class X:
    # Define properties here

    # Define constructor here
    def __init__(self, len, brd):
        self.l = len
        self.b = brd

    def perimeter(self):
        return 2 * (self.l + self.b)

    # Complete the function

    def area(self):
        return (self.l * self.b)


# Complete the function


# Rectangle a = new Rectangle(2, 3)  // Length = 2, Breadth = 3
# a.perimeter() // Should give 10
# a.area() // Should give 6
a = X(2, 3)
print(a.area)
print(a.perimeter())
