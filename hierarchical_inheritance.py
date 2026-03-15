class Human:
    def __init__(self,name,age):
        self.parts=12
        self.name = name
        self.age = age
    def coding(self):
        print(f"my name is {self.name} and i am {self.age} old.i am interested in coding")
class Programmer(Human):
    def kaggle(self):
        print(f"my name is {self.name} and i am {self.age} old.i am interested in kaggle")
    def knn(self):
        print(f"my name is {self.name} and i am {self.age} old.i am interested in knn Algorithm")
class analyst(Human):
    def system(self):
        print(f"my name is {self.name} and i am {self.age} old.i am interested in system")
obj=Programmer("honey",21)
obj2=analyst("shreya",18)
obj.coding()
obj.kaggle()
obj.knn()
obj2.system()