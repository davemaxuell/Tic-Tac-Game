from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from outline import Outline
from ball import Ball
import time

board = Screen()
board.setup(900, 700)
board.bgcolor("black")
board.title("PONG!")

outline = Outline()

right_paddle = Paddle()
right_paddle.teleport(340, 0)
right_score = Scoreboard()
right_score.goto(50, 305)
right_score.write_score()

left_paddle = Paddle()
left_paddle.teleport(-340, 0)
left_score = Scoreboard()
left_score.goto(-50, 305)
left_score.write_score()

board.listen()
board.onkey(right_paddle.upwards, "Up")
board.onkey(right_paddle.downwards, "Down")
board.onkey(left_paddle.upwards, "w")
board.onkey(left_paddle.downwards, "s")

ball = Ball()

while True:
    time.sleep(0.02)
    board.update()
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.setheading(360 - ball.heading())

    if ball.xcor() > 320 and right_paddle.ycor() + 50 >= ball.ycor() >= right_paddle.ycor() - 50:
        ball.setheading(180 - ball.heading())
        # faster ball each time blocked
        ball.make_harder()
    if ball.xcor() < -320 and left_paddle.ycor() + 50 >= ball.ycor() >= left_paddle.ycor() - 50:
        ball.setheading(180 - ball.heading())
        # faster ball each time blocked
        ball.make_harder()

    if ball.xcor() >= 340:
        for i in range(1, 10, +1):
            ball.blinking()
        left_score.update()
        ball.home()
        ball.make_heading()
    if ball.xcor() <= -340:
        for i in range(1, 10, +1):
            ball.blinking()
        right_score.update()
        ball.home()
        ball.make_heading()

    ball.ball_move()


board.exitonclick()
