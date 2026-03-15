class ClassRoom:
    def __init__(self):
        print("calling init from ClassRoom")
        self.benches_in_school=120
        self.chairs_in_school=100
    def benches(self):
        print("there are 30 benches!!")
    def students(self):
        print("class room contains boys and girls")
class Faculty:
    def __init__(self,name):
        print("calling init from Faculty")
        self.name=name
    def teachers(self):
        print("teachers can take a long time")
    def students(self):
        print("big classrooms have more students")
class Total(ClassRoom,Faculty):
    def __init__(self,name,language,intial):
        self.language=language
        self.intial=intial
        Faculty.__init__(self,name) ##here only calling from Faculty only thats why it doesnt call other functions
        ClassRoom.__init__(self)
    def teachers(self):
        print("we have male teachers")
    def students(self):
        print("we have boy students")
    def display(self):
        print(f"hi,i am {self.name}, i had learned {self.language}, my intial is {self.intial}")
        return "correct"
obj1=Total("johny","English","park")
obj2=Faculty("manisha")
print(obj2.name)
# obj1.students()
# Faculty.students(obj1)
# ClassRoom.benches(obj1)
# Total.teachers(obj1)
# Total.students(obj1)
# print(Boys.mro())
# print(obj1.benches_in_school)
# print(obj1.name+" and "+obj2.name)
# obj1.teachers()
# obj2.teachers()
print(obj1.benches_in_school)
print(obj1.name)
print(obj1.language)
print(obj1.intial)
obj1.display()
print(obj1.display())
