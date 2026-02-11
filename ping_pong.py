from turtle import Turtle,Screen
from scoreboard import Scoreboard
from dash import Slide
from ball import Ball
import time
timmy=Turtle("square")
screen=Screen()
screen.setup(height=600,width=800)
screen.tracer(0)
slide1=Slide(350,0)
slide2=Slide(-350,0)
screen.title("Ping pong")
screen.bgcolor("black")
screen.listen()
screen.onkey(slide1.move_up,"Up")
screen.onkey(slide1.move_down,"Down")
screen.onkey(slide2.move_up,"w")
screen.onkey(slide2.move_down,"s")
ball=Ball(0,0)
scoreboard=Scoreboard()
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.xcor()>325 and ball.distance(slide1)<50 or ball.xcor()<-325 and ball.distance(slide2)<50 :
        ball.bounce_x()
    if ball.xcor()>400 :
        ball.ball_reset()
        scoreboard.update_score2()
        # ball.move_speed()
    if ball.xcor()<-400:
        ball.ball_reset()
        scoreboard.update_score1()
        # ball.move_speed()







screen.exitonclick()
