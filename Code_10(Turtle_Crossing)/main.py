from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

myScreen.listen()
myScreen.onkey(fun=player.moveForward, key="Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    myScreen.update()
    car.create_car()
    car.move_car()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            is_game_on = False
            score.game_over()

    if player.check_finish_line():
        car.increase_speed()
        score.increaseScore()

myScreen.exitonclick()
