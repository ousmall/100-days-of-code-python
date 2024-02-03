from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification import Notification


prices = DataManager("prices")
users = DataManager("users")
flight_search = FlightSearch()
notification = Notification()

# before edit data, I should fetch data first
prices_data = prices.get_data()
clients_data = users.get_data()


# client data
def add_users():
    print("Welcome to Small's Flight Club!"
          "\nWe offer you the Best Flight Deals and Email you!"
          "\nPlease sign up:")
    firstname = input("Your first name:>")
    lastname = input("Your last name:>")
    email = input("Email address:>")
    if email.find("@") == -1 or email.find(".") == -1:
        email = input("Invalid Email address, please try again:")
    users.get_user(firstname=firstname, lastname=lastname, email=email)
    print("You will be notify if cheap flights come!")


add_users()


ORIGIN_CITY_IATA = "YYZ"


for city in prices_data:
    if city["iataCode"] == "":
        city_code = flight_search.get_destination_code(city["city"])
        city["iataCode"] = city_code
        prices.update_destination_codes(city)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in prices_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification.send_email(clients_data, flight)
