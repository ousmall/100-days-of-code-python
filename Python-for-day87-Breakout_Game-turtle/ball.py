from turtle import Turtle
import random

ANGLE = (45, 135)
BALL_ORIGIN = (0, -250)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setpos(BALL_ORIGIN)
        self.initial_direction()
        self.hideturtle()

    def initial_direction(self):
        initial_angle = random.choice(ANGLE)
        self.setheading(initial_angle)

    def move(self):
        self.showturtle()
        self.forward(20)

    def x_bounce(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def y_bounce(self):
        current_heading = self.heading()
        self.setheading(- current_heading)

    def reset(self):
        self.hideturtle()
        self.goto(BALL_ORIGIN)
        self.initial_direction()
        self.move()