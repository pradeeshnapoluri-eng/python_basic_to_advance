class Circle:
    pi = 3.14
    def __init__(self,radius): ##here extra radius used to add something extra
        self.radius_of_obj = radius
    def circumference(self):
        return 2*self.pi*self.radius_of_obj  ##2 x 3.14 x radius of obj(if given value).
circle1 = Circle(1)
print(circle1.circumference())
circle2 = Circle(2)
print(circle2.circumference())
circle3 = Circle(3)
print(circle3.circumference())
circle4 = Circle(4)
print(circle4.circumference())
