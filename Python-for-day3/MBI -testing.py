weight = int(input("What is your weight?,please type by kilogram.\n"))
height = float(input("What is your height?,please type by meter.\n"))
BMI = float("{:.2f}".format(weight/height**2))


if BMI < 18.5:
  print("Your BMI is " + str(BMI) + ", you are underweight.")
elif BMI < 25:
  print("Your BMI is " + str(BMI) + ", you have a normal weight.")
elif BMI < 30:
  print("Your BMI is " + str(BMI) + ", you are slightly overweight.")
elif BMI < 35:
  print("Your BMI is " + str(BMI) + ", you are obese.")
else:
  print("Your BMI is " + str(BMI) + ", you are clinically obese.")
