from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """Class to handle the snake"""
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        """Create the main snake body with 3 initials squares"""
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adding on new segment to the snake body"""
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.setposition(position)
        self.segments.append(tim)

    def extend(self):
        """Adding new segment to the rear part"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward, the tail is follow along the head"""
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].setposition(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Using the up arrow key to go up"""
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        """Using the down arrow key to go down"""
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        """Using the left arrow key to go left"""
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        """Using the right arrow key to go right"""
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
