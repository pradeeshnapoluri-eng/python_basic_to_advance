from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("i am from vehicle class")
#############
# from abstraction_methods import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("start with kick")
class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.gears=6
    def start(self):
        print("start with key")
bike=Bike(3,"blue")
bike.start()
