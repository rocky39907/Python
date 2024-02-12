from turtle import Turtle

SNAKE_COORD = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_obj_list = []
        self.initialBody()
        self.head = self.snake_obj_list[0]

    def initialBody(self):
        '''Build the initial body of the snake with 3 snake objects (These are 3 turtle class object).'''
        for pos in SNAKE_COORD:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.speed("fastest")
            new_snake.goto(pos)
            self.snake_obj_list.append(new_snake)

    def extendBody(self):
        '''Add one snake object to the end of the snake body. Should be called
        only after an initial snake body is already built up.'''
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.goto(self.snake_obj_list[-1].pos())
        self.snake_obj_list.append(new_snake)

    def moveSnake(self):
        '''Move the snake head by 20 steps forward and n-2 segment to n-1 place.'''
        for obj in range(len(self.snake_obj_list) - 1, 0, -1):
            new_xcor = self.snake_obj_list[obj - 1].xcor()
            new_ycor = self.snake_obj_list[obj - 1].ycor()
            self.snake_obj_list[obj].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        '''Allow the snake to turn upward if it's not moving from downward direction currently.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Allow the snake to turn downward if it's not moving from upward direction currently.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Allow the snake to turn left if it's not moving from right direction currently.'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Allow the snake to turn right if it's not moving from left direction currently.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
