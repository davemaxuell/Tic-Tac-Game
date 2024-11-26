from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.make_paddle()

    def make_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed(0)

    def upwards(self):
        if self.ycor() <= 250:
            self.goto(x=self.xcor(), y=self.ycor()+20)

    def downwards(self):
        if self.ycor() > -250:
            self.goto(x=self.xcor(), y=self.ycor()-20)

