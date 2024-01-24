print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n").lower()
bill = 0

if size == "s":
 bill += 15
if size == "m":
  bill += 20
if size == "l":
  bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()

if add_pepperoni == "y":
  if size == "s":
    bill +=2
  else:
    bill +=3
  
extra_cheese = input("Do you want extra cheese? Y or N\n").lower() 
   
if extra_cheese == "y":
  bill +=1
 
print(f"Your final bill is: ${bill}.")