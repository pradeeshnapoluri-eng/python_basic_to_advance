# a='welcome to my channel'
# a_splits=a.split(' ') #we provided space.space is also considered as character.
# print(a_splits)

import random

# names=input("enter everyone names here along with comma: ")
# splitted_names=names.split(",")
# # print(splitted_names)
# length=len(splitted_names)
# random_ones=random.randint(0,length-1)
# print(f"{splitted_names[random_ones]} will pay the bill of all...")

a=(input("enter the veggies ur wish: "))
split_veggies=a.split(",")
length=len(split_veggies)
randomes=random.randint(0,length-1) #here a is starting index which starts from 0 whether length starts from 1,so we do minus
print(f"{split_veggies[randomes]} is the final ones")
print(length)
