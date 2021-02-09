from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
bet = screen.textinput(title="Bet Box", prompt="Wich turtle will win the race ? (Color)")
print(bet)
turtles = []
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
i = 0
for color in colors:
    turtle = Turtle()
    turtle.penup()
    turtle.color(color)
    turtle.shape("turtle")
    turtle.shapesize(1.5)
    turtle.goto(x=-240, y=-125+(50*i))
    turtles.append(turtle)
    i = i + 1

winner = ""

def race():
    running = True
    while running:
        for turtle in turtles:
            move = random.randint(10, 100)
            turtle.forward(move)
            if turtle.xcor() > 240:
                global winner
                running = False
                winner = turtle.color()

race()

if winner == bet:
    screen.textinput("You won !", "You won what is your name")
    screen.bye()
else:
    screen.textinput("You lost !", "You lost what is your name")
    screen.bye()

screen.exitonclick()