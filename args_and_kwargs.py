# def add(*numbers,name):
#     n=0
#     print(numbers)
#     print(name)
#     for i in numbers:
#         n+=i
#          #print("the sum is ",n)
#     print("the total sum is",n)
# # add(1,2,3,4,5)
# # add(56,44,11)
# # add(21,3,6)
# add(1,2,3,name="pradee")
################################################################
def person_info(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
person_info(1,2,3,name="ram",age=26,dept="cse")
person_info(2,4,name="venu",dept="cse")
################################################################