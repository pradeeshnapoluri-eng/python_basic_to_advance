class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
       print(f"this animal is {self.name} and its age is {self.age}.")
class Mammal(Animal):
   def give_birth(self):
       print("Mammal gives birth")
class Bird(Animal):
   def lay_eggs(self):
       print("Bird lays eggs")
class Platypus(Mammal, Bird):
   pass
platypus = Platypus("emu",12)
platypus.speak() # Method from Animal class
platypus.give_birth() # Method from Mammal class
platypus.lay_eggs() # Method from Bird class