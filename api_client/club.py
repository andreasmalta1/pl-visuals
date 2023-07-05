import requests
from teams import TEAMS

endpoint = "http://localhost:8000/api/club/"

for team in TEAMS:
    data = {"club_name": team.replace("-", " "), "club_id": TEAMS[team]["fotmob_id"]}
    get_response = requests.post(endpoint, json=data)
