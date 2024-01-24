from HL_logo import logo, vs
from VS_list import data
import random
import os

print(logo)
print("Welcome to the higher vs lower gamble world!")


def message_choose():
    message = random.choice(data)
    return message

def format_data(message):
    name = message["name"]
    description = message["description"]
    country = message["country"]
    return f"{name}, a {description}, from {country}"

def answer_check(user_choice, a_follower, b_follower):
    if a_follower > b_follower:
        return user_choice == "a"
    else:
        return user_choice == "b"
    

def play_game():
    message_A = message_choose()
    message_B = message_choose()
    score = 0   
    end_game = False
    while not end_game:
        message_A = message_B
        message_B = message_choose()
    
        while message_A == message_B:
            message_B = message_choose()

        print(f"Compare A: {format_data(message_A)}.")
        print(vs)
        print(f"Against B: {format_data(message_B)}.")
         
        user_choice = input("Who has more follower? Type 'A' or 'B':\n").lower()
        a_follower = message_A["follower_count"]
        b_follower = message_B["follower_count"]
        correct = answer_check(user_choice, a_follower, b_follower)
        
        os.system('cls')
        print(logo)
        if correct:
            score += 1
            print(f"You are right. Current score: {score}.")
        else:
            end_game = True
            print(f"Sorry, you are wrong. Final score: {score} ")
        
play_game()
