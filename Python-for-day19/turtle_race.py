from turtle import Turtle, Screen
import random

is_on = False
t_screen = Screen()
t_screen.setup(width=500, height=500) 
turtle_race = t_screen.textinput(title="Make your bet!",
                                 prompt="Who will win? "
                                        "Bring your option(red/blue/yellow/"
                                        "green/orange/pink):")
y_pos = [-150, -100, -50, 0, 50, 100]
new_color = []
colors = ["red", "blue", "yellow", "green", "orange", "pink"]
random.shuffle(colors)
new_color.extend(colors)


all_turtle = []
for turtle_pos in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(new_color[turtle_pos])
    t.penup()
    t.goto(x=-230, y=y_pos[turtle_pos])
    all_turtle.append(t)


if turtle_race:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 216:
            is_on = False
            winning_color = turtle.fillcolor()
            if winning_color == turtle_race:
                print(f"You win! The {winning_color} turtle win the race!")
            else:
                print(f"You lose! The {winning_color} turtle win the race!")
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)


t_screen.exitonclick()
