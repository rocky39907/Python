import random
from turtle import Turtle, Screen
from random import Random

my_turtle = Turtle()
my_turtle.shape("turtle")

def draw_shape(total_shape):
    color = ["red", "green", "blue", "pink", "purple", "black", "yellow", "orange", "violet"]
    lines = 3
    width = 5
    while lines < total_shape+3:
        my_turtle.color(random.choice(color))
        for _ in range(lines):
            my_turtle.pensize(width)
            my_turtle.forward(100)
            my_turtle.right(360 / lines)
        lines += 1
        width += 1

user_input = int(input("How many shapes do you want: "))
draw_shape(user_input)


my_screen = Screen()
my_screen.exitonclick()