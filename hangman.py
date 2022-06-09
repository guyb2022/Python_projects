import random
from hangman_drawings import hang
from hangman_word_list import word_list  

def init_blank_word(blank_word):
    """Init the blank word"""
    for index in range(len(word_choice)):
        blank_word.append('-')

def fill_blank_word(guess,word_choice,blank_word):
    """Fill in the blank word with matched words"""
    for index in range(len(word_choice)):
        if word_choice[index] == guess:
             blank_word[index] = guess 

def count_matches(guess,word_choice):
    """Count how many matches are"""
    if guess not in blank_word:
        return word_choice.count(guess)
    else:
        print('You already chosen that word, try again!')
    return 0
    
def generate_hangman(hang,lifes):
    """Print the figure"""
    print(hang[lifes-1])

    if __name__ == '__main__':
    
    print('Welcome to Hangman')
    word_choice = random.choice(word_list)
    blank_word = []
    lifes = 9
    count_t_guess = 0
    not_end = True
    init_blank_word(blank_word)
    while(not_end):
        # ask the user to guess a word
        guess = input('Guess a word?')

        #check if the guess is correct or not
        if guess in word_choice:
          count_t_guess += count_matches(guess,word_choice)
          fill_blank_word(guess,word_choice,blank_word)
          print(''.join(blank_word))
          print()
        else:
          # Create the hangman art
          generate_hangman(hang,lifes)
          lifes -= 1
        # check the end game condition
        if (lifes == 0) or count_t_guess == len(word_choice):
            not_end = False        

    if count_t_guess == len(word_choice):
        print("Well Done")
    else:
        print("Looser")
    print('Game Over')