import requests
import csv
import os

from teams import TEAMS

endpoint = "http://localhost:8000/api/league/"

data = {
    "league_id": 47,
    "name": "Premier League",
    "code": "epl",
    "country": "England",
    "confederation": "UEFA",
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
