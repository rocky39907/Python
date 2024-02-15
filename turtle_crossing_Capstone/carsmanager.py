from turtle import Turtle
import random
import time

COLOR = ["red", "green", "blue", "purple", "yellow"]
CAR_SPEED = ["slow", "normal", "fast", "fastest"]

class Cars(Turtle):
    '''Create a Cars manager object from this class to create new cars and manage them.'''
    def __init__(self):
        super().__init__()
        self.cars_list = []

    def newCar(self):
        '''Creating a new Car from Turtle class and appending it to the 'Cars_list' list.'''
        chance = random.randint(1, 4)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLOR))
            new_car.penup()
            start = (400, random.randint(-200, 200))
            new_car.goto(start)
            new_car.setheading(180)
            self.cars_list.append(new_car)
