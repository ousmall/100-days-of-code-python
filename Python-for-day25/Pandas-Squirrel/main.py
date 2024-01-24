# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # csv.reader can separate each data
#     temperatures = []
#     for each_data in data:
#         if each_data[1] != "temp":  # exclude the title "temp"
#             temperatures.append(int(each_data[1]))
#     print(temperatures)


import pandas  # pandas library to solve the data issue

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()  #  or .to_dict to become a dictionary
# data_num = len(temp_list)
# sum_temp = sum(temp_list)
# average_temp = round((sum_temp/data_num), 2)

# average_temp = round(data["temp"].mean(), 2)  # series.mean() count the average
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# # writing: data.condition = data.condition
#
# print(data[data.temp == data.temp.max()])  # the satisfactory condition in the square bracket
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]  # without the sequence, it will contain the sequence number
# print(monday_temp)

# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv(("new_data.csv"))

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
color_analyze = color.value_counts()

color_count = pandas.DataFrame(color_analyze)
color_count.to_csv("Squirrel_fur_color.csv")
