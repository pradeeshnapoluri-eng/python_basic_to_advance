class Persons:
    followers=0
    company_salary=15000
    company_name="microsoft tech"
    new_name=""
    new_age=""  ##adding these in class persons are not necessary but without adding also works fine.
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age
    def show(self,job_doing):
        print(f"hello i am {self.person_name},my age is {self.person_age},my job is {job_doing}") ##here in fstring we concatenate with commas
        # return obj1.name ##here if we return lyk this it prints what we return.otherwise it gives none.
    def update_workers(self,updated_name,updated_age,updated_salary):
        self.followers += 1
        self.new_name = updated_name
        self.new_age = updated_age
        self.total_salary = updated_salary
obj1=Persons("ravi", 20)
obj2=Persons("kavya", 39)
obj3=Persons("sindhu", 20)
# print(obj1) ##this does not give the output.
# print(obj1.person_name);print(obj1.company_name);print(obj1.company_salary)
# print(obj2.name);print(obj2.company_name);print(obj2.company_salary)
# print(obj3.name);print(obj3.company_name);print(obj3.company_salary)
# print(obj1.show()) ##if we print the calling def function it gives the none.because that have to return something
# obj1.show()
# print(obj1.name)
# obj1.show("frontend developer")
# obj2.show("backend developer")
# obj3.show("python developer")
obj1.update_workers("jenny",34,25000)
obj1.update_workers("madhu",45,28000)
obj1.update_workers("vanaja",32,67000)
obj1.update_workers("krishna",50,45000)
###how many times we write,it shows the last one updated only###
print(obj1.new_name); print(obj1.new_age);print(obj1.total_salary)
# print(obj1.followers)
# print(obj2.followers)
# print(obj3.followers)
