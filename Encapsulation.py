# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.__account_holder = account_holder
#         self.__balance = initial_balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited rs{amount}. New balance: rs{self.__balance}")
#         else:
#             print("Invalid amount")
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew rs{amount}. New balance: rs{self.__balance}")
#         else:
#             print("Invalid amount or insufficient balance")
    
#     def get_balance(self):
#         return self.__balance
    
#     def get_account_holder(self):
#         return self.__account_holder


# # Usage
# account = BankAccount("John Doe", 1000)
# account.deposit(500)
# account.withdraw(200)
# print(f"Balance: rs{account.get_balance()}")
#################################
class School:
    def __init__(self, students=100):
        self.__students = students
    
    def students(self):
        print(f" the students are {self.__students} in a school")
class Classroom(School):
    def __init__(self, students=30, teachers=10):
        super().__init__(students)
        self.__teachers = teachers
    
    def teachers(self):
        print(f" the teachers are {self.__teachers} in a school")
    def students(self):
        print(f" the students are {self._School__students} in a classroom")
class Benches(Classroom):
    def __init__(self, students=3, benches=20):
        super().__init__(students)
        self.__benches = benches
    
    def benches(self):
        print(f" the benches are {self.__benches} in a school")
    def students(self):
        print(f" the students are {self._School__students} in a bench")
    def return_students(self):
        return self._School__students
    def return_teachers(self):
        return self._Classroom__teachers
c1=Classroom()
c1.students()
c1.teachers()
b1=Benches()   
b1.students()
b1.benches()