from turtle import *
import random
from Modules import Data

screen = Screen()

screen.bgcolor('black')
setpos(10, -200)
shape('turtle')
speed(10)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        backward(100)
        right(angle)


for shape_side_n in range(3, 19):
    color(random.choice(Data.colors))
    draw_shape(shape_side_n)

screen.exitonclick()




