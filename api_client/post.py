import requests
import csv
import os

lge_endpoint = "http://localhost:8000/api/league/"
comps_endpoint = "http://localhost:8000/api/competition/"

team_folders = os.listdir("csv_data")

for team_folder in team_folders:
    if team_folder == "seasons":
        continue

    lge_team_folder = os.path.join("csv_data", team_folder, "lge")
    comps_team_folder = os.path.join("csv_data", team_folder, "comps")

    endpoint = lge_endpoint

    for competition_folder in [lge_team_folder, comps_team_folder]:
        if competition_folder == comps_team_folder:
            endpoint = comps_endpoint

        csv_files = os.listdir(competition_folder)
        for csv_file in csv_files:
            if "matches" in csv_file:
                continue

            season = csv_file.split(".")[0].replace("-", "/")
            offset = 0
            with open(
                os.path.join(competition_folder, csv_file), "r", encoding="UTF-8"
            ) as file:
                csvreader = csv.reader(file)

                if len(next(csvreader)) == 25:
                    offset = 14

                next(csvreader, None)
                for row in csvreader:
                    data = {}
                    data["season"] = season
                    data["player_name"] = row[1]
                    data["position"] = row[3]
                    data["nation"] = row[2]
                    data["age"] = row[4]
                    data["league"] = row[38 - offset]
                    data["club"] = int(row[37 - offset])
                    data["matches_played"] = int(row[5])
                    data["starts"] = int(row[6])
                    data["minutes"] = int(row[7])
                    data["goals"] = int(row[9])
                    data["assists"] = int(row[10])
                    data["penalty_kicks"] = int(row[14])
                    data["penalty_goals"] = int(row[13])

                    data["yellow_cards"] = int(row[15])
                    data["red_cards"] = int(row[16])
                    if not offset:
                        data["xg"] = float(row[17])
                        data["non_penalty_xg"] = float(row[18])
                        data["xa"] = float(row[19])
                        data["progressive_passes"] = int(row[22])
                        data["progressive_carries"] = int(row[21])
                        data["progressive_receives"] = int(row[23])

                    get_response = requests.post(endpoint, json=data)
                    print(get_response.json())
