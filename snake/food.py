from turtle import Turtle
import random
COLORS = ['red', 'green', 'white', 'purple', 'orange', 'brown']

class Food(Turtle):
    """Class to hold all the food requirements"""
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Set new food at random place"""
        self.color(random.choice(COLORS))
        self.setposition(random.randint(-280, 280), random.randint(-280, 280))



