from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class ScoreBoard(Turtle):
    """"Class to handle scores and printing scores to the screen """
    def __init__(self):
        """Init score board class"""
        super().__init__()
        self.score = 50
        self.color('white')
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        """Print the score on the screen"""
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Handle the end game case"""
        self.setposition(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score and refresh the screem"""
        self.score += 1
        self.clear()
        self.print_score()