from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print(f"paid {amount} using UPI")
class Card(Payment):
    def pay(self,amount):
        print(f"paid {amount} using CARD")
class Cash(Payment):
    def pay(self,amount):
        print(f"paid {amount} using CASH")
class Dollar(ABC):
    @abstractmethod
    def display(self):
        print("display")
class Family(ABC):
    @abstractmethod
    def display(self):
        print("these are dollars")
class Teacher(Family):
    def display(self):
        print("these are teachers")
class Aunty(Teacher):
    def display(self):
        print("Aunty")
class Kids(Aunty):
    def display(self):
        print("Kids")
class Uncles(Aunty):
    def display(self):
        print("Uncles")
class Nephew(Uncles):
    def display(self):
        print("Nephew")

