from player import Player
from turtle import Screen
from scoreboard import Score
from carsmanager import Cars
import random
import time

# 1. Setup game screen and background color.
scr = Screen()
scr.screensize(canvheight=600, canvwidth=800, bg="black")
# 1.1. Turn off the animation effect till screen is updated
scr.tracer(n=0)

# 2. Initialize the Player and Scorer instance
player = Player()
car = Cars()
scorer = Score()

# 3. Listening on keystroke and move the turtle
scr.listen()
scr.onkeypress(fun=player.moveUp, key="Up")

# 4 Iterating through a loop to continue the Game
is_game_on = True
sleep = 0.2
while is_game_on:
    scr.update()
    time.sleep(sleep)
    # Detecting if Turtle has reached the destination,
    # then level up the player and move the Turtle to initial place
    if player.ycor() > 260:
        scorer.updateScore()
        if scorer.curr_score == 4:
            scorer.gameFinish()
            is_game_on = False
        else:
            player.movePlToInitPlace()
            sleep -= 0.05

    # Creating a new Car
    car.newCar()

    for obj in range(len(car.cars_list)):
        # Detecting if any Car has hit the Turtle, then give Game Over message
        if player.distance(car.cars_list[obj]) < 30:
            scorer.gameOver()
            is_game_on = False
            break
        # Detecting if any Car has hit the end of the road then delete it else move them by 20 pixels
        if car.cars_list[obj].xcor() > 400:
            car.cars_list[obj].delete()
        else:
            # Move the cars by 10 pixels
            car.cars_list[obj].forward(10)

# Hold the screen till clicking on it
scr.exitonclick()