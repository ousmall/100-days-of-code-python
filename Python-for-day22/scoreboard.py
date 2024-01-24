from turtle import Turtle

FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """renew the scoreboard"""
        self.clear()
        self.goto(-200, 250)
        self.write(f"Play1: {self.l_score}", align="center", font=FONT)
        self.goto(200, 250)
        self.write(f"Play2: {self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.home()
        if self.l_score > self.r_score:
            self.write("player 1 win the game", align="center", font=FONT)
        else:
            self.write("player 2 win the game", align="center", font=FONT)
