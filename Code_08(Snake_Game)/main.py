from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

allTurtles = []

myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")
myScreen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

myScreen.listen()
myScreen.onkey(fun=snake.up, key="Up")
myScreen.onkey(fun=snake.down, key="Down")
myScreen.onkey(fun=snake.right, key="Right")
myScreen.onkey(fun=snake.left, key="Left")

is_game_on = True
while is_game_on:
    myScreen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food and update the score
    if snake.allTurtles[0].distance(food) < 14:
        food.refresh()
        snake.extendSnake()
        scoreboard.increaseScore()

    # Detect collision with the wall
    if (snake.allTurtles[0].xcor() > 280 or snake.allTurtles[0].xcor() < -280 or snake.allTurtles[0].ycor() > 280
            or snake.allTurtles[0].ycor() < -280):
        snake.resetSnake()
        scoreboard.resetScore()

    # Detect collision with the body
    for segment in snake.allTurtles[1:]:
        if snake.allTurtles[0].distance(segment) < 5:
            snake.resetSnake()
            scoreboard.resetScore()

myScreen.exitonclick()
