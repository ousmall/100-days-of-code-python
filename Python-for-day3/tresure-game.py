print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

c1=input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if c1 == "left":
 c2=input("You are at a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
 
 if c2 == "wait":
  c3=input("You arrived at the island and you faced three door in front of you, yello,red and blue. Which colour do you choose? Type 'yellow' or 'red' or 'blue'\n").lower()
  
  if c3 =="yellow":
   print("You got the treasure!")
   print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
  elif c3 == "red":
   print("You got eaten by a shark!,Game Over!")
  else:
   print("You fell into a hole and died!,Game Over!")
 
 else:
  print("You are drowning and died.Game Over!")

else:
 print("You are lose in the forest.Game Over!")
