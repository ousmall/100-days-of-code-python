from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 250


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def turn_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def turn_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def at_the_goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def restart(self):
        self.setpos(STARTING_POSITION)






