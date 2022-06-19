from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
FONT_GAME_OVER = ('Arial', 40, 'normal')
WIDTH = 800
HEIGHT = 600


class ScoreBoard(Turtle):
    """"Class to handle scores and printing scores to the screen """
    def __init__(self):
        """Init score board class"""
        super().__init__()
        self.level = 1
        self.lives = 3
        self.lives_list = []
        self.print_score()

    def print_score(self):
        """Print the score on the board"""
        self.clear()
        self.color('black')
        self.penup()
        self.setposition(-WIDTH/2+80, HEIGHT/2-40)
        self.hideturtle()
        self.write(f"LEVEL {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Handle the end game case"""
        self.clear()
        self.setposition(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT_GAME_OVER)

