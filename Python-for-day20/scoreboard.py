from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 300)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def score_count(self):
        self.clear()
        self.score += 1
        self.update_score()


