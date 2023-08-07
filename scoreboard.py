from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
        contents = int(contents)
        self.high_score = contents
        self.color("white")
        self.calculate_score()

    def calculate_score(self):
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        str_high_score = str(self.high_score)
        with open("data.txt", mode="w") as file:
            file.write(str_high_score)
        self.calculate_score()
