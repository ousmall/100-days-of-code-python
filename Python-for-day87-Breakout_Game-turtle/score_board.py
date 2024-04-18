from turtle import Turtle

FONT = ("Courier", 16, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.setpos(0, 300)
        self.speed(0)
        self.score = 0
        try:
            with open('highest_score.text') as f:
                self.highest_score = int(f.read())
        except FileNotFoundError:
            self.highest_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Highest Score:{self.highest_score}        Score:{self.score}", align=ALIGN, font=FONT)

    def current_score(self, points):
        self.score += points
        self.update_score()

    def score_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.text", "w") as f:
                f.write(f"{self.highest_score}")
            self.score = 0
            self.update_score()