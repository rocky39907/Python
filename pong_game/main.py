import time
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball

# Setting up main screen
mainScr = Screen()
mainScr.screensize(canvwidth=800, canvheight=600)
mainScr.bgcolor("black")
mainScr.tracer(n=0)

# Setting up divider using a Turtle object and placing the Ball
scrDivider = Turtle()
scrDivider.penup()
scrDivider.color("white")
scrDivider.hideturtle()
scrDivider.speed("fastest")
scrDivider.goto(0, -270)
scrDivider.pendown()
scrDivider.goto(0, 260)

# Initializing Ball and Score instance
ball = Ball()
score = Score()
START = (0, -290)

# Setting up the Paddle for both side by initializing Paddle Class Object
rpaddle = Paddle("R")
lpaddle = Paddle("L")

# Moving the paddles up and down based on Keyboard input
mainScr.listen()
mainScr.onkeypress(key="Up", fun=lpaddle.up)
mainScr.onkeypress(key="Left", fun=lpaddle.down)
mainScr.onkeypress(key="Right", fun=rpaddle.up)
mainScr.onkeypress(key="Down", fun=rpaddle.down)

# Keeping the Game On till the ball hits a wall
is_game_on = True
ball_direction = "right"
while is_game_on:
    mainScr.update()
    ball.moveBall(ball_direction)
    time.sleep(0.1)
    print(ball.pos())

    # Collision detection of the ball with the paddle
    for seg in range(5):
        if ball.distance(rpaddle.segment[seg]) < 20 or ball.distance(lpaddle.segment[seg]) < 20:
            # Count the score
            score.updateScore()
            while ball.distance(START) > 10:
                ball.backward(20)
                mainScr.update()
                time.sleep(0.08)
                #print(ball.pos())
            if ball_direction == "left":
                ball_direction = "right"
            else:
                ball_direction = "left"

    # Collision detection of the ball with the wall
    if ball.xcor() < -380 or ball.xcor() > 380:
        is_game_on = False
        # Game Over message
        score.gameOver()

mainScr.exitonclick()