from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_no = random.randint(1, 6)
        if random_no == 6:
            my_car = Turtle()
            my_car.shape("square")
            my_car.shapesize(stretch_len=2, stretch_wid=1)
            my_car.color(random.choice(COLORS))
            my_car.penup()
            random_y = random.randint(-240, 240)
            my_car.goto(300, random_y)
            self.all_cars.append(my_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def increase_speed(self):
        self.carspeed += MOVE_INCREMENT
