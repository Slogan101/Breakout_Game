from turtle import Turtle
import random
COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

# x = -230
# y = 120

class Block(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.penup()
        self.goto(x=x, y=y)
        # self.quantity = random.choice(weights)


class Blocks:
    def __init__(self):
        self.y_start = 30
        self.y_end = 160
        self.blocks = []
        self.create()


    def create_lane(self, y_cor):
        for i in range(-230, 230, 35):
            brick = Block(i, y_cor)
            self.blocks.append(brick)

    def create(self):
        for i in range(self.y_start, self.y_end, 22):
            self.create_lane(i)

