from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_screen = Screen()

def rand_color():
    my_screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color



my_turtle.shape("turtle")
my_turtle.speed("fastest")
my_turtle.hideturtle()
for r in range(-100, 100, 20):
    my_turtle.penup()
    my_turtle.setpos(-100, r)
    for c in range(10):
        #my_turtle.color(rand_color())
        my_turtle.pendown()
        #my_turtle.begin_fill()
        my_turtle.dot(10, rand_color())
        #my_turtle.end_fill()
        my_turtle.penup()
        my_turtle.forward(20)
    # my_turtle.left(90)
    # my_turtle.penup()
    # my_turtle.forward(10)
    # my_turtle.left(90)
    # my_turtle.pendown()



my_screen.exitonclick()