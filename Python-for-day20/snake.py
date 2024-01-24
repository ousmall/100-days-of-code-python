from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # the first block

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segment.speed(3)
        self.segments.append(segment)

    def extend(self):
        self.add_snake(self.segments[-1].position())  # call the position method

    def move(self):
        """when the very first one moving, the others should follow it"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """when moving up, it can't move down"""
        if self.head.heading() != DOWN:  #
            self.head.setheading(UP)

    def down(self):
        """when moving down, it can't move up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """when moving left, it can't move right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """when moving right, it can't move left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
