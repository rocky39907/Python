from turtle import Turtle

SCORE_BOARD_PLACE = (-20, 280)
SCORE_MAPPING = {0: "Easy",
                 1: "Medium",
                 2: "Hard",
                 3: "Expert"}
class Score(Turtle):
    def __init__(self):
        self.curr_score = 0
        self.scorer = Turtle()
        self.scorer.color("red")
        self.scorer.hideturtle()
        self.scorer.penup()
        self.scorer.goto(SCORE_BOARD_PLACE)
        self.scorer.write(arg=f"Level: {SCORE_MAPPING[self.curr_score]}", align="center", font=("arial", 14, "bold"))

    def gameOver(self):
        '''Displays GAME OVER message in the center of the screen.'''
        self.scorer.color("red")
        self.scorer.home()
        self.scorer.write(arg="! GAME OVER !", align="center", font=("arial", 20, "bold"))

    def gameFinish(self):
        '''Displays GAME OVER message in the center of the screen.'''
        self.scorer.color("red")
        self.scorer.home()
        self.scorer.write(arg="!! You are CHAMPION. No more level left!!", align="center", font=("arial", 20, "bold"))

    def updateScore(self):
        '''Update the score by 1.'''
        self.curr_score += 1
        self.scorer.clear()
        self.scorer.write(arg=f"Level: {SCORE_MAPPING[self.curr_score]}", align="center", font=("arial", 14, "bold"))
