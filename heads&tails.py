#importing random module
import random
coin_side=random.randint(1,2)
print(coin_side)#here if we use strings then it prints that characters only,if we doesn't use then it prints what the data under variable.

if coin_side ==1:
    print("heads")
else:
    print("tails")
print(f'your coin side is {coin_side}')
