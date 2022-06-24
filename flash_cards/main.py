from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "italic"
WORD_FONT = ("Ariel", 60, 'bold')
TITLE_FONT = ("Ariel", 40, FONT_NAME)
LANGUAGE_FONT = ("Ariel", 20, FONT_NAME)
# TBD: enable more languages (german/spanish/italian/...)
word_dict = {}
current_card = {}


def init_words_list():
    """
    Init the words to be learned
    TBD: add more languages with relevant dict
    """
    global word_dict
    try:
        data = pd.read_csv('data/french_word_to_learn.csv')
    except FileNotFoundError:
        original_data = pd.read_csv('data/french_words.csv')
        word_dict = original_data.to_dict(orient="records")
    else:
        word_dict = data.to_dict(orient="records")


def next_card():
    """Get the next card after pressing the check mark button"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def delete_card():
    """Remove words we already know"""
    word_dict.remove(current_card)
    # Save the new dict to file
    df = pd.DataFrame(word_dict)
    df.to_csv('data/french_word_to_learn.csv', index=False)
    next_card()


def flip_card():
    """Flip the card to the other side and replace the text"""
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(title_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


if __name__ == '__main__':
    # Init words list dict
    init_words_list()
    # Create main window
    window = Tk()
    window.title("Flashing Card - Learn Language Every Day")
    window.minsize(width=800, height=550)
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
    # Timer delay
    flip_timer = window.after(3000, func=flip_card)
    # Create Images
    front_card_img = PhotoImage(file="image/card_front.png")
    back_card_img = PhotoImage(file="image/card_back.png")
    right_img = PhotoImage(file="image/right.png")
    wrong_img = PhotoImage(file="image/wrong.png")
    # Init canvas
    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_image = canvas.create_image(400, 263, image=front_card_img)
    title_text = canvas.create_text(400, 150, text='', font=TITLE_FONT)
    word_text = canvas.create_text(400, 263, text='', font=WORD_FONT)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)
    # Create the correct button
    correct_button = Button(image=right_img, command=next_card ,highlightthickness=0)
    correct_button.grid(row=1, column=1)
    # Create the wrong button
    wrong_button = Button(image=wrong_img, command=delete_card, highlightthickness=0)
    wrong_button.grid(row=1, column=0)

    next_card()

    window.mainloop()
