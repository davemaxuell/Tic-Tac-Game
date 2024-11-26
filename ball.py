from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_ball = 5
        self.make_ball()

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.make_heading()
        if self.heading() == 90 or self.heading() == 270:
            self.make_heading()

    def make_heading(self):
        self.setheading(random.randrange(0, 360))
        
    def ball_move(self):
        self.forward(self.speed_ball)

    def blinking(self):
        self.hideturtle()
        time.sleep(0.05)
        self.showturtle()
        time.sleep(0.05)

    def make_harder(self):
        self.speed_ball += 0.3
