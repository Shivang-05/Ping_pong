from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score_1=0
        self.score_2=0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-320, 260)
        self.write(f'SCORE:{self.score_2}', move=False, align="center", font=("Arial", 12, "normal"))
        self.goto(320, 260)
        self.write(f'SCORE:{self.score_1}', move=False, align="center", font=("Arial", 12, "normal"))
    def update_score1(self):
        self.score_1+=1
        self.update_scoreboard()
    def update_score2(self):
        self.score_2+=1
        self.update_scoreboard()


