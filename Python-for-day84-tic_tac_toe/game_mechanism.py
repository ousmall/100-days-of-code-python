import json


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.score = {'X': 0, 'O': 0}

    def print_board(self):
        """ print the current situation of game board """
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # This method does not need to access any instance variables, so it can be a static method.
    # If we want to change the methods to a static method,
    # we can use the @staticmethod decorator.
    @staticmethod
    def print_board_nums():
        """ print the board No. like this
        |1|2|3|
        |4|5|6|
        |7|8|9|"""
        board_number = [[str(i) for i in range(j * 3 + 1, (j + 1) * 3 + 1)] for j in range(3)]
        for num in board_number:
            print('| ' + ' | '.join(num) + ' |')

    def available_moves(self):
        """ show the current index of empty grid """
        return [index + 1 for index, value in enumerate(self.board) if value == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        """ Make a move on the game board """
        square -= 1
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):

        # According to the current position of the move,
        # locate the row, column and diagonal of the position.
        row_ind = (square - 1) // 3   # I start from 1, so I need to subtract 1
        col_ind = square % 3

        # Check if the rows are the same
        if self.board[row_ind * 3] == self.board[row_ind * 3 + 1] == self.board[row_ind * 3 + 2] == letter:
            return True

        # Check if the columns are the same
        if self.board[col_ind] == self.board[col_ind + 3] == self.board[col_ind + 6] == letter:
            print("Vertical win!")
            return True

        # Check if the left diagonal are the same
        if self.board[0] == self.board[4] == self.board[8] == letter:
            return True

        # Check if the right diagonal are the same
        if self.board[2] == self.board[4] == self.board[6] == letter:
            return True

        return False

    def update_score(self, winner):
        if winner == 'X' or winner == 'O':
            self.score[winner] += 1

    def save_score(self, game_score):
        with open(game_score, 'w') as file:
            json.dump(self.score, file)

    def load_score(self, game_score):
        try:
            with open(game_score, 'r') as file:
                self.score = json.load(file)
        except FileNotFoundError:
            print("Score file not found.")

    def reset_score(self):
        self.score = {'X': 0, 'O': 0}

    def reset_board(self):
        """ Reset the game board to initial state """
        self.board = [' ' for _ in range(9)]
        self.current_winner = None