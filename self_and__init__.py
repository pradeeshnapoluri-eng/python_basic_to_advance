# class BioData:
#     def __init__(self,person_name,their_address):
#         self.name = person_name
#         self.address = their_address
# obj1=BioData("daniela","paris")
# print(obj1.name)
# print(obj1.address)
# obj2=BioData("lara","los angeles")
# print(obj2.name)
# print(obj2.address)
########################################################################################################################
# class BioData:
#     def __init__(self,person_name,their_address):
#         self.name = person_name
#         self.address = their_address
#     def display_information(self):
#         # print(self.name)
#         # print(self.address)
#         print(f"My name is {self.name} and, my address is {self.address}.")
# data1=BioData("daniela","paris")
# data2=BioData("lara","los angeles")
# data3=BioData("meghan","USA")
# asia4=BioData("kavita","Bangladesh")
# data1.display_information()
# data2.display_information()
# data3.display_information()
# asia4.display_information()
###############################################################################################################
class MyClass:
    def __init__(self,staff_name,subject_name):
        self.faculty_name=staff_name
        self.course=subject_name
    def display(self):
        print(self.faculty_name)
        print(self.course)
class1=MyClass("manisha","english")
class2=MyClass("hema","maths")
class1.faculty_name="john"
class1.course="biology"
print(class1.faculty_name,class1.course)
class1.display()

class1.faculty_name="preethi"
class1.course="science"
class2.display()
class1.display()
# class3.display()


