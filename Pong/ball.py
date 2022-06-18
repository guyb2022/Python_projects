from turtle import Turtle


class Ball(Turtle):
    """Class to create the ball for the game."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.x_direction = 20
        self.y_direction = 20
        self.speed('fastest')
        self.ball_speed = 0.1

    def move(self):
        """Move the ball to the new position"""
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Bounce if the ball hit one of the paddles"""
        self.x_direction *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        """Bounce if the ball hit one of the walls"""
        self.y_direction *= -1

    def reset_position(self):
        """Go to the starting point after ball went out of the walls"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()




