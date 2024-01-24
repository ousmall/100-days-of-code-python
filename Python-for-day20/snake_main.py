from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
game_start = screen.textinput(title="Greedy Snake Game",
                              prompt="Please type 'Y' to start:")
screen.tracer(0)
scoreboard = Scoreboard()

# TODO:1 create a snake body,including 3 individual blocks
snake = Snake()  # call the class Snake and then create(initial)

# TODO:3 create the food
food = Food()

# TODO:2 Move the snake, they should move one by one and replace the previous one
screen.listen()
screen.onkey(snake.up, "Up")  # capitalize the first letter when using keyboard
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

if game_start:
    game_is_on = True

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()

    # TODO:4 detect collision with food (*It should be in the while loop  *food module)
    # TODO:5 create a scoreboard(*scoreboard module)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()  # when the head eat the food, it extends
        scoreboard.score_count()

    # TODO:6 detect collision with wall
    if snake.head.xcor() < -340 or snake.head.xcor() > 340 or snake.head.ycor() < -350 or snake.head.ycor() > 300:
        game_is_on = False
        scoreboard.game_over()

    # TODO:7 detect collision with tail
    for segment in snake.segments[1:]:  # using the slicing method to cut it off
        # if segment == snake.head: # ignore the first one
        #    pass
        if snake.head.distance(segment) < 10:  # detect the distance of head to every segment
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
