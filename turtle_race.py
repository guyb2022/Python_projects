from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
winner_color = screen.textinput(title='Turtle race bets', prompt='Who will win? choose color')

colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown']


def init_turtles():
    """Init all turtles with shape/color"""
    x = -240
    y = -100
    for index in range(10):
        tim = Turtle(shape='turtle')
        tim.color(random.choice(colors))
        tim.penup()
        tim.setposition(x, y)
        y += 25


def start_race():
    """Starting the race with all turtles initiated"""
    not_win = True
    while not_win:
        for turtle in screen.turtles():
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= 220 and not_win:
                turtle_winning_color = turtle.pencolor()
                not_win = False
                if turtle_winning_color == winner_color:
                    print('You won!!!')
                else:
                    print('You lost!!!')


init_turtles()
start_race()

screen.exitonclick()
