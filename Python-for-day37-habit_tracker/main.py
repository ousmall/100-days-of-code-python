import requests as rs
from datetime import datetime, timedelta

TOKEN = "secrete"
USERNAME = "smallou"
GRAPH_ID = "first-graph-2024"

# create a user account
Pixela_endpoint = "https://pixe.la/v1/users"

Pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # when using post, parameters should be "json"
# response = rs.post(url=Pixela_endpoint, json=Pixela_params)
# print(response.text)
# # https://pixe.la/@smallou


# create a graph

graph_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs"

header = {"X-USER-TOKEN": TOKEN}

graph_params = {
    "id": GRAPH_ID,
    "name": "English_learning",
    "unit": "minute",
    "type": "int",
    "color": "ichou",
}

# graph_response = rs.post(url=graph_endpoint, headers=header, json=graph_params)
# print(graph_response.text)
# # https://pixe.la/v1/users/smallou/graphs/first-graph-2024.html


# post a pixel

post_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_header = header

today = datetime.now().strftime("%Y%m%d")
yesterday = (datetime.now() - timedelta(1)).strftime("%Y%m%d")
# format the type of date: https://www.w3schools.com/python/python_datetime.asp

post_params = {
    "date": yesterday,
    "quantity": "78",
}

# post_response = rs.post(url=post_endpoint, headers=header, json=post_params)
# print(post_response.text)


# update the data for using put

update_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_header = header

update_params = {"quantity": "76"}

update_response = rs.put(url=update_endpoint, headers=header, json=update_params)
print(update_response.text)


# delete data for using delete
delete_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"  # change the date

delete_header = header

# delete_response = rs.delete(url=delete_endpoint, headers=header)
# print(delete_response)
