from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 50, 'normal')


class ScoreBoard(Turtle):
    """"Class to handle scores and printing scores to the screen """
    def __init__(self):
        """Init score board class"""
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.setposition(0, 230)
        self.hideturtle()
        self.print_score(0, 0)

    def print_score(self, score_r, score_l):
        """Print the score on the screen"""
        self.clear()
        self.write(f'{score_l}          {score_r}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Handle the end game case"""
        self.clear()
        self.setposition(0, 0)
        self.write(f'GAME  OVER', align=ALIGNMENT, font=FONT)
