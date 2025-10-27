from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

myScreen = Screen()
myScreen.bgcolor("black")
myScreen.setup(width=800, height=600)
myScreen.title("Pong Game")
myScreen.tracer(0)

rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))
pong = Ball()
score = Scoreboard()

myScreen.listen()
# movement of right paddle
myScreen.onkey(fun=rightPaddle.up, key="Up")
myScreen.onkey(fun=rightPaddle.down, key="Down")

# movement of left paddle
myScreen.onkey(fun=leftPaddle.up, key="w")
myScreen.onkey(fun=leftPaddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(pong.ball_move)
    myScreen.update()
    pong.move()

    # Detect collision with wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # Detect collision with both paddles
    if pong.distance(rightPaddle) < 50 and pong.xcor() > 325 or pong.distance(leftPaddle) < 50 and pong.xcor() < -325:
        pong.bounce_x()

    # Detect if the ball misses the right paddle
    if pong.xcor() > 370:
        pong.reset_pos()
        score.l_score += 1
        score.updateScore()

    # Detect if the ball misses the left paddle
    if pong.xcor() < -370:
        pong.reset_pos()
        score.r_score += 1
        score.updateScore()

myScreen.exitonclick()
