from turtle import Turtle


class Midline(Turtle):
    def __init__(self):
        super().__init__()

    def draw_line(self):
        self.setpos(0, 300)
        self.setheading(270)
        self.pencolor("white")
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)