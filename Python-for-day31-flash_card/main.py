from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
current_word = {}
word_pairs = {}

try:
    # Use pandas to read data from the CSV file
    new_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_pairs = original_data.to_dict(orient="records")
    # Convert DataFrame to a list of dictionaries, refer to:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
else:
    word_pairs = new_data.to_dict(orient="records")


# Todo 2: create new flash card
def next_word():
    global current_word, flip_time
    # when choose a word, save it in global scope and other function can use it
    window.after_cancel(flip_time)
    # the flip won't work after user stop clicking
    current_word = random.choice(word_pairs)
    canvas.itemconfig(card_bg, image=front_bg)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    flip_time = window.after(3000, flip_word)


# Todo 3: flip the card
def flip_word():
    canvas.itemconfig(card_bg, image=back_bg)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")


# Todo 4: save the progress

def have_learned():
    """remove the words have learned and save the rest of the words in a new csv"""
    word_pairs.remove(current_word)
    next_word()
    words_unknown = pandas.DataFrame(word_pairs)
    words_unknown.to_csv("data/words_to_learn.csv", index=False)
    # everytime when saving words, system will add index automatically, so remove it
    update_progress()


def update_progress():
    """update my progress"""
    progress.config(text=f"{101 - len(word_pairs)}/100")


# Todo 1: set up UI
window = Tk()
window.title("Top 100 of French Words")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(3000, flip_word)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_bg = PhotoImage(file="images/card_front.png")
back_bg = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(405, 263, image=front_bg)
canvas.grid(column=1, row=1, columnspan=2)


# create text in canvas
title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word = canvas.create_text(400, 300, text="", font=WORD_FONT)


# create buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_word)
unknown_button.grid(column=1, row=2)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=have_learned)
known_button.grid(column=2, row=2)

# create a label to show how many words have learned
progress = Label(text=f"{101-len(word_pairs)}/100", font=('Ariel', 20, 'bold'))
progress.config(bg=BACKGROUND_COLOR, fg="white", highlightthickness=0)
progress.grid(column=0, row=0)


# start to learn
next_word()


window.mainloop()
