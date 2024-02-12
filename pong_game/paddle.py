from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, side):
        '''Arg (Type: str): side: 'R' for Right or 'L' for Left side.
        Build a paddle in either Left or Right side of the screen based on passed Argument.'''
        super().__init__()
        self.segment = []
        self.side = side
        if self.side.lower() == "r":
            self.buildPaddle(x=360)
        else:
            self.buildPaddle(x=-360)

    def buildPaddle(self, x):
        '''Arg (Type Int): x: Takes the X axis value to start building paddle at that position.'''
        for y_cor in range(-40, 60, 20):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            new_segment.goto(x, y_cor)
            self.segment.append(new_segment)

    def move(self, direction):
        '''Arg (Type Int): direction: An integer Angle (90 or 270 degree) to move the Paddle Up or Down ward.'''
        for seg in self.segment:
            seg.speed("fastest")
            if direction == 90:
                if self.segment[-1].ycor() > 280:
                    pass
                else:
                    seg.setheading(direction)
                    seg.forward(DISTANCE)
            else:
                if self.segment[-1].ycor() < -190:
                    pass
                else:
                    seg.setheading(DOWN)
                    seg.forward(DISTANCE)

    def up(self):
        self.move(direction=UP)

    def down(self):
        self.move(direction=DOWN)