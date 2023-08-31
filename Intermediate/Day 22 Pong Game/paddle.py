from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.listen()

class Paddle(Turtle):
    def __init__(self, position):
        self.x_cor = position[0]
        self.y_cor = position[1]

        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x_cor, self.y_cor)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

