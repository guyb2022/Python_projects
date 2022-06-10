from art import logo
import random
from replit import clear

print(logo)

def check_sum(hand):
    """Inner check for each cycle of checks"""
    sum = 0
    for index in range(len(hand)):
        sum += hand[index]
    return sum

def check_total_sum(hand):
    """
    Check the total sum of the hand
    Take into consideration the case 11 is in the hand
    In this case we need to check both 11=11 and 11=1
    """
    sum = check_sum(hand)
    
    if 11 not in hand:
        return sum
    elif 11 in hand and sum <= 21:
        return sum
    elif 11 in hand and sum > 21:
        while 11 in hand:
            hand[hand.index(11)] = 1
            sum = check_sum(hand)
            if sum < 22:
                return sum
    return sum
        
def take_card():
    """Return a new card randomly"""
    cards_pack = [11,10,10,10,10,9,8,7,6,5,4,3,2]
    return random.choice(cards_pack)

def init_players_hands(player1,player2):
    """Init first round before taking new card"""
    player1.append(take_card())
    player1.append(take_card())
    player2.append(take_card())
    return player1, player2

def play_player_hand(player_hand, player_result):
    """
    Create all moves for player until he decide to stop taking new card
    Or his hand get 21 or above
    """
    not_end = True
    while not_end:
        choice = input("Do you want another card? 'Y' or 'N': ").lower()
        if  choice == 'y':
            player_hand.append(take_card())
            player_result = check_total_sum(player_hand)
            print(f'Your hand: {player_hand} - Current score: {player_result}')
            if player_result == 21:
                print('You Win!!!')
                return 21
            if player_result > 21:
                print('You are Busted!!!')
                return 22
        else:
            not_end = False
    return player_result
        
def play_diller_hand(diller_hand, player_result):
    """Create all moves for diller until he reach optimal hand"""
    not_end = True
    while not_end:
        diller_hand.append(take_card())
        diller_result = check_total_sum(diller_hand)
        if diller_result >= 21:
            not_end = False
        elif diller_result >= player_result:
            not_end = False
    return diller_result

def print_status(player_hand, player_result, diller_hand, diller_result):
    print(f'Your hand: {player_hand} - Current score: {player_result}')
    print(f'Diller hand: {diller_hand} - Current score: {diller_result}')
    
def play_game():
    """
    Main loop for the game. 
    Creating all moves for player and diller
    Handelling the outcomes and the flow
    """
    player_hand = []
    diller_hand = []
    player_hand, diller_hand = init_players_hands(player_hand, diller_hand)
    player_result = check_total_sum(player_hand)
    diller_result = check_total_sum(diller_hand)
    print_status(player_hand, player_result, diller_hand, diller_result)
    player_result = play_player_hand(player_hand,player_result)

    if player_result == 21:
        print("You Win!!!")
        return
    if player_result > 21:
        return
    else:
        diller_result = play_diller_hand(diller_hand,player_result)
        print_status(player_hand, player_result, diller_hand, diller_result)
            
        if diller_result > 21:
            print('You Win!!!')
        elif diller_result > player_result:
            print('You Lost!!!')
        elif diller_result < player_result:
            print('You Win!!!')
        elif diller_result == player_result:
            print("It's a draw!!!")
        
if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        play_game()
    print('Game Over!!')
        
