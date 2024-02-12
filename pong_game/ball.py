from turtle import Turtle
import random

START = (0, -290)

class Ball(Turtle):

    def __init__(self):
        '''Initialize a Ball Object and move it to it's initial position.'''
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("blue")
        self.penup()
        self.goto(START)

    def moveBall(self, direction):
        '''Arg (Type: str): direction: 'right' or 'left'.
        Moving the ball to either right or left of the screen in a random angle.'''
        if self.distance(START) < 10:
            if direction == "right":
                angle = random.randint(30, 55)
            else:
                angle = random.randint(130, 165)
            self.setheading(angle)
            #print(angle)
        self.forward(20)


