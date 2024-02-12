from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.curr_score = 0
        self.scorer = Turtle()
        self.scorer.color("white")
        self.scorer.hideturtle()
        self.scorer.penup()
        self.scorer.goto(-50, 330)
        self.scorer.write(arg=f"Score: {self.curr_score}", align="center", font=("arial", 14, "bold"))

    def gameOver(self):
        '''Displays GAME OVER message in the center of the screen.'''
        self.scorer.color("red")
        self.scorer.home()
        self.scorer.write(arg="! GAME OVER !", align="center", font=("arial", 20, "bold"))

    def updateScore(self):
        '''Update the score by 1.'''
        self.curr_score += 1
        self.scorer.clear()
        self.scorer.write(arg=f"Score: {self.curr_score}", align="center", font=("arial", 14, "bold"))
