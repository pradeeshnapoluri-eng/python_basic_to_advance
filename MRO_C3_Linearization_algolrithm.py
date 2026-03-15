class A:
    # pass
    def display(self):
        print("display from A class")
class B(A):
    # pass
    def display(self):
        print("display from B class")
class C(A):
    def show(self):
        print("display from C class")
class D(B,C):
    # pass
    def display(self):
        print("display from D class")
d1=D()
# d1.display()
print(D.__mro__(A))
