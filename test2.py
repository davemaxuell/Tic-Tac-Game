import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Bouncing Ball")

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)  # Fastest drawing speed

# Set initial movement angle and speed
ball.setheading(22)  # Initial direction in degrees
ball_speed = 10

# Define the boundary limits
boundary = 290  # Since screen size is 600x600, limit is 290 to stay within bounds

# Ball movement and bouncing function
def move_ball():
    # Move the ball forward
    ball.forward(ball_speed)

    # Get the ball's current position
    x, y = ball.xcor(), ball.ycor()

    # Check for collision with the top or bottom wall
    if y > boundary or y < -boundary:
        ball.setheading(360 - ball.heading())  # Reverse the vertical direction

    # Check for collision with the left or right wall
    if x > boundary or x < -boundary:
        ball.setheading(180 - ball.heading())  # Reverse the horizontal direction

    # Continue moving the ball
    screen.ontimer(move_ball, 10)  # Repeat movement every 20 ms

# Start moving the ball
move_ball()

# Keep the window open until closed by the user
turtle.done()
