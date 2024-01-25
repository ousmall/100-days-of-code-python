import requests as rs

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = rs.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data_trivia = response.json()


question_data = data_trivia["results"]