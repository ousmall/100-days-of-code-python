import requests
import account_data

SHEETY_ENDPOINT = "https://api.sheety.co/"


class DataManager:

    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.sheet_url = SHEETY_ENDPOINT + account_data.SHEET_URL + self.sheet_name
        self.headers = {
            "Authorization": f"Bearer {account_data.SHEETY_TOKEN}"
        }

    def get_data(self):
        response = requests.get(url=self.sheet_url, headers=self.headers)
        response.raise_for_status()
        data = response.json()[self.sheet_name]
        return data

    def update_destination_codes(self, city):
        new_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(url=f"{self.sheet_url}/{city['id']}",
                                json=new_data, headers=self.headers)
        response.raise_for_status()
        # print(response.text)

    def get_user(self, firstname, lastname, email):  # single data, dont add "s"
        client_data = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }
        response = requests.post(url=self.sheet_url,
                                 json=client_data, headers=self.headers)
        response.raise_for_status()
        print(response.text)
        print(f"Success! Your information:{firstname.title()} {lastname.title()} and "
              f"{email} has been stored!")
