from flask import Flask
import random

guess_web = Flask(__name__)

num_choice = random.randint(0, 9)


@guess_web.route("/")
def game_start():
    return ("<div style='text-align: center;'>"
            "<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/4QaQ4tA0OUwkkrnG9Z/giphy.gif?cid"
            "=790b7611elnknyhzu587z3ewwar4ijm2fxuda0ek2zgtqr34&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
            "</div>")


@guess_web.route("/<int:num>")
def guess(num):
    if num > 9 or num < 1:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: red;'>OUT OF RANGE</h1>"
                "<img src='https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif?cid"
                "=790b7611d3h2qqytl4ormrmeuxxgra9s4g7hlvewco1y7mqa&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                "</div>")
    elif num < num_choice:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: green;'>TOO LOW, TRY AGAIN!</h1>"
                "<img src='https://media.giphy.com/media/CilAbpLI2APlV4UdYX/giphy.gif?cid"
                "=ecf05e470b8gqz6mu5rrlqbcergepsp8zf5c8d22dgjh2wu7&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                "</div>")
    elif num > num_choice:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: blue;'>TOO HIGH, TRY AGAIN!</h1>"
                "<img src='https://media.giphy.com/media/3o8doVAxrMjXbIHaU0/giphy.gif?cid"
                "=ecf05e4737y2a07k9t4uuyffkks642zll6wfisttcw7vw89s&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                "</div>")
    else:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: pink;'>YOU GUESS IT RIGHT, CONGRATS!</h1>"
                "<img src='https://media.giphy.com/media/18smLWpYdamGY/giphy.gif?cid"
                "=ecf05e474ugtzk6mlnx35pa223w35c4odr31s3d6g7v8dvvb&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
                "</div>")


if __name__ == "__main__":
    guess_web.run(debug=True)