import turtle
from turtle import *
import random

screen = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


speed('fastest')


def draw_spirograph(size_of_graph):
    xc = 0
    yc = 0
    for _ in range(int(360 / size_of_graph)):
        color(random_color())
        circle(100)
        setheading(heading() + size_of_graph)


draw_spirograph(2)
screen.exitonclick()
