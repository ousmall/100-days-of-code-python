import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

# set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")

# set objects
turtle = Player()
car = CarManager()
road = Road()
road.draw_line()
score = Scoreboard()

# turtle control
screen.listen()
screen.onkey(turtle.move, "Up")
screen.onkey(turtle.turn_left, "Left")
screen.onkey(turtle.turn_right, "Right")


# start the game
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car.move_cars()

    if turtle.at_the_goal():
        score.get_score()
        car.increase_speed()
        turtle.restart()

    for each_car in car.cars:
        if turtle.distance(each_car) < 20:
            game_is_on = False
score.game_over()


screen.exitonclick()