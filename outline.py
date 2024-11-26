from turtle import Turtle


class Outline(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pencolor("white")
        self.penup()
        self.teleport(350, 310)
        self.pendown()
        self.goto(350, -310)
        self.goto(-350, -310)
        self.goto(-350, 310)
        self.goto(350, 310)
