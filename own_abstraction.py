from abc import ABC, abstractmethod
# class Classroom(ABC):
#     def __init__(self):
#         self.no_of_students=60
#         self.no_of_benches=30
#     @abstractmethod
#     def room(self):
#         pass
#     def display(self):
#         print("this is a class room")
# #########
# class Students(Classroom):
#     def __init__(self):
#         super().__init__()
#         self.kids=[]
#     def room(self):
#         print("they are students")
# class Teacher(Classroom):
#     def __init__(self):
#         super().__init__()
#     def room(self):
#         print("they are teachers")
#     def chairs(self):
#         print("these are chairs")
# # members=Students()
# # members.room()
###############################
class Family:
    def __init__(self):
        self.no_of_persons=4
    @abstractmethod
    def members(self):
        print(f"we are {self.no_of_persons} in our family")
    def display(self):
        print("i am from base class")
class Mother(Family):
    def __init__(self):
        self.no_of_child=2
    @abstractmethod
    def mommy(self):
        print(f"i am mommy to {self.no_of_child} children")
    def display(self):
        print("i am from 2nd class")
class Father(Family):
    def __init__(self):
        self.no_of_kids=2
    @abstractmethod
    def daddy(self):
        print(f"i am dad to {self.no_of_kids} children")
    def display(self):
        print("i am from 3rd class")
class Child1(Family):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def john(self):
        print("i am elder brother in my family")
    def display(self):
        print("i am from 4th class")
class Child2(Family):
    def __init__(self):
        super().__init__()
    def riya(self):
        print("i am younger sister in my family")
    def display(self):
        pass