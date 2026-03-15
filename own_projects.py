# # a=[1,2,3,4,5,6,7,1,1,3,1]
# # b=[2,5,4,3,6,7,1,3,45,4,3,3,3]
# # c=a.count(1)
# # print(c)
# # q=a.index(3)
# # print(q)
# # box1=['A','A','A']
# # box2=['A','A','A']
# # box3=['A','A','A']
# # box4=['A','A','A']
# # matrix=[box1,box2,box3,box4]
# # print(f"{box1}\n{box2}\n{box3}\n{box4}")
# # place=input("enter where you have to place it: ")
# # rows=int(place[0])#rows are list so rows had index
# # columns=int(place[1])#columns does not have index so starts with 1
# # rows_columns=matrix[rows-1][columns-1]='🙂'
# # #in matrix,even they are rows and columns we have to reduce the index.
# # # so row-1,columns are like lists which seems as index so column-1.
# #
# # print(f"{box1}\n{box2}\n{box3}\n{box4}")
# #################################################################################333
# # import random
# # user=int(input("Enter your ones 0 for rock,1 for paper,2 for scissors: "))
# # if user >= 3 or user <0:
# #     print("you entered invalid number!!")
# # else:
# #     computer_choice=random.randint(0,2)
# #     # print("computer chose:",computer_choice)
# #     print(f"computer chose:{computer_choice}")
# #     if user==computer_choice:
# #         print("It's a match!")
# #     elif user==0 and computer_choice==2:
# #         print("You win!")
# #     elif user==2 and computer_choice==0:
# #         print("you lose!")
# #     elif user>computer_choice:
# #         print("you won!")
# #     elif user<computer_choice:
# #         print("you loosed!")
# ##############################-PRIME NUMBER EASY METHOD-###################################################
# # number = int(input("Enter a number: "))
# # if number % 2 == 0:
# #     print("its even")
# # elif number % 3 != 0 and number % 2 != 0:
# #     print("its prime number")
# # else:
# #     print("its odd")
# # print(number)
# ###################################################################################################
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# def exponent(a,b):
#     return a^b
# def floor_division(a,b):
#     return a//b
# performing_operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
#     "^":exponent,
#     "//": floor_division,
#     }
# for operator in performing_operations:
#     print(operator)
# continue_performance = True
# num1 = int(input("Enter first number: "))
# symbol=input("Enter symbol: ")
# num2 = int(input("Enter second number: "))
# if symbol in performing_operations:
#     print(performing_operations[symbol])
# else:
#     print("bye")

# def open():
#     pass
# print("hello".upper())
# print("BAKE".lower())
# open()
# #######################################################
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#         s1 = Student("raju", 10)
#         s2 = Student("hari", 20)
#         print(s1+s2)
# ###############################################################################################################
# coin_input = int(input("enter the coins: "))
# while coin_input < 10:
#     coin_input += 1
#     print("You have", coin_input, "coins.")
#     continue
#     # pass
# if coin_input <= 10:
#     print("You had single coins!")
# elif coin_input >= 10:
#     print("You had double coins!")
# else:
#     print("You lose !")
# ###############################################################################################################
# num = [10,20,30]
# new_num = [40,50,60]
# for i in new_num:
#     num.append(i)
# print(num)
# ###############################################################################################################
# i=0
# while i<6:
#     i+=1
#     print(i)
#     # i+=1
# ###############################################################################################################
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.scatter(x,y)
# plt.title("scatterplot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()
# ###############################################################################################################
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
# print("even numbers")
# for i in range(1,101):
#     if i % 2 != 0:
#         print(i)
# print("odd numbers")
# ###########################################own project of guessing a number####################################################################
# import random
# num=random.randint(1,20)
# def random_number():
#     for num in range(1,20):
#         print(f"random number between 1 and 20 is {random.randint(1,20)}")
#         return True
#     return False
# random_number()
# guessing=True
# def false(guessing):
#     global guess
#     while guessing:
#         guess = int(input("enter a number: "))
#         if guess==num:
#             print("your guess is right")
#             return False
#         elif guess<=num:
#             print("your guess is too low")
#         elif guess>=num:
#             print("your guess is too high")
#         if guess==0:
#             guessing = False
#             print("exit program")
# false(guessing)
#####################################################################################################
# import random
# condition=0
# level = (input("enter the level u want?: "))
# num=random.randint(1,10)
# for num in level:
#     print(f"this is number {num}")
#     while level == num:
#         level = (input("enter the level u want?: "))
#         for num in level:
#             print(f"this is number {num}")
#         def looping():
#             if level<=num :
#                 return level
#             else:
#                 print("exit")
#                 return False
#         looping()
# ####################################################################
# num=int(input("Enter a number: "))
# if num & 1 == 0:
#     print("even")
# else:
#     print("odd")
########################################
# class Student:
#     print("hi")
#     print("bye")
# student1 = Student()
# print()
################################################
# food="pizza"
# new_food=food.replace("z","s")
# print(new_food)


#import packages
import random
import turtle
import time

#to create screen
# screen=turtle.Screen()
# screen.title("SNAKE GAME")
# screen.setup(width=800,height=600)
# screen.tracer(0)
# screen.bgcolor("black")
# #create border
# turtle.speed(5)
# turtle.pensize(5)
# turtle.penup()
# turtle.goto(-310,250)
# turtle.pendown()
# turtle.color("red")
# turtle.forward(600)
# turtle.right(90)
# turtle.forward(500)
# turtle.right(90)
# turtle.forward(600)
# turtle.right(90)
# turtle.forward(500)
# turtle.penup()
# turtle.hideturtle()
# ##score
# score=0
# delay=0.1
# #snake
# snake=turtle.Turtle()
# snake.speed()
# snake.shape("square")
# snake.color("blue")
# snake.penup()
# snake.goto(0,0)
# snake.direction="stop"
# ##food
# fruit=turtle.Turtle()
# fruit.speed(0)
# fruit.shape("square")
# fruit.color("violet")
# fruit.penup()
# fruit.goto(30,30)
# old_fruit=[]
# ##scoring
# scoring=turtle.Turtle()
# scoring.speed(0)
# scoring.color("white")
# scoring.penup()
# scoring.hideturtle()
# scoring.goto(0,300)
# scoring.write("Score: 0",align="center",font=("Courier",24,"normal"))
# ##define how to move
# def snake_up():
#     if snake.direction != "down":
#         snake.direction="up"
# def snake_down():
#     if snake.direction != "up":
#         snake.direction="down"
# def snake_left():
#     if snake.direction != "right":
#         snake.direction="left"
# def snake_right():
#     if snake.direction != "left":
#         snake.direction="right"
#
# def snake_move():
#     if snake.direction == "up":
#         y=snake.ycor()
#         snake.sety(y+20)
#     if snake.direction == "down":
#         y=snake.ycor()
#         snake.sety(y-20)
#     if snake.direction == "left":
#         x=snake.xcor()
#         snake.setx(x-20)
#     if snake.direction == "right":
#         x=snake.xcor()
#         snake.setx(x+20)
# # keyboard binding
# screen.listen()
# screen.onkey(snake_up,"Up")
# screen.onkey(snake_down,"Down")
# screen.onkey(snake_left,"Left")
# screen.onkey(snake_right,"Right")
# ##main loop
# game_is_on=True
# while game_is_on:
#     screen.update()
#
#     #snake and fruit collision
#     if snake.distance(fruit)<20:
#         x=random.randint(-290,270)
#         y=random.randint(-240,240)
#         fruit.goto(x,y)
#         scoring.clear()
#         score+=1
#         scoring.write("score:{}.".format(score),align="center",font=("Courier",24,"normal"))
#         delay-=0.001
#
#         ##creating new foods
#         new_fruit=turtle.Turtle()
#         new_fruit.speed(0)
#         new_fruit.shape("square")
#         new_fruit.color("blue")
#         new_fruit.penup()
#         old_fruit.append(new_fruit)
#     #adding ball to snake
#     for index in range(len(old_fruit)-1,0,-1):
#         a=old_fruit[index -1].xcor()
#         b=old_fruit[index -1].ycor()
#         old_fruit[index].goto(a,b)
#     if len(old_fruit)>0:
#         a=snake.xcor()
#         b=snake.ycor()
#         old_fruit[0].goto(a,b)
#     snake_move()
#
#     #snake and border collision
#     if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()< -240:
#         game_is_on=False
#         time.sleep(1)
#         # break
#         screen.clear()
#         screen.bgcolor("turquoise")
#         scoring.goto(0,0)
#         scoring.write("   GAME OVER \n your score is:{}.".format(score),align="center",font=("Courier",24,"normal"))
#     #snake collisions
#     for food in old_fruit:
#         if food.distance(snake)<20:
#             time.sleep(1)
#             screen.clear()
#             screen.bgcolor("turquoise")
#             scoring.goto(0,0)
#             scoring.write("   GAME OVER \n your score is:{}.".format(score),align="center",font=("Courier",24,"normal"))
#     time.sleep(delay)
# turtle.Terminator()
# turtle.exitonclick()
######################################################################################################
# try:
#     a=2
#     b=4
#     c=0
#     print(a/c)
#     print(a/b)
# except ZeroDivisionError:
#     print("Division by zero")
#################################
def func():
    print(90)
    return True
print(func() and dir(func))
