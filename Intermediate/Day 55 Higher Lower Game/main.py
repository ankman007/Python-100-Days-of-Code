from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(1, 5)

@app.route('/')
def home():
    return '<h1>Guess a number between 1 - 5.</h1><br>' \
           '<img width=200 height=200 src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjU0dTh1Zmd4enR1NHY0YjdtbTd4MDdvYjZzejJoOWlycnFqcmd6ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUn3CftPBajoflzROU/giphy-downsized-large.gif">'

@app.route('/<number>')
def check_number(number):
    if random_num == int(number):
        return f'<h1>You guess was correct</h1><br>' \
               '<img width=200 height=200 src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTFwOHlzd3huNmg0cndqMzQ4ZXlwNzZwNGFiYTd4bmJnNWkwbDRieiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UAXK9VGoJTbdcPgmcJ/giphy.gif">'
    elif random_num < int(number):
        return f'<h1>Too High. Please try again.</h1><br>' \
               '<img width=200 height=200 src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3ZlenZvenMzZDAzODU3aWFrdW5hbnhnbnFndzhqNHBvajRzcm1zeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dnFqm7tIPOwK9pOFzq/giphy.gif">'

    elif random_num > int(number):
        return f'<h1>Too Low. Please try again.</h1><br>' \
               '<img width=200 height=200 src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWN4eXRzc3ZuMzljZXJkaDN4MWM1NWNya3cxN3RreHh0cWJycHVyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif">'

app.run(debug=True)



