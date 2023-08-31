import turtle
from turtle import *
import random
from Modules import Data

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


angle = [0, 90, 180, 270]
width(10)
speed("fast")

screen = Screen()
screen.bgcolor("black")

for _ in range(200):
    color(random_color())
    forward(30)
    setheading(random.choice(angle))

screen.exitonclick()
