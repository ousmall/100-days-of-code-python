names = input("Please offer the names as participants,split by 'space button':\n").split()

import random
num_items = len(names)

random_name = random.randint(0,num_items - 1)

final_choice = names[random_name]
print(final_choice + " is going to buy the meal today!")
