import requests
import csv

endpoint = "http://localhost:8000/api/competition/"

with open("csv_data/comps_info.csv", "r") as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    data = {}
    for row in csvreader:
        data["season"] = "2022/2023"
        data["player_name"] = row[1]
        data["position"] = row[3]
        data["nation"] = row[2]
        data["age"] = row[4]
        data["league"] = row[38]
        data["club"] = row[36]
        data["club_id"] = int(row[37])
        data["matches_played"] = int(row[5])
        data["starts"] = int(row[6])
        data["minutes"] = int(row[7])
        data["goals"] = int(row[9])
        data["assists"] = int(row[10])
        data["penalty_kicks"] = int(row[14])
        data["penalty_goals"] = int(row[13])
        data["xg"] = float(row[17])
        data["non_penalty_xg"] = float(row[18])
        data["xa"] = float(row[19])
        data["yellow_cards"] = int(row[15])
        data["red_cards"] = int(row[16])
        data["progressive_passes"] = int(row[22])
        data["progressive_carries"] = int(row[21])
        data["progressive_receives"] = int(row[23])

        get_response = requests.post(endpoint, json=data)
        print(get_response.json())
