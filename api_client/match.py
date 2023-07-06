import requests
import csv
import os

from teams import TEAMS

endpoint = "http://localhost:8000/api/match/"

team_folders = os.listdir("csv_data")
for team_folder in team_folders:
    if team_folder == "seasons":
        continue

    team_name = team_folder.title()
    club = TEAMS[team_name]["fotmob_id"]

    lge_team_folder = os.path.join("csv_data", team_folder, "lge")
    comps_team_folder = os.path.join("csv_data", team_folder, "comps")

    csv_files = os.listdir(lge_team_folder)
    for csv_file in csv_files:
        if "matches" not in csv_file:
            continue

        season = csv_file.split(".")[0].replace("-", "/").replace("_matches", "")

        league_csv = os.path.join(lge_team_folder, csv_file)
        comps_csv = os.path.join(comps_team_folder, csv_file)

        num_matches_league = 0
        num_matches_comps = 0

        with open(league_csv, "r") as file:
            csvreader = list(csv.reader(file))
            matches_record = csvreader[-1][6].split("-")

            for value in matches_record:
                num_matches_league += int(value)

        with open(comps_csv, "r") as file:
            csvreader = list(csv.reader(file))
            matches_record = csvreader[-1][7].split("-")

            for value in matches_record:
                num_matches_comps += int(value)

        data = {
            "club": club,
            "season": season,
            "num_matches_league": num_matches_league,
            "num_matches_comps": num_matches_comps,
            "league": 47,
        }

        get_response = requests.post(endpoint, json=data)
        print(get_response.json())
