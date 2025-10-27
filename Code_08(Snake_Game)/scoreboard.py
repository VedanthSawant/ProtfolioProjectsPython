from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_path = "highest_score.txt"
        if os.path.isfile(self.file_path):
            with open(self.file_path) as file:
                content = file.read()
                self.high_score = content
        else:
            self.high_score = 0
            with open(self.file_path, "w") as file:
                file.write(f"{self.high_score}")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def resetScore(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open(self.file_path, "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.updateScore()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScore()
