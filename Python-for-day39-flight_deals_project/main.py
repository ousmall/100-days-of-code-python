from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()


# fetch data
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"


for city in sheet_data:
    if city["iataCode"] == "":
        city_code = flight_search.get_destination_code(city["city"])
        city["iataCode"] = city_code
        data_manager.update_destination_codes(city)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:

        print(f"Low price alert! Only CA${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
              f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to "
              f"{flight.return_date}.")
