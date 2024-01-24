from turtle import Turtle


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def draw_line(self):
        self.teleport(400, -250)
        self.setheading(180)
        self.pencolor("white")
        self.pendown()
        self.forward(800)

        for y in range(-150, 151, 100):
            self.teleport(400, y)
            for _ in range(30):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)

        self.teleport(400, 250)
        self.setheading(180)
        self.pendown()
        self.forward(800)
