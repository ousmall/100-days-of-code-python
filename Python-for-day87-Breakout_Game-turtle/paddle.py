from turtle import Turtle

POSITION = (0, -300)


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setpos(POSITION)

    def move_right(self):
        x_move = self.xcor()
        if x_move < 340:
            self.setx(x_move + 20)

    def move_left(self):
        x_move = self.xcor()
        if x_move > -340:
            self.setx(x_move - 20)