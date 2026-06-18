# def square(x):
#     return x * x
# print(square(5))  # Output: 25
#############
class Duck:
    def swim(self):
        print("The duck is swimming in the pond.")
    def speak(self):
        print("The duck says quack!")
    
class Dog:
    def swim(self):
        print("The dog is swimming in dirtywater.")
    def speak(self):
        print("The dog says woof!")

class Person:
    def speak(self):
        print("The person says hello!")
    def swim(self):
        print("The person is swimming in the pool.")

class Demo:
    # @staticmethod  ##must in duck typing or else add self in parameter.
    def display(self,obj):
        obj.swim()
        obj.speak()
        print("information displayed successfully")

demo_obj=Demo()
d=Duck()
D=Dog()
p=Person()
demo_obj.display(D)
demo_obj.display(d)
demo_obj.display(p)
###
