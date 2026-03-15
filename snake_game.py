#import packages
import random
import turtle
import time

#to create screen
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.bgcolor("black")
#create border
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("sea green")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()
##score
score=0
delay=0.1
#snake
snake=turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direction="stop"
##food
fruit=turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("red")
fruit.penup()
fruit.goto(30,30)
old_fruit=[]
##scoring
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("indigo")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: 0",align="center",font=("Courier",24,"normal"))
##define how to move
def snake_up():
    if snake.direction != "down":
        snake.direction="up"
def snake_down():
    if snake.direction != "up":
        snake.direction="down"
def snake_left():
    if snake.direction != "right":
        snake.direction="left"
def snake_right():
    if snake.direction != "left":
        snake.direction="right"

def snake_move():
    if snake.direction == "up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x=snake.xcor()
        snake.setx(x+20)
# keyboard binding
screen.listen()
screen.onkey(snake_up,"Up")
screen.onkey(snake_down,"Down")
screen.onkey(snake_left,"Left")
screen.onkey(snake_right,"Right")
##main loop
game_is_on=True
while game_is_on:
    screen.update()

    #snake and fruit collision
    if snake.distance(fruit)<20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write("score:{}.".format(score),align="center",font=("Courier",24,"normal"))
        delay-=0.001

        ##creating new foods
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("blue")
        new_fruit.penup()
        old_fruit.append(new_fruit)
    #adding ball to snake
    for index in range(len(old_fruit)-1,0,-1):
        a=old_fruit[index -1].xcor()
        b=old_fruit[index -1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a=snake.xcor()
        b=snake.ycor()
        old_fruit[0].goto(a,b)
    snake_move()

    #snake and border collision
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()< -240:
        game_is_on=False
        time.sleep(1)
        # break
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0,0)
        scoring.write("   GAME OVER \n your score is:{}.".format(score),align="center",font=("Courier",24,"normal"))
    #snake collisions
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0,0)
            scoring.write("   GAME OVER \n your score is:{}.".format(score),align="center",font=("Courier",24,"normal"))
    time.sleep(delay)
turtle.Terminator()
turtle.exitonclick()







