from turtle import Turtle, Screen
import random

SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.make_ball()

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.make_heading()
        if self.heading() == 90 or self.heading() == 270:
            self.make_heading()  # Avoid purely vertical heading

    def make_heading(self):
        self.setheading(random.randrange(0, 360))

    def bounce_to_wall(self):
        self.setheading(360 - self.heading())  # Reverse vertical direction

    def bounce_to_paddle(self):
        self.setheading(180 - self.heading())  # Reverse horizontal direction

    def move(self):
        self.forward(SPEED)
        self.check_collision()
        screen.ontimer(self.move, 20)  # Repeatedly call move every 20 ms

    def check_collision(self):
        x, y = self.xcor(), self.ycor()

        # Check for collision with top or bottom wall
        if y > 290 or y < -290:  # Assuming screen height is 600
            self.bounce_to_wall()

        # Check for collision with left or right wall
        if x > 390 or x < -390:  # Assuming screen width is 800
            self.bounce_to_paddle()


# Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create and start the ball
ball = Ball()
ball.move()  # Start moving the ball

# Keep the window open until closed by the user
screen.mainloop()
