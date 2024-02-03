import account_data
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SECURITY = "SSL/TLS"
SENDER_NAME = "Small's Flight Club"


class Notification:

    def __init__(self):
        self.email_server = SMTP_SERVER
        self.port = SMTP_PORT

    def send_email(self, users, flight):
        try:
            for user in users:
                receiver = user["email"]
                client_name = f"{user["firstName"]} {user["lastName"]}"
                message = (f"Subject:Low Price Alart from {SENDER_NAME}\n\n"
                           f"Dear {client_name},\nGreat Deal for you!"
                           f"\nOnly CA${flight.price} to fly from "
                           f"{flight.origin_city}-{flight.origin_airport} to "
                           f"{flight.destination_city}-{flight.destination_airport}, "
                           f"from {flight.out_date} to {flight.return_date}.")

                with smtplib.SMTP(self.email_server, self.port) as connection:
                    connection.starttls()
                    connection.login(user=account_data.SMTP_USER, password=account_data.SMTP_PASS)
                    connection.sendmail(from_addr=account_data.SENDER_ADDRESS,
                                        to_addrs=receiver,
                                        msg=message)
                    print(f"The message to {receiver} was sent.")
        except smtplib.SMTPServerDisconnected:
            print("ERROR: Could not connect to the SMTP server. "
                  "Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly.")

