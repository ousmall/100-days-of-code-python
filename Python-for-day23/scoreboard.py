from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        """renew the scoreboard"""
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def get_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)