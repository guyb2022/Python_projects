from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "italic"
FONT = ("Ariel", 15, FONT_NAME)


class QuizInterface:
    """
    Quiz UI gets the quiz bank through quiz_brain
    Initialize all the UI graphics components
    """
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Creating the window
        self.window = Tk()
        self.window.title("Brain Quizzer")
        self.question_bank = []
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # creating the canvas
        self.canvas = Canvas(width=400, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text='Blank',
                                                     font=FONT,
                                                     fill=THEME_COLOR,
                                                     width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Labels
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=FONT, fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.score_label.focus()
        # Create buttons
        true_img = PhotoImage(file="./images/true.png")
        self.True_button = Button(image=true_img, command=self.true_answer, highlightthickness=0)
        self.True_button.grid(column=0, row=2)
        false_img = PhotoImage(file="./images/false.png")
        self.False_button = Button(image=false_img, command=self.false_answer, highlightthickness=0)
        self.False_button.grid(column=1, row=2)
        # calling next question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetch the next question"""
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")

    def true_answer(self):
        """The True button was pressed"""
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        """The False button was pressed"""
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        """Give feedback on the answer that was pressed"""
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)