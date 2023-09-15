from turtle import Screen
from blocks import Blocks
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=500, height=400)
screen.bgcolor('black')
screen.title("Breakout Game")
x = -230
y = 120
screen.tracer(0)
screen.listen()

ball = Ball()
block = Blocks()

def collision():
    for bl in block.blocks:
        if ball.distance(bl) < 30:
            scoreboard.increase_score()
            bl.clear()
            bl.goto(3000, 3000)
            block.blocks.remove(bl)
            ball.bounce_y()


paddle = Paddle()
screen.onkey(key='Right', fun=paddle.righ)
screen.onkey(key='Left', fun=paddle.lef)

Game_on = True

while Game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    collision()

    if ball.ycor() > 180 or ball.distance(paddle) < 35:
        ball.bounce_y()
    if ball.xcor() > 225 or ball.xcor() < -225:
        ball.bounce_x()
    if ball.ycor() < -180:
        ball.reset_position()
        scoreboard.reset_()








screen.mainloop()