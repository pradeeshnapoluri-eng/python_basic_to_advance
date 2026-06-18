# class Employee:
#     def __init__(self, name, salary):
#         self.name = name          # public attribute
#         self.__salary = salary    # private attribute
#
# emp = Employee("Fedrick", 50000)
# print(emp.name)
# print(emp._Employee__salary)
######################
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute
    def display(self):
        print("i am base class")

class Workers(Employee):
    def __init__(self, name, salary):
        super().__init__(name,salary)
    def display(self):
        print("i am worker in this company")

emp = Employee("Fedrick", 50000)
print(emp.name)
print(emp._Employee__salary)
emp.display()
print()
W1=Workers("rohit",34200)
print(W1.name)
print(W1._Employee__salary)
# print(W1._Workers__salary)
W1.display()
print()
#####
class Mango:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        ...
    def mango(self):
        pass
    def mango2(self):
        print("I am mango")
m=Mango("Mango",20000)
print(m.name)
print(m.salary)
