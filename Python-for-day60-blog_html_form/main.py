from flask import Flask, render_template, request
import requests as rs
from datetime import datetime as dt
import smtplib

# email information
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SECURITY = "TLS"  # SSL/TLS
MY_EMAIL = "smallouforme@gmail.com"
MY_PASS = "vwvepjpzahhreglr"

# blog contents
ARTICLE = "https://api.npoint.io/886b0c394633b04e2704"
response = rs.get(url=ARTICLE)
article_post = response.json()

app = Flask(__name__)

year = dt.now().year


@app.route('/')
def home():
    return render_template("index.html", posts=article_post, current_year=year)


@app.route('/blog/<int:index>')
def blogs(index):
    return render_template("post.html", posts=article_post, index=index, current_year=year)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    result = None
    if request.method == 'POST':
        if request.form:
            name = request.form['name']
            email = request.form['email']
            phone_num = request.form['phone']
            message = request.form['message']
            send_email(name, email, phone_num, message)
            result = "Successfully sent your message!"
            return render_template("contact.html", current_year=year, result=result, sent_message=True)
    return render_template("contact.html", current_year=year, result=result, sent_message=False)


@app.route('/about')
def self_information():
    return render_template("about.html", current_year=year)


def send_email(name, email, phone_num, message):
    try:
        email_message = (f"Subject: A message comes from your blog!\n\n"
                         f"You got a message:\n"
                         f"From {name}, Email:{email}, phone number:{phone_num} \n"
                         f"For details:\n"
                         f"{message}")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=email_message)
            print(f"The message was sent.")
    except smtplib.SMTPServerDisconnected:
        print("ERROR: Could not connect to the SMTP server. "
              "Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly.")


if __name__ == "__main__":
    app.run(debug=True)
