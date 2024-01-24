print("Welcome to the tip calculator!")

money = float(input("What was the total bill?\n $"))
tip = float(input("How much tip would you like to give?\n 10,12, or 15\n"))
people_number = int(input("How many people to split the bill?\n"))
bill = round((money * (tip / 100) + money) / people_number)

bill = "{:.2f}".format((money * (tip / 100) + money) / people_number)

print(f"Each person should pay:\n ${bill}")
