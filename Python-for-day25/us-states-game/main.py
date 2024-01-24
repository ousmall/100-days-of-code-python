import turtle
import pandas
WITH = 750
HEIGHT = 550


def add_state(select_state):
    answer_state = turtle.Turtle()
    answer_state.hideturtle()
    answer_state.penup()
    answer_state.goto(select_state.x.item(), select_state.y.item())
    answer_state.write(select_state.state.item())  # or simply write 'answer_state'
    # pandas .item() get the first element
    # .items() returns an iterable tuple (index, value)


screen = turtle.Screen()
screen.setup(WITH, HEIGHT)
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.goto(0, -15)

# def get_mouse_click_coor(x, y):
#     """get the X and Y coordinates"""
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
title_text = "Guess the state"
prompt_text = "What's the name of the state:"


state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
guessed_state = []
game_is_on = True

while game_is_on:
    answer = screen.textinput(title=title_text,
                              prompt=prompt_text).title()  # Make all input capitalized
    if answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)  # create a new file
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer in all_states and answer not in guessed_state:
        add_state(state_data[state_data.state == answer])
        guessed_state.append(answer)

    guessed_count = len(guessed_state)
    if guessed_count > 0:
        title_text = f"{guessed_count}/50 states correct"
        prompt_text = "Enter another state:"
    if guessed_count == 50:
        game_is_on = False
