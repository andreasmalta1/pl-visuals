import requests
import csv

endpoint = "http://localhost:8000/api/match/"

num_matches = 0

with open("csv_data/comps_matches.csv", "r") as file:
    csvreader = list(csv.reader(file))
    matches_record = csvreader[-1][7].split("-")

    for value in matches_record:
        num_matches += int(value)


data = {"club": 10260, "season": "2022/2023", "num_matches": num_matches}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
