import datetime as dt
import random
import smtplib

MY_EMAIL = "smallouforme@gmail.com"
PASSWORD = "not setting"


now = dt.datetime.now()
day_of_week = now.weekday()


with open("quotes.txt") as file:
    quotes = file.readlines()
# quotes = [quote.strip() for quote in quotes]  # not necessary
    today_soup = random.choice(quotes)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if day_of_week == 6:
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Daily inspiration\n\n{today_soup}.")