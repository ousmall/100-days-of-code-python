student_heights = input("please type the students height in 'cm',split by 'space button': \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for each_height in student_heights:
  total_height += each_height

average_height = "{:.0f}".format(total_height/(n+1)) 
print(f"total height = {total_height}")
print(f"number of students = {n+1}")
print(f"average height = {average_height}")
