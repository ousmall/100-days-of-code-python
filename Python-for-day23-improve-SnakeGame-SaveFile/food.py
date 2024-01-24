from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-300, 300)
        ran_y = random.randint(-300, 250)
        self.goto(ran_x, ran_y)