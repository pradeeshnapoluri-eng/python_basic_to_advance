import random

user=int(input("Enter your ones 0 for rock,1 for paper,2 for scissors: "))
if user >= 3 or user <0:
    print("you entered invalid number!!")
else:
    computer_choice=random.randint(0,2)
    # print("computer chose:",computer_choice)
    print(f"computer chose:{computer_choice}")
    if user==computer_choice:
        print("It's a match!")
    elif user==0 and computer_choice==2:
        print("You win!")
    elif user==2 and computer_choice==0:
        print("you lose!")
    elif user>computer_choice:
        print("you won!")
    elif user<computer_choice:
        print("you loosed!")