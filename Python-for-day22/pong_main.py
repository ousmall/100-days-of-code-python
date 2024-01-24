# TODO:1 create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from mid_line import Midline
import time

WIDTH = 800
HEIGHT = 600

x_range = int(WIDTH / 2) - 55
y_range = int(HEIGHT / 2) - 20

game_screen = Screen()
game_screen.setup(WIDTH, HEIGHT)
game_screen.bgcolor("black")
game_screen.title("Pong Game")
# game_screen.textinput(title="Pong Game", prompt="Enter 'Y' to get started")
game_screen.tracer(0)

# TODO:2 create paddle * 2 and ball

paddle_right = Paddle((380, 0))  # use the constant to replace position in class
paddle_left = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()
mid_line = Midline()


# TODO:3 move the paddles
game_screen.listen()
game_screen.onkey(paddle_right.up, "Up")
game_screen.onkey(paddle_right.down, "Down")
game_screen.onkey(paddle_left.up, "W")
game_screen.onkey(paddle_left.down, "S")

# TODO:4 move a ball

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(ball.wait_speed)
    mid_line.draw_line()
    ball.move()

    # TODO:5 detect the collision with wall and bounce
    if ball.ycor() > y_range or ball.ycor() < -y_range:
        ball.wall_bounce()

    # TODO:6 detect the collision with paddle and bounce
    if (ball.distance(paddle_right) < 50 and ball.xcor() < x_range + 20) or \
            (ball.distance(paddle_left) < 50 and ball.xcor() > -x_range - 20):
        ball.paddle_bounce()
    # distance is count between the center of two objects,
    # so we should consider the top and the button of the paddle

    # TODO:7 detect when paddle misses
    # right miss, and left score
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    # left miss, and right score
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False

scoreboard.game_over()
# TODO:8 keep score
game_screen.exitonclick()
