import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('U.S. State Quiz Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title='Guess the US State', prompt="What's another state's name?")
print(answer_state)

