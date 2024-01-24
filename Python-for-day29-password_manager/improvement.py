from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get().lower()
    email = email_input.get().lower()
    password = password_input.get().lower()

    # new learning about JSON, a kind of tool to restore data
    new_json = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message=f"website and email are required!")
    else:
        save = messagebox.askokcancel(title="confirmation", message=f"Website:{website} \n"
                                                                    f"Email:{email} \n"
                                                                    f"Password:{password} \n"
                                                                    f"Please confirm and save")

        if save:
            # read the old data, if not, create it
            try:
                with open("password.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            # update should be in the same line with the main codes
            data.update(new_json)

            # saving update data
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)

                web_input.delete(0, END)
                password_input.delete(0, END)

            '''老师的代码：
            try:
                with open("password.json", "r") as file:
                    data = json.load(file)
            
            except FileNotFoundError:
                 with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            
            else:
                data.update(new_json)
                with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
            
            finally:
                web_input.delete(0, END)
                password_input.delete(0, END)
            '''


# ---------------------------- SEARCH DATA ------------------------------- #
def search():

    website_reach = web_input.get().lower()

    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    # change the mode in read and load the data from json document, and the type of data is dict
        if len(website_reach) == 0:
            messagebox.showwarning(title="Oops", message=f"website is required!")
        else:
            if website_reach in data:
                search_data = data[website_reach]  # delete
                email = search_data.get("email")  # email = data[website_reach]["email"]
                password = search_data.get("password")  # password = data[website_reach]["password"]
                messagebox.showinfo(title="Information", message=f"Website:{website_reach} \n"
                                                                 f"Email:{email} \n"
                                                                 f"Password:{password}")
            else:
                messagebox.showwarning(title="Error", message=f"None details "
                                                              f"for '{website_reach}' exists!")

    except FileNotFoundError:
        messagebox.showwarning(title="Caution", message=f"No Data File Found!")


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
web_input = Entry(width=27)
web_input.grid(column=2, row=2)
web_input.focus()

email_input = Entry(width=36)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "smallouforme@gmail.com")

password_input = Entry(width=27)
password_input.grid(column=2, row=4)

# Todo 5: setup button
generate_button = Button(text="Generate", command=generate)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add To File", width=35, command=save_data)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=3, row=2)

window.mainloop()
