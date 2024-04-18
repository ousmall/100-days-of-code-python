from turtle import Screen
from blocks import BlockManager
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

FONT = ("Courier", 26, "normal")

# setup screen
game_screen = Screen()
game_screen.title("Breakout Game")
game_screen.bgcolor("black")
game_screen.setup(width=800, height=700)
game_screen.tracer(0)

# setup objects
block_manager = BlockManager()
block_manager.create_blocks()

paddle = Paddle()
ball = Ball()
score_board = Scoreboard()

# bind keyboard
game_screen.listen()
game_screen.onkeypress(paddle.move_right, "Right")
game_screen.onkeypress(paddle.move_left, "Left")


# main loop
def play_game():
    while True:
        game_screen.update()
        ball.move()

        # check collision between ball and paddle
        if ball.distance(paddle) < 20 and ball.ycor() < -280:
            ball.y_bounce()

        # check collision between ball and wall
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.x_bounce()

        if ball.ycor() > 340:
            ball.y_bounce()

        if ball.ycor() < -350:
            ball.reset()
            score_board.score_reset()

        # check collision between ball and blocks
        for each_block in block_manager.blocks:
            ball_dx = abs(ball.xcor() - each_block.xcor())
            ball_dy = abs(ball.ycor() - each_block.ycor())

            if ball_dx < 20 and ball_dy < 20:
                if ball_dx < ball_dy:
                    ball.x_bounce()
                else:
                    ball.y_bounce()

                each_block.goto(1000, 1000)
                each_block.clear()

                if each_block.color()[0] == "red":
                    score_board.current_score(4)
                elif each_block.color()[0] == "orange":
                    score_board.current_score(3)
                elif each_block.color()[0] == "yellow":
                    score_board.current_score(2)
                elif each_block.color()[0] == "green":
                    score_board.current_score(1)

                score_board.update_score()

        game_screen.update()

        # Check if all blocks are cleared
        if len(block_manager.blocks) == 0:
            game_screen.clear()
            score_board.update_score()
            score_board.goto(0, 0)
            score_board.write("You Win!", align="center", font=FONT)
            break

        game_screen.ontimer(play_game, 10)  # Run main_loop again after 10 milliseconds


# Run the main loop
play_game()
game_screen.mainloop()
