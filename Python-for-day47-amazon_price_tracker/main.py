import requests
import sys  # import it to change encode and decode method
from bs4 import BeautifulSoup
import smtplib

# some constant information
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SECURITY = "TLS"  # SSL/TLS
MY_EMAIL = "smallouforme@gmail.com"
MY_PASS = "vwvepjpzahhreglr"
EXPECTED_PRICE = 499

# Todo 1: get price of the stuff we want from Amazon
amazon_ipad_url = ("https://www.amazon.com/Apple-2022-10-9-inch-iPad-Wi-Fi/dp/B0BJLDDCGS/"
                   "ref=sr_1_2?crid=ZVGBKG7NA0DD&keywords=ipad&qid=1707493341&refinements"
                   "=p_89%3AApple%2Cp_n_condition-type%3A2224371011&rnid=2224369011&s"
                   "=electronics&sprefix=%2Caps%2C250&sr=1-2&th=1")
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/121.0.0.0 Safari/537.36",
    "accept-language": "en-US,en;q=0.5",
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br"
}

# my window system need to alternate the encode method, just ask chatGPT
sys.stdout.reconfigure(encoding='utf-8')

response = requests.get(url=amazon_ipad_url, headers=headers)
ipad_page = response.text.encode('utf-8').decode('utf-8')

soup = BeautifulSoup(ipad_page, "lxml")
price = soup.find("span", class_="a-offscreen").get_text().split("$")[1]
good = soup.find("span", id="productTitle").get_text().strip()


try:
    message = (f"Subject: Amazon Price Alert!\n\n"
               f"Dear Small,\n"
               f"Great Deal for you!\n"
               f"{good} is now only ${price}!\n"
               f"For details:\n"
               f"{amazon_ipad_url}").encode("utf-8")
    # .encode("utf-8") Converts the entire string to a UTF-8 encoded byte sequence

    if float(price) < EXPECTED_PRICE:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=message)
            print(f"The message was sent.")
except smtplib.SMTPServerDisconnected:
    print("ERROR: Could not connect to the SMTP server. "
          "Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly.")