import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def play_game(attempts):
    """Main game funcion"""
    num_attemtps = attempts
    num_to_guess = random.randint(1,100)
    not_end = True
    while not_end:
        print(f'You have {num_attemtps} attempts reamiaing to guess the number')
        guess = int(input('Make a guess: '))
        if guess == num_to_guess:
            print("You are right!!!")
            not_end = False
        elif guess < num_to_guess:
            print("Too Low.")
            num_attemtps -= 1
        elif guess > num_to_guess:
            print("Too High.")
            num_attemtps -= 1
        
        if num_attemtps == 0:
            print("You've run out of guesses!!!\nLooser ")
            not_end = False
        else:
            print("Guess Again.")
    print(f'Number to guess was: {num_to_guess}')

def set_difficulty():
    dificulty = input("Choose dificulty: 'easy' or 'hard': ")
    if dificulty == 'easy':
        attempts = EASY_LEVEL
    else:
        attempts = HARD_LEVEL 
    return attempts
    
if __name__ == '__main__':
    print("Welcome To The Number Guessing Game")
    play_game(set_difficulty())
