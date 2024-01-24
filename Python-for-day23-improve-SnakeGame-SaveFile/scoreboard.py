from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')


# the update part
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 300)
        self.color("white")
        with open("data.text") as data_score:
            self.highest_score = int(data_score.read())
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}   Highest Score:{self.highest_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.text", mode="w") as data_score:
                data_score.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def score_count(self):
        self.score += 1
        self.update_score()
