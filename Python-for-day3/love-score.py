print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") 
name2 = input("What is your spouse's name?\n") 

combine_name = name1 + name2
lower_name = combine_name.lower()

t = lower_name.count("t")
u = lower_name.count("u")
r = lower_name.count("r")
e = lower_name.count("e")
first_number = t + u + r + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_number = l + o + v + e

total = str(first_number)+ str(second_number)
love_socre = int(total)

if love_socre < 10 or love_socre > 90:
 print(f"Your score is {love_socre}, you go together like coke and mentos.")
elif love_socre <= 50 and love_socre >= 40:
 print(f"Your score is {love_socre}, you are alright together.")
else:
 print(f"Your score is {love_socre}.")
