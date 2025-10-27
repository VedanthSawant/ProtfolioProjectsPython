from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle_pos = position
        self.createPaddle()

    def createPaddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.paddle_pos)

    def up(self):
        if self.ycor() < 270:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(), self.ycor() - 20)