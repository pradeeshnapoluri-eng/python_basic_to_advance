# class Demo:
#     var="jenny"
# d=Demo()
# print(d.var)
# print(d.__dict__)
# print(type(d))
# print(type(Demo))
# print(len(d.var))

class Author:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return (f"Author name is {self.name} and age is {self.age}")
    def __len__(self):
        return (f"Author age is {self.age}")
    def __del__(self):
        print("Object is deleted")
d=Author("jenny",23)
print(d.name);print(d.age)
print()
print(d.__str__())
print(d.__len__())
del d