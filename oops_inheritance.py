class Student: ##parent class
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def madam(self):
        print("hi student,i am teacher")
    def work(self):
        print("working teacher for students")
################# not another problem#############################
class MaleStudent(Student): ##child class
    def flirt(self):
        print("i can flirt with students")
    def work(self):
        super().work()  ##this brings the previous same function in child class from parent class
        print("i am manager")
ob1 = MaleStudent()
ob1.madam() ##inherit
ob1.flirt()
ob1.work()
print(ob1.num_eyes)
print(ob1.num_nose)
class FemaleStudent(MaleStudent):
    def books(self):
        print("books are important to study")
    def job(self):
        super().work()
        print("soon can work with students")
obj2 = FemaleStudent()
obj2.books()
obj2.job()