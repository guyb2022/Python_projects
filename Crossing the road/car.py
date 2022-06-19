from turtle import Turtle
import random
WIDTH = 800
HEIGHT = 600
COLORS = ['red', 'green', 'black', 'purple', 'orange', 'brown']


class Car(Turtle):
    """Init class for the car"""
    def __init__(self):
        """Init score board class"""
        super().__init__()
        self.create_car()

    def cars_move(self, cars):
        """Move the cars to the new position"""
        for car in cars:
            new_x = car.xcor() - 20
            car.goto(new_x, car.ycor())

    def create_car(self):
        """Create new car"""
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(400, random.randint(-HEIGHT/2+20, HEIGHT/2-40))
        self.speed('fastest')
        self.setheading(180)

    def reset_position(self, x, y):
        """Reset the car position after hitting left wall"""
        self.goto(x, y)
