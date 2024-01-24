# import colorgram

# rgb_color = []
# colors = colorgram.extract('kirby.png', 15)
# for color in colors:

#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)

import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()
t.teleport(-250, -250)
t.penup()
t.hideturtle()
color_list = [(101, 190, 171), (100, 164, 209), (207, 137, 182),
              (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211),
              (25, 26, 26), (217, 163, 85), (239, 212, 97), (189, 89, 132),
              (124, 73, 114), (160, 209, 185),
              (89, 126, 186)]

t.speed("fast")
total_dot = 100


for dot_step in range(1, total_dot + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_step % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
