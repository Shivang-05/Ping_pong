from turtle import Turtle
class Slide(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x,y)
    def move_up(self):
       newy_cor=self.ycor()+25
       self.goto(self.xcor(),newy_cor)
    def move_down(self):
       newy_cor=self.ycor()-25
       self.goto(self.xcor(),newy_cor)

