from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_screen = Screen()
def rand_color():
    my_screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


def draw_shape(total_steps):
    direction = [0, 90, 180, 270]
    my_turtle.pensize(15)
    for _ in range(total_steps):
        my_turtle.color(rand_color())
        my_turtle.forward(30)
        my_turtle.setheading(random.choice(direction))

user_input = int(input("How many steps do you want to move: "))
draw_shape(user_input)

my_screen.exitonclick()
