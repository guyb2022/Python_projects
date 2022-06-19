from turtle import Turtle
MOVE_DISTANCE = 20
WIDTH = 800
HEIGHT = 600


class Passenger(Turtle):
    """Init the passenger object"""
    def __init__(self):
        super().__init__()
        self.lives_left = 3
        self.create_body()

    def create_body(self):
        """Create the passenger body"""
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(0, -280)
        self.speed('fastest')
        self.setheading(90)

    def reset_position(self):
        """Reset position to starting point"""
        self.goto(0, -280)

    def up(self):
        """Go up"""
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < (HEIGHT/2 + 20):
            self.goto(self.xcor(), new_y)

    def down(self):
        """Go down"""
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -HEIGHT/2:
            self.goto(self.xcor(), new_y)

    def right(self):
        """Go right"""
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < WIDTH/2:
            self.goto(new_x, self.ycor())

    def left(self):
        """Go left"""
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -WIDTH/2:
            self.goto(new_x, self.ycor())
