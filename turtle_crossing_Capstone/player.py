from turtle import Turtle

START = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.setheading(90)
        self.penup()
        self.goto(START)

    def moveUp(self):
        self.forward(10)

    def movePlToInitPlace(self):
        '''Move the Player to initial place for next Level.'''
        self.hideturtle()
        self.goto(START)
        self.setheading(90)
        self.showturtle()
