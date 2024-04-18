from turtle import Turtle

block_height = 20
block_width = 50
block_space = 5
block_colors = ["red", "orange", "yellow", "green"]
block_rows = 8


class Block(Turtle):
    def __init__(self, color, start_x, start_y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(start_x, start_y)


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.rows = block_rows
        self.width = block_width
        self.height = block_height
        self.space = block_space
        self.colors = block_colors

    def create_blocks(self):
        start_y = 250
        for row in range(self.rows):
            color_index = row // 2
            color = self.colors[color_index]
            for col in range(-250, 300, self.width):
                block = Block(color, col, start_y - (row * (self.height + self.space)))
                self.blocks.append(block)
