# a=20 #global
# def display():
#     a=10 #local
#     print(a)
#     def show():
#         b=15
#         print(b)
#     show()
# display()
##########################
# a,b = 5,3
# def display():
#     if a > b:
#         c=20
#         c+=a+b
#         print(c)
#     else:
#         print("none")
# display()
# def main():
#     a=12
#     a+=1
#     print(a)
# display()
# main()
###########################################
# def display():
#     name=input("Enter your name: ")
#     name+=" lecture"
#     print(name)
# display()
################################################################
name = "jenny"
def display():
    global name
    name += " lectures"
print(name)
display()
print(name)