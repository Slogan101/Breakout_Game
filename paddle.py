from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=0.7, stretch_len=7)
        self.penup()
        self.goto(x=0, y=-180)

    def righ(self):
        self.fd(50)
        # newy = self.xcor() + 20
        # self.goto(x=newy, y=self.ycor())

    def lef(self):
        self.bk(50)
        # self.newy = self.xcor() - 20
        # self.goto(x=self.newy, y=self.ycor())