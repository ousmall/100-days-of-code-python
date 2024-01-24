from game_logo import logo
import random
import os


def number():
    return random.randint(1, 100)


def difficulty(choose_level):
    attempts = 0    
    if choose_level == "easy":
        attempts += 10
    if choose_level == "hard":
        attempts += 5
    return attempts


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    choose_level = input("Choose a difficulty, Type 'easy' or 'hard': \n")
    if choose_level != "easy" and "hard":
        print("Invoid indication, please try again! ")
        play_game()        
    game_is_end = False
    serect_num = number()
    attempts_left = difficulty(choose_level)
        
    while not game_is_end and attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number. ")
        guess_number = int(input("Make a guess: "))
        if guess_number != serect_num:
            if guess_number > serect_num:
                print("Too high.\nGuess again.")
            else: 
                print("Too low.\nGuess again.")
            attempts_left -= 1
            
        else:
            print(f"Congratulations! You've guessed the correct number: {serect_num}")
            game_is_end = True
    if attempts_left == 0:
        print(f"The correct number is {serect_num} ")
        game_is_end = True

play_game() 

while input("Do you want to play again?'Y' or 'N'").lower() == "y":
   os.system("cls")
   play_game() 
