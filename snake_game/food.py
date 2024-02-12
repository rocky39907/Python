import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refreshFood()

    def refreshFood(self):
        '''Get a random X and Y axis position of the food and move it from center to that position.'''
        self.x_cor = random.randint(-360, 360)
        self.y_cor = random.randint(-310, 310)
        self.goto(self.x_cor, self.y_cor)
