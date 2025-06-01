import requests

API_KEY = "ba24ff28d95f2cdaeda6ee64a8c90cd5"


url = "http://api.aviationstack.com/v1/flights"
params = {
    "access_key": API_KEY,
    "limit": 3
}

response = requests.get(url, params=params)
print("Response status code:", response.status_code)
print("Response data:")
print(response.json())
