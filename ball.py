from turtle import Turtle
class Ball(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(x,y)
        self.x_move=14
        self.y_move=14
        self.move_speed=0.1
    def movement(self):
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x_cor,y_cor)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed*=0.9
    def ball_reset(self):
        self.goto(0,0)
        self.x_move *= -1
        self.move_speed=0.1
