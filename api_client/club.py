import requests
import csv

endpoint = "http://localhost:8000/api/club/"

data = {"club_name": "Manchester City", "club_id": 8465}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
