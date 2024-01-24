from black_jack_logo import logo
import random
import os


def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # A = 11
    selected_card = random.choice(cards)
    cards.remove(selected_card)
    return selected_card       


def calculate_point(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

 
def deal_process():
    user_cards = []
    computer_cards = []
    
    for _ in range(2): 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    deal_over = False
    while not deal_over:
        user_point = calculate_point(user_cards)
        com_point = calculate_point(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_point}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_point == 0 or com_point == 0 or user_point > 21:
            deal_over = True
        else: 
            user_round = input("Please type 'y' to get another card or type 'n' to pass:\n")
            if user_round == 'y':
                user_cards.append(deal_card())
                user_point = calculate_point(user_cards)
            elif user_round == 'n':
                deal_over = True
            else:
                print("You gave an invaild command, please try again.")

        while com_point != 0 and com_point < 17:
            computer_cards.append(deal_card())
            com_point = calculate_point(computer_cards)
    return user_cards, user_point, computer_cards, com_point

      
def compare(user_point,com_point):
    if user_point == com_point:
        return "Tie 🙃"
    elif user_point == 0:
        return "Win with a Blackjack 😎"
    elif com_point == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_point > 21:
        return "You went over. You lose 😭"
    elif com_point > 21:
        return "Opponent went over. You win 😁"
    elif user_point > com_point:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
        
    user_cards, user_point, computer_cards, com_point = deal_process()
    #multiple assignment

    print(f"Your final hand: {user_cards}, final score: {user_point}")
    print(f"Computer's final hand: {computer_cards}, final score: {com_point}")
    print(compare(user_point, com_point)) 

print(logo)    
while input("Do you want to play the Blackjack? Type 'y' or 'n': \n") == "y":
    os.system('cls')
    play_game()
