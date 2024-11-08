import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

myScreen = Screen()
myScreen.setup(width=500, height=400)
user_input = myScreen.textinput(title="Make your bet.", prompt="Who will win the race? Enter the color.")
allTurtles = []

yaxis = -70
for item in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[item])
    new_turtle.goto(x=-230, y=yaxis)
    yaxis += 30
    allTurtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for each_turtle in allTurtles:
        if each_turtle.xcor() > 230:
            is_race_on = False
            if user_input == each_turtle.pencolor():
                print(f"You've won!!")
            else:
                print(f"You've lost!!! The winning turtle was {each_turtle.pencolor()}")
        each_turtle.forward(random.randint(0, 10))

myScreen.exitonclick()
