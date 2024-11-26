from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.hideturtle()
        self.penup()
        self.speed(0)

    def write_score(self):
        self.pendown()
        self.pencolor("white")
        self.write(f"{self.point}", font=("Arial", 30, "bold"))

    def update(self):
        self.clear()
        self.point += 1
        self.write(f"{self.point}", font=("Arial", 30, "bold"))
