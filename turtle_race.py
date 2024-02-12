from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
color = ["red", "yellow", "blue", "green", "pink", "black", "purple", "orange"]
turtle_list = []
is_race_over = False

def placeTurtle(tur_obj):
    tur_obj.penup()
    turtle_list_len = len(turtle_list)
    tur_pos = turtle_list.index(tur_obj)
    tur_obj.color(color[tur_pos])
    tur_gap = round(560 / (turtle_list_len - 1))
    tur_obj.goto(x=-380, y=(-280 + (tur_gap * tur_pos)))


turtle_count = int(screen.numinput(title="Number of participants",
                                prompt="How many turtles are participating in the race (Max 8)"))
if turtle_count > 1 and turtle_count < 9:
    for _ in range(turtle_count):
        new_turtle = Turtle(shape="turtle")
        turtle_list.append(new_turtle)
    for n in range(turtle_count):
        placeTurtle(turtle_list[n])
    my_bet = screen.textinput(title="Turtle Race", prompt="Which color of turtle you want to put your bet on: ")
    if my_bet in color:
        is_race_over = False
        while not is_race_over:
            for turtle in turtle_list:
                rand_move = random.randint(0, 10)
                turtle.forward(rand_move)
                if turtle.xcor() >= 380:
                    is_race_over = True
                    if turtle.pencolor() == my_bet.lower():
                        print(f"You WIN! {turtle.pencolor()} is the Winner!")
                    else:
                        print(f"You Lost! {turtle.pencolor()} is the Winner!")
        screen.exitonclick()
    else:
        is_race_over = True
        print(f"No turtle found with {my_bet} color!")
        screen.bye()
else:
    is_race_over = True
    print("You must enter in between 2-8 turtles for the race to happen!")
    screen.bye()



