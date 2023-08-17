import random
from turtle import Turtle, Screen
import time
sc = Screen()
sc.setup(width=700, height=500)
sc.bgcolor("white")
sc.tracer(0)


xpos = [0, -20, -40]
newl = []

for i in range(0, 3):
    newt = Turtle("square")
    newt.penup()
    newt.color("green")
    newt.goto(xpos[i], 0)
    newl.append(newt)

game_on=True


def up():
    if newl[0].heading()!=270:
        newl[0].setheading(90)
def down():
    if newl[0].heading()!=90:
        newl[0].setheading(270)
def left():
    if newl[0].heading()!=0:
        newl[0].setheading(180)
def right():
    if newl[0].heading()!=180:
        newl[0].setheading(0)
sc.listen()

sc.onkey(fun=up,key="Up")
sc.onkey(fun=down,key="Down")
sc.onkey(fun=left,key="Left")
sc.onkey(fun=right,key="Right")

food= Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)

x = random.randint(-300, 300)
y = random.randint(-200, 200)
food.goto(x,y)
#
score = 0

scoreBoard = Turtle()
scoreBoard.color("black")
scoreBoard.penup()
scoreBoard.goto(0,215)
scoreBoard.write(arg=f"Score: {score}", align="center", font=('Arial', 18, 'bold'))
scoreBoard.hideturtle()


# game over
def game_over():
    gameOver = Turtle()
    gameOver.color("black")
    gameOver.penup()
    gameOver.goto(0,0)
    gameOver.write(arg="game over", align="center", font=('Arial', 18, 'bold'))
    gameOver.hideturtle()

while game_on:
    time.sleep(0.1)
    sc.update()

    for i in range(len(newl)-1, 0, -1):
        newl[i].goto(x=newl[i-1].xcor(), y=newl[i-1].ycor())
    newl[0].color("black")
    newl[0].forward(20)

    x = random.randint(-300, 300)
    y = random.randint(-200, 200)

    if newl[0].distance(food) <15:
        food.goto(x, y)

        score = score + 1
        scoreBoard.clear()
        scoreBoard.write(arg=f"Score: {score}", align="center", font=('Arial', 18, 'bold'))

        newt = Turtle("square")
        newt.penup()
        newt.goto(x=232,y=900)
        newt.color("green")
        newl.append(newt)

    #     collision with wall
    if newl[0].xcor()>335 or newl[0].xcor()<-345 or newl[0].ycor()>230 or newl[0].ycor()<-230:
        game_over()
        game_on=False

sc.exitonclick()

