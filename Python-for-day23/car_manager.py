from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.start_line = int(SCREEN_WIDTH / 2 + 20)
        self.road_y_up = int(SCREEN_HEIGHT / 2 - 50)
        self.road_y_down = int(-SCREEN_HEIGHT / 2 + 60)

    def create_car(self):
        car = Turtle("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(self.start_line, random.choice(range(self.road_y_down, self.road_y_up)))
        self.cars.append(car)

    def move_cars(self):
        if not random.randint(0, 5):
            self.create_car()
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
