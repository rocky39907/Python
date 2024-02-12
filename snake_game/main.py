from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# Creating an object from Turtle and Screen class to get hold of class methods
scr = Screen()
scr.bgcolor("black")

# Setting up screen size of 800X700 mm
scr.setup(width=800, height=700)

# Turning Off animation effect to show all snake objects together
scr.tracer(n=0)

#Building the Snake and initializing Scoreboard
snake = Snake()
score = Score()

# Listening on Keystroke to move the snake in that direction
scr.listen()
scr.onkeypress(fun=snake.up, key="Up")
scr.onkeypress(fun=snake.down, key="Down")
scr.onkeypress(fun=snake.right, key="Right")
scr.onkeypress(fun=snake.left, key="Left")

is_game_on = True
new_food = Food()

# Looping through to continue moving the snake
while is_game_on:
    # Refreshing the screen every 10 milliseconds
    scr.update()
    time.sleep(0.1)

    # Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        is_game_on = False
        score.gameOver()
        pass

    # Detect collision with Tail
    for snake_obj in snake.snake_obj_list[1:]:
        if snake.head.distance(snake_obj) < 10:
            is_game_on = False
            score.gameOver()
            pass
    snake.moveSnake()

    # Detect collision with food
    if snake.head.distance(new_food) < 15:
        snake.extendBody()
        score.updateScore()
        new_food.refreshFood()

scr.exitonclick()