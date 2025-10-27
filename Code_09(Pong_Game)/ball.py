from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_pos = 10
        self.y_pos = 10
        self.ball_move = 0.1

    def move(self):
        x_axis = self.xcor() + self.x_pos
        y_axis = self.ycor() + self.y_pos
        self.goto(x_axis, y_axis)

    def bounce_y(self):
        self.y_pos *= -1

    def bounce_x(self):
        self.x_pos *= -1
        self.ball_move *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.ball_move = 0.1
        self.bounce_x()
