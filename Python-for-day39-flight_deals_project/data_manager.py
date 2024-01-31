import requests
import account_data

SHEETY_ENDPOINT = "https://api.sheety.co/"


class DataManager:

    def __init__(self):
        self.sheet_url = SHEETY_ENDPOINT + account_data.SHEET_URL
        self.headers = {
            "Authorization": f"Bearer {account_data.SHEETY_TOKEN}"
        }

    def get_destination_data(self):
        response = requests.get(self.sheet_url, headers=self.headers)
        response.raise_for_status()
        data = response.json()["prices"]
        return data

    def update_destination_codes(self, city):
        new_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(
            url=f"{self.sheet_url}/{city['id']}",
            json=new_data,
            headers=self.headers
        )
        response.raise_for_status()
        # print(response.text)
