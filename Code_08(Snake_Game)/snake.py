from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.x_axis = 0
        self.allTurtles = []
        self.createSnake()

    def createSnake(self):
        for item in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=self.x_axis, y=0)
            self.x_axis -= 20
            self.allTurtles.append(new_turtle)

    def extendSnake(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.allTurtles[-1].position())
        self.allTurtles.append(new_turtle)

    def resetSnake(self):
        for eachTurtle in self.allTurtles:
            eachTurtle.goto(1000, 1000)
        self.allTurtles.clear()
        self.createSnake()

    def move(self):
        for seg in range(len(self.allTurtles) - 1, 0, -1):
            x_axis = self.allTurtles[seg - 1].xcor()
            y_axis = self.allTurtles[seg - 1].ycor()
            self.allTurtles[seg].goto(x_axis, y_axis)
        self.allTurtles[0].forward(10)

    def up(self):
        if self.allTurtles[0].heading() != DOWN:
            self.allTurtles[0].setheading(UP)

    def down(self):
        if self.allTurtles[0].heading() != UP:
            self.allTurtles[0].setheading(DOWN)

    def right(self):
        if self.allTurtles[0].heading() != LEFT:
            self.allTurtles[0].setheading(RIGHT)

    def left(self):
        if self.allTurtles[0].heading() != RIGHT:
            self.allTurtles[0].setheading(LEFT)

