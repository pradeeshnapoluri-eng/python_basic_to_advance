# print(int.__add__(1,3))
# print(int.__mul__(2,3))
# print(int.__sub__(5,2))
# print(str.__add__('Hello', ' World'))
# print(str.__mul__('Hello ', 3))
####

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return (ComplexNumber(self.real + other.real, self.imag + other.imag))
    def __str__(self):
        return (f"{self.real}r + {self.imag}i")
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2
print(f'c3 is: {c3}')
