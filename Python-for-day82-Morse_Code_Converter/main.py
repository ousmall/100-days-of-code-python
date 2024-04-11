from tkinter import *
from tkinter.ttk import Combobox
import ttkbootstrap as ttk
from tkinter import messagebox


# crete a morse dictionary:
def get_morse():
    with open('morse_code.txt') as f:
        morse_data = {line.split(" ")[0]: line.split(" ")[1].strip("\n") for line in f.readlines()}
    return morse_data


# get text from input box
def get_text():
    text = text_input.get().upper()
    if len(text) == 0:
        messagebox.showwarning(title="Warning", message=f"Input is required!")
    return text


def interpretation():
    morse_code = get_morse()
    content = get_text()
    translate_text = ""
    if selected_option.get() == "Encrypt":
        for char in content:
            if char in morse_code:
                translate_text += morse_code[char] + " "

# convert morse code to text, we need to separate them by " ", each unit as a char
    if selected_option.get() == "Decrypt":
        char_units = content.split(" ")
        for unit in char_units:
            if unit in morse_code.values():
                for key, value in morse_code.items():
                    if value == unit:
                        translate_text += key
            else:
                messagebox.showwarning(title="Caution", message=f"Invalid input!")
    text_input.delete(0, END)
    outcome_text_box.delete(0, END)
    outcome_text_box.insert(0, translate_text.strip())


# UI setup

root = ttk.Window()
style = ttk.Style("pulse")
root.title("Morse Code Converter")
root.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300)
logo_img = PhotoImage(file="morse-code.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(column=2, row=1)


text_label = Label(text="Enter your context:")
text_label.grid(column=1, row=2)
text_input = Entry(width=20)
text_input.grid(column=2, row=2)
text_input.focus()

selected_option = StringVar(root)
options = ["Encrypt", "Decrypt"]
option_menu = Combobox(root, textvariable=selected_option,
                       values=options, state="readonly", width=10)
option_menu.grid(column=3, row=2)
selected_option.set('Select')

outcome_label = Label(text="Consequence:")
outcome_label.grid(column=1, row=4)
outcome_text_box = Entry(width=20)
outcome_text_box.grid(column=2, row=4)
outcome_label.config(pady=20)

button = ttk.Button(root, text="Generate", command=interpretation)
button.grid(column=3, row=4)

root.mainloop()