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

    def bounce_y(self):from ball import Ball
from scoreboard import ScoreBoard
from paddle import Paddle
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The PONG Game")
screen.tracer(0)

l_pedal = Paddle((-385, 0))
r_pedal = Paddle((385, 0))

ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_pedal.up, "Up")
screen.onkey(r_pedal.down, "Down")
screen.onkey(l_pedal.up, "w")
screen.onkey(l_pedal.down, "s")

for index in range(-300, 330, 40):
    brick = Ball()
    brick.shape('square')
    brick.setposition(0, index)

game_on = True

while game_on:
    """Main game loop, handle the paddles/ball/scoreBoard"""
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(l_pedal) < 50 and ball.xcor() < -350 or \
            ball.distance(r_pedal) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    # Detect out of boundaries for player A
    if ball.xcor() <= -380:
        r_pedal.score += 1
        score_board.print_score(r_pedal.score, l_pedal.score)
        ball.reset_position()
    # Detect out of boundaries for player B
    elif ball.xcor() >= 380:
        l_pedal.score += 1
        score_board.print_score(r_pedal.score, l_pedal.score)
        ball.reset_position()
    # Detect if one of the player got to 10 points, then end game
    if l_pedal.score == 10 or r_pedal.score == 10:
        score_board.game_over()
        game_on = False

screen.exitonclick()

        """Bounce if the ball hit one of the walls"""
        self.y_direction *= -1

    def reset_position(self):
        """Go to the starting point after ball went out of the walls"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()




