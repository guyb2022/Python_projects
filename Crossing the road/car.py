from turtle import Turtle
import random
WIDTH = 800
HEIGHT = 600
COLORS = ['red', 'green', 'black', 'purple', 'orange', 'brown']
SPEED_CAR = 10


class CarPool(Turtle):
    """Init class for the car"""
    def __init__(self):
        """Init score board class"""
        super().__init__()
        self.speed_car = SPEED_CAR
        self.hideturtle()
        self.cars_list = []
        self.create_car()

    def cars_move(self):
        """Move the cars to the new position"""
        for car in self.cars_list:
            car.backward(-self.speed_car)

    def create_car(self):
        """Create new car"""
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(400, random.randint(-HEIGHT/2+60, HEIGHT/2-60))
        new_car.speed('fastest')
        new_car.setheading(180)
        self.cars_list.append(new_car)

    def reset_position(self, x, y):
        """Reset the car position after hitting left wall"""
        self.goto(x, y)

    def speed_up(self):
        self.speed_car += 5
