# project Nutritionix

import requests as rs
from datetime import datetime

# Parts of Nutritionix

# private information
MY_WEIGHT = "secrete"
MY_HEIGHT = "secrete"
AGE = "secrete"

# Nutritionix setting
MY_ID = "secrete"
MY_API = "secrete"
Host_domain = "https://trackapi.nutritionix.com"

# natural language
nutrient_endpoint = "/v2/natural/nutrients"
exercise_endpoint = "/v2/natural/exercise"

my_exercise = input("What exercise you did today?\n")

n_params = {
    "query": my_exercise,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": AGE
}

n_headers = {
    "x-app-id": MY_ID,
    "x-app-key": MY_API
}

n_response = rs.post(url=f"{Host_domain}{exercise_endpoint}",
                     headers=n_headers, json=n_params)
n_data = n_response.json()


# Parts of Sheet

MAIN_ENDPOINT = "https://api.sheety.co/"
SHEET_API = "secrete"
project = "nutritionProject"
sheet_name = "sheet1"
object_ID = "num"  # row 1 or 2 or something like that
TOKEN = "secrete"

get_post_endpoint = f"{MAIN_ENDPOINT}{SHEET_API}/{project}/{sheet_name}"
put_delete_endpoint = f"{MAIN_ENDPOINT}{SHEET_API}/{project}/{sheet_name}/{object_ID}"

date = datetime.today().date().strftime("%d/%m/%Y")
time = datetime.today().time().strftime("%I:%M%p")
# strptime() convert str into date type

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
