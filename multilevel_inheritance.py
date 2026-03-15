# class Parents:
#     def daddy(self):
#         print("daddy is main")
# class Child(Parents):
#     def children(self):
#         print("children are going to school")
# class  Babies(Child):
#     def baby(self):
#         print("baby is drinking water")
# class Toddler(Babies,Child,Parents):
#     def papa(self):
#         print("papa is getting water")
#         print("jai hind")
# kid1=Toddler()
# # kid2=Child()
# # kid2.children()
# # kid2.daddy()
# # kid1=Babies
# kid1.children()
# kid1.baby()
# kid1.papa()
# kid1.daddy()
#################
class Parents:
    def __init__(self,name,age):
        self.name_of_them=name
        self.age_of_them=age
    def daddy(self):
        print("daddy is main")
class Child(Parents):
    def children(self):
        print("children are going to school")
class  Babies(Child):
    def baby(self):
        print(f"baby name is {self.name_of_them} and age is {self.age_of_them} years old")
    def daddy(self):
        # Parents.daddy(self)
        # super().daddy()
        print(f"daddy name is {self.name_of_them} and he was {self.age_of_them} years old")
class Programmer(Babies):
    def coding(self):
        print("the coder is coding")
object=Babies("lakshu",2)
object.baby()
object.daddy()
