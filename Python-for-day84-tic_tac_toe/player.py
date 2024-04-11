import random


class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        move = None
        while not valid_square:
            square = input(self.letter + " Your turn, please choose your move (1-9): ")
            try:
                move = int(square)
                if move not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid input, please try again.")
        return move


class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move
