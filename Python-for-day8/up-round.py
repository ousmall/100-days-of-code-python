import math
# learn from ChatGPT

def paint_calc(height , width , cover):
  number_of_cans = (height * width) / cover 
  total = math.ceil(number_of_cans)
  print(f"You'll need {total} cans of paint.")
  
test_h = int(input("What is the height of your room?\n")) 
test_w = int(input("What is the width of your room?\n")) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
