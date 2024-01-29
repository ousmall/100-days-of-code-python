# project Nutritionix

import requests as rs
from datetime import datetime
from tkinter import *
from tkinter import messagebox

# UI set up

FONT = ("Times New Roman", 12, "normal")

# Parts of Nutritionix

MY_ID = "78aff6a0"
MY_API = "d9b8b563a5ba760f7fcb686ca1c6494c"
Host_domain = "https://trackapi.nutritionix.com"

# natural language
nutrient_endpoint = "/v2/natural/nutrients"
exercise_endpoint = "/v2/natural/exercise"

# Parts of Sheet
MAIN_ENDPOINT = "https://api.sheety.co/"
SHEET_API = "61ae00aac812b0b5afc6a35f9d541aed"
project = "nutritionProject"
sheet_name = "sheet1"
object_ID = "num"  # row 1 or 2 or something like that
TOKEN = "youwillbebetterthanbefore"

get_post_endpoint = f"{MAIN_ENDPOINT}{SHEET_API}/{project}/{sheet_name}"
put_delete_endpoint = f"{MAIN_ENDPOINT}{SHEET_API}/{project}/{sheet_name}/{object_ID}"

date = datetime.today().date().strftime("%d/%m/%Y")
time = datetime.today().time().strftime("%I:%M%p")


# strptime() convert str into date type


def confirm():
    my_exercise = exercise_input.get()
    my_time = time_input.get()
    weight = weight_input.get()
    height = height_input.get()
    age = age_input.get()

    if len(my_exercise) == 0 or len(my_time) == 0:
        messagebox.showwarning(title="Notification", message=f"exercise and time are required!")
    else:
        confirmed = messagebox.askokcancel(title="confirmation",
                                           message=f"Exercise:{my_exercise} \n"
                                                   f"Time:{my_time} mins \n"
                                                   f"Weight:{weight} kg\n"
                                                   f"Height:{height} cm\n"
                                                   f"Age:{age} \n\n"
                                                   f"Please confirm")
        if confirmed:
            # set Nutritionix response
            n_params = {
                "query": f"I {my_exercise} {my_time} minutes",
                "weight_kg": weight,
                "height_cm": height,
                "age": age
            }

            n_headers = {
                "x-app-id": MY_ID,
                "x-app-key": MY_API
            }

            n_response = rs.post(url=f"{Host_domain}{exercise_endpoint}",
                                 headers=n_headers, json=n_params)
            n_data = n_response.json()

            # set Sheet response
            for exercise in n_data["exercises"]:
                name = exercise["name"]
                duration = exercise["duration_min"]
                calories = exercise["nf_calories"]

                s_params = {
                    sheet_name: {
                        "date": date,
                        "time": time,
                        "exercise": name.title(),
                        "duration": duration,
                        "calories": calories
                    }
                }

                bearer_headers = {"Authorization": f"Bearer {TOKEN}"}
                s_response = rs.post(url=get_post_endpoint, headers=bearer_headers, json=s_params)
                print(s_response.text)


# UI set up

window = Tk()
window.title("Exercise Today")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=270)
logo_img = PhotoImage(file="photo.png")
canvas.create_image(150, 135, image=logo_img)
canvas.grid(column=1, row=1, columnspan=9)

exercise_label = Label(text="Exercise & Sport:", font=FONT, padx=10, pady=10)
exercise_label.grid(column=1, row=2)
exercise_input = Entry(width=55)
exercise_input.grid(column=2, row=2, columnspan=8)
exercise_input.focus()

time_label = Label(text="Time:", font=FONT, padx=10, pady=10)
time_label.grid(column=1, row=3)
time_input = Entry(width=7)
time_input.grid(column=2, row=3)
min_label = Label(text="Minutes")
min_label.grid(column=3, row=3)

weight_label = Label(text="Weight:", font=FONT, padx=10, pady=10)
weight_label.grid(column=1, row=4)
weight_input = Entry(width=7)
weight_input.grid(column=2, row=4)
kg_label = Label(text="kg")
kg_label.grid(column=3, row=4)

height_label = Label(text="Height:", font=FONT, padx=10, pady=10)
height_label.grid(column=5, row=4)
height_input = Entry(width=7)
height_input.grid(column=6, row=4)
cm_label = Label(text="cm")
cm_label.grid(column=7, row=4)

age_label = Label(text="Age:", font=FONT, padx=10, pady=10)
age_label.grid(column=8, row=4)
age_input = Entry(width=7)
age_input.grid(column=9, row=4)

confirm_button = Button(text="Confirm", font=FONT, command=confirm)
confirm_button.grid(column=4, row=5, columnspan=2)

window.mainloop()
