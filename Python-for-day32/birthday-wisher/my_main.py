# #################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

LETTER_1 = "letter_templates/letter_1.txt"
LETTER_2 = "letter_templates/letter_2.txt"
LETTER_3 = "letter_templates/letter_3.txt"
letter_path = [LETTER_1, LETTER_2, LETTER_3]
random_letter_path = random.choice(letter_path)

MY_EMAIL = "smallouforme@gmail.com"
PASSWORD = "not setting"

birth_info = pd.read_csv("birthdays.csv")
birth_list = birth_info.to_dict(orient="records")
# to_dict(orient="records") return to a list


today = dt.datetime.now()
matching_record = [record for record in birth_list if
                   record['day'] == today.day and record['month'] == today.month]

matching_name = matching_record[0]["name"]
matching_email = matching_record[0]["email"]


# Todo 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if matching_record:
        with open(random_letter_path, "r") as letter_file:
            letter_content = letter_file.read()
            email_content = letter_content.replace("[NAME]", matching_name)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=matching_email,
                        msg=f"Subject:Happy Birthday\n\n{email_content}.")
