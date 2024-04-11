import logo
from player import HumanPlayer, RandomComputerPlayer
from game_mechanism import TicTacToe
import time
import os


def play_game(game, player_x, player_o):
    score_file = 'score.json'
    if os.path.exists(score_file):
        try:
            game.load_score(score_file)
            load_score = input("Do you want to load previous score? (yes/no): ").lower()
            if load_score == 'yes':
                game.load_score(score_file)
                print("Current Score - X: {}, O: {}".format(game.score['X'], game.score['O']))
        except FileNotFoundError:
            print("Score file not found.")

    time.sleep(1)

    while True:
        game.reset_board()
        game_is_on = True

        if game_is_on:
            print(logo.logo)
            game.print_board_nums()

        letter = 'X'
        while game.empty_squares() and game.current_winner is None:
            square = player_o.get_move(game) if letter == 'O' else player_x.get_move(game)
            if game.make_move(square, letter):
                if game_is_on:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('')

                if game.current_winner is not None:
                    if game_is_on:
                        print(game.current_winner + ' wins!')
                        game.update_score(game.current_winner)
                        print("Current Score - X: {}, O: {}".format(game.score['X'], game.score['O']))

                        save_or_reset = input("Do you want to save score or not? (yes/no): ").lower()
                        if save_or_reset == 'yes':
                            game.save_score('score.json')
                        elif save_or_reset == 'no':
                            game.reset_score()

                    break
                letter = 'O' if letter == 'X' else 'X'

            time.sleep(0.8)

        if game.current_winner is None:
            print('It is a tie!')

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
        else:
            print("Let's play again!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play_game(t, x_player, o_player)
