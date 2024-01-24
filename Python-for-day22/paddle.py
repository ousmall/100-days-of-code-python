from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(position)

    # The difference from the Snake game is that it does not require changing direction
    def up(self):
        new_y = self.ycor() + 30
        if new_y <= 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        if new_y >= -250:
            self.goto(self.xcor(), new_y)
