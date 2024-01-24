target = int(input("Please give the final number:\n")) 
final_number = 0
for number in range(2, target + 1, 2):
    final_number += number
if target > 1000:
    print("The number should be least than 1000.")

print(f"The total addition is: {final_number}")
