year = int(input("Please type the year you want to know if it is a leap year:\n"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
     print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
