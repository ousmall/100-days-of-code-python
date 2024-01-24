rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n")
if option == "0":
    print(rock)
if option == "1":
    print(paper)
if option == "2":
    print(scissors)
else:
 print("you gave the wrong input, try again!\n")
 
import random
print("The computer chose:")
computer_option = random.randint(0, 2)
if computer_option == 0:
    print(rock)
elif computer_option == 1:
    print(paper)
else:
    print(scissors)

if option == "0" and computer_option == 0 or option == "1" and computer_option == 1 or option == "2" and computer_option == 2:
    print("tied")
if option == "0" and computer_option == 1 or option == "1" and computer_option == 2 or option == "2" and computer_option == 0:
    print("you lose")
if option == "0" and computer_option == 2 or option == "1" and computer_option == 0 or option == "2" and computer_option == 1:
    print("you win")