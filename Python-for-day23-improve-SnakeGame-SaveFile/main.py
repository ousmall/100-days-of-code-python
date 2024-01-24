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
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up") 
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

    if snake.head.distance(food) < 15:  
        food.refresh()
        snake.extend() 
        scoreboard.score_count()

    if snake.head.xcor() < -340 or snake.head.xcor() > 340 or snake.head.ycor() < -350 or snake.head.ycor() > 300:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]: 
        if snake.head.distance(segment) < 10: 
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
