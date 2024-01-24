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


def play_game():

    # turtle control
    screen.listen()
    screen.onkey(turtle.move, "Up")
    screen.onkey(turtle.turn_left, "Left")
    screen.onkey(turtle.turn_right, "Right")

    # start to move
    time.sleep(0.05)
    screen.update()
    car.move_cars()

    if turtle.at_the_goal():
        score.get_score()
        car.increase_speed()
        turtle.restart()


title_text = "Turtle is crossing"
prompt_text = "Enter 'Go' to play"

# start the game
game_started = False
while not game_started:
    answer = screen.textinput(title_text, prompt_text)

    if answer and answer.lower() == "go":
        game_started = True

while game_started:
    play_game()

    for each_car in car.cars:
        if turtle.distance(each_car) < 20:
            answer = screen.textinput(title_text, "Enter 'Y' to restart or 'N' to exit")
            if answer and answer.lower() == 'y':
                turtle.restart()
            else:
                game_started = False

score.game_over()

screen.exitonclick()
