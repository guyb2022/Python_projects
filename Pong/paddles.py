from turtle import Turtle
POSITIONS = [(0, 20), (0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 40
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.segments = []
        self.score = 0
        self.position = position
        self.create_body()
        self.body = None

    def create_body(self):
        """Creation the player pedal, initialize with 4 blocks"""
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(self.position)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(UP)

    def up(self):
        """Using the up arrow key to go up"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """Using the down arrow key to go down"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
