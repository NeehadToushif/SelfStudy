class ComplexNumber:
    real = 0
    imaginary = 0

    # Define constructor here
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, x: "ComplexNumber") -> "ComplexNumber":
        real = self.real+x.real
        imaginary = self.imaginary+x.imaginary
        return ComplexNumber(real,imaginary)
    # Complete the function

    def subtract(self, x: "ComplexNumber") -> "ComplexNumber":
        real = self.real - x.real
        imaginary = self.imaginary - x.imaginary
        return ComplexNumber(real, imaginary)
    # Complete the function

    def multiply(self, x: "ComplexNumber") -> "ComplexNumber":
        m = x.real * self.real - x.imaginary * self.imaginary
        n = self.imaginary * x.real + self.real * x.imaginary
        return ComplexNumber(m, n)
    # Complete the function

    def divide(self, x: "ComplexNumber") -> "ComplexNumber":
        m = (self.real * x.real + self.imaginary * x.imaginary) / (x.real * x.real + x.imaginary * x.imaginary)
        n = (self.imaginary * x.real - self.real * x.imaginary) / (x.real * x.real + x.imaginary * x.imaginary)
        return ComplexNumber(m, n)
# Complete the function


a = ComplexNumber(10, 5)
b = ComplexNumber(2, 3)
c1 = a.add(b)
c2 = a.subtract(b)
c3 = a.multiply(b)
c4 = a.divide(b)
print(c1,c2,c3,c4)