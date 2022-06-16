from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        score_board.print_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 285 or \
            snake.head.xcor() < -285 or \
            snake.head.ycor() > 285 or \
            snake.head.ycor() < -285:
        game_on = False
        score_board.game_over()

    # detect collision of head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()
