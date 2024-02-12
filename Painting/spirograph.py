from turtle import Turtle, Screen
import random
#from Day18_draw_random_walk import rand_color

my_turtle = Turtle()
my_screen = Screen()
my_turtle.shape("turtle")
my_turtle.speed(10)

def rand_color():
    my_screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color

def spirograph(count):
    heads_shift = round(360 / count)
    heads_pos = 0
    for _ in range(count):
        my_turtle.color(rand_color())
        my_turtle.circle(100)
        heads_pos += heads_shift
        my_turtle.setheading(heads_pos)

user_choice = int(input("How many circles to draw in the Spirograph: "))
spirograph(user_choice)

my_screen.exitonclick()