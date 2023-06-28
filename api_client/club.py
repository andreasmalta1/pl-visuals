import requests
import csv

endpoint = "http://localhost:8000/api/club/"

data = {"club_name": "Arsenal", "club_id": 9825}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
