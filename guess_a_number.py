import random
import logo
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
#######checking by defining the level type like easy or hard.(chosen_level)=easy/hard
def level_type(chosen_level):
    if chosen_level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
########checking the answers by defining function with arguments used to check the answer
##number=what we give input
##answer=what computer taught
##attempts=how many attempts we are doing
def check_answer(number,answer,attempts):
    if number < answer:
        print("your guess is too low")
        return attempts - 1
    elif number > answer:
        print("your guess is too high")
        return attempts - 1
    else:
        print(f"your guess is correct!,the answer is {answer}")
        return attempts - 1  ##optional step
def game():
    print("Welcome to Guess A Number")
    print(logo.log)
    print("Think of a number between 1 and 20")
    num = random.randint(1, 20)
    print(num)
    level = input("Choose a level type? easy/hard?: ")
    attempts=level_type(level)
    number = 0
    while number != num:
        print(f'you have {attempts} attempts to guess the number!')
        number = int(input("Choose a number between 1 and 20: "))
        attempts = check_answer(number,num,attempts)
        if attempts == 0:
            print("You are out of guesses......... YOU LOSE!")
            return True
        elif number != num:
            print("sorry..guess again !")

game()
