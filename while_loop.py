# num=int(input("enter a number(use -2 for QUIT!): ")) ##we have to write to choose it na!
# while num !=-2:
#     print(num)
#     num=int(input("enter a number(use -2 for QUIT!): ")) ##here we have to write it for looping it
# ###########################################################
#  count=0
#  while count <= 5:
#     # count+=1 ###if we want to print by adding directly use before the printing
#     # print(count)
#     # count+=1 ###if we want the count then iterate by adding,use after printing
#     # if count == 3:
#     #     break
# else:
#     print("out!!!")
#  print("out from loop")
############################################3
# count=1
# while True:
#     print(count)
#     count+=1
#     if count == 4:
#         break
#     else:
#         print("out of block")
###########################(own_mini_project)##############################
user=int(input(" please enter your number except -2(1 to 10): "))
while user !=-2: ##not equal to used to stop loop
    print(user)
    if user <= 9:
        print("single digit")
    elif user >= 10 and user <=20:
        pass
        # break ##this makes to stop the executing code tooo
        print("double digit")
    else:
        print("out of loop")
    user = int(input(" please enter your number except -2(1 to 10): "))
print("successfully out ")


