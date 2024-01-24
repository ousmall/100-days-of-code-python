from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip  # copy and paste module


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    # use join() to combine all the characters, but it must need a separator
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()

    # check if the inputs are empty or not
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message=f"website and email are required!")
    else:
        # before save the file, ask users to make a confirmation
        save = messagebox.askokcancel(title="confirmation", message=f"Website:{website} \n"
                                                                    f"Email:{email} \n"
                                                                    f"Password:{password} \n"
                                                                    f"Please confirm and save")

        if save:
            with open("password.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                web_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Todo 1: set up window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Todo 2: set up canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Todo 3: setup label
web_label = Label(text="Website:")
web_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# Todo 4: setup entry(input)
web_input = Entry(width=36)
web_input.grid(column=2, row=2, columnspan=2)
web_input.focus()

email_input = Entry(width=36)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "smallouforme@gmail.com")
# use insert() to embed values in text input, and 0 means initial, END means ultimate

password_input = Entry(width=27)
password_input.grid(column=2, row=4)

# Todo 5: setup button
generate_button = Button(text="Generate", command=generate)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add To File", width=35, command=save_data)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
