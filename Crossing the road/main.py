from turtle import Screen, Turtle
from passenger import Passenger
from car_pool import CarPool
from scoreboard import ScoreBoard
import time
import random

WIDTH = 800
HEIGHT = 600
LIVES = 3
FONT = ('Arial', 40, 'normal')
# Create the screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('white')
screen.title("The turtle Road Game")
screen.tracer(0)
# Create passenger object
passenger = Passenger()
# create the car objects
carpool = CarPool()
# create the scoreboard
scoreboard = ScoreBoard()

lives = []
# Create the lives icons
for index in range(LIVES):
    lives_p = Turtle()
    lives_p.penup()
    lives_p.shape('turtle')
    lives_p.color('black')
    lives_p.setposition(WIDTH / 2 - 30 * (1 + index), HEIGHT / 2 - 20)
    lives.append(lives_p)
# Listen to keys pressed for direction changes
screen.listen()
screen.onkey(passenger.up, "Up")
screen.onkey(passenger.down, "Down")
screen.onkey(passenger.left, "Left")
screen.onkey(passenger.right, "Right")

game_on = True
time_sleep = 0.5
# Starting the game
while game_on:
    """Main game loop, handle the passenger/cars/scoreBoard"""
    screen.update()
    time.sleep(time_sleep)
    carpool.cars_move()

    # Detect collision with cars
    for car in carpool.cars_list:
        if passenger.distance(car) < 20:
            time_sleep = 1
            scoreboard.level = 1
            scoreboard.print_score()
            lives[passenger.lives_left-1].hideturtle()
            passenger.lives_left -= 1
            passenger.reset_position()
            time.sleep(0.5)
            scoreboard.goto(0, 0)
            if passenger.lives_left >= 1:
                scoreboard.write('You lost 1 live\n  Try Again', align='center', font=FONT)
                time.sleep(1)
            elif passenger.lives_left == 0:
                scoreboard.write('LAST CHANCE', align='center', font=FONT)
                time.sleep(1)
            scoreboard.clear()
            scoreboard.print_score()
            break

    # If all lives were depleted
    if passenger.lives_left < 0:
        scoreboard.game_over()
        game_on = False

    # If last level was achieved
    if scoreboard.level > 10:
        scoreboard.goto(0, 0)
        scoreboard.write('WELL DONE\n YOU WON!!!', align='center', font=FONT)
        time.sleep(3)
        scoreboard.game_over()
        game_on = False

    # create the care randomly
    if random.randint(0, 100) > 50:
        carpool.create_car()

    # delete the car after reaching the left side
    for car in carpool.cars_list:
        if car.xcor() < -390:
            del car

    # Advance the level after turtle reaches the upper boarder
    if passenger.ycor() > HEIGHT/2-20:
        scoreboard.level += 1
        scoreboard.print_score()
        passenger.reset_position()
        carpool.speed_up()

screen.exitonclick()
