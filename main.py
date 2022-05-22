import requests
import datetime as dt

USER_NAME
TOKEN
GRAPH_ID = 'graph1'
DATE = dt.datetime.now().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'hour',
    'type': 'float',
    'color': 'ichou'
}
header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_config = {
    'date': DATE,
    'quantity': '2',
 }
# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=header)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
update_pixel_params = {
    'quantity': '4',
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=header)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=header)
print(response.text)
