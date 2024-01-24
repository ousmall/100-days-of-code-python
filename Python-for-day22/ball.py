from turtle import Turtle
import random
ANGLE = (45, 135, 225, 315)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.wait_speed = 0.01
        self.penup()
        self.set_initial_direction() 
        
    def set_initial_direction(self):
        initial_angle = random.choice(ANGLE)
        self.setheading(initial_angle)

    def move(self):
        self.forward(20)

    def paddle_bounce(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)
        self.wait_speed *= 0.9

    def wall_bounce(self):
        current_heading = self.heading()
        self.setheading(-current_heading)

    def reset(self):
        self.home()
        self.wait_speed = 0.01
        self.set_initial_direction()
