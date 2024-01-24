import pandas  # pandas library to solve the data issue

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
color_analyze = color.value_counts()

color_count = pandas.DataFrame(color_analyze)
color_count.to_csv("Squirrel_fur_color.csv")
