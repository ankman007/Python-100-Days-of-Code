import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=700)
user_bet = screen.textinput(title='Make You Bet', prompt='Which turtle will win the race? Enter a color:')

colors = ('red', 'blue', 'yellow', 'green', 'orange', 'pink', 'brown')
y_position = [-150, 100, -100, 50, -50, 0]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-480, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
