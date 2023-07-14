import os
import csv
import time
import requests
import pandas as pd

from teams import TEAMS
from constants import COLUMNS_FULL

new_season = 2022
season = f"{new_season}-{new_season+1}"
season_model = f"{new_season}/{new_season+1}"


def get_info(url):
    html = pd.read_html(url, header=0)
    if not html:
        return pd.DataFrame()

    df = html[0]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    return df


def drop_rows(df, column, value):
    for i in df.index:
        if df.at[i, column] == value:
            df = df.drop([i])
    return df


def get_team_data(
    team_name,
    csv_lge,
    csv_comps,
    csv_mth_lge,
    csv_mth_comps,
):
    time.sleep(60)

    print(team_name)
    print(season)

    fbref_id = TEAMS[team_name]["fbref_id"]
    fotmob_id = TEAMS[team_name]["fotmob_id"]
    if TEAMS[team_name].get("short_name"):
        team_name = TEAMS[team_name].get("short_name")

    url_lge = f"https://fbref.com/en/squads/{fbref_id}/{season}/{team_name}-Stats"
    comps_lge = f"https://fbref.com/en/squads/{fbref_id}/{season}/all_comps/{team_name}-Stats-All-Competitions"

    df_lge = get_info(url_lge)
    df_comps = get_info(comps_lge)

    df_lge.drop(columns=df_lge.columns[-1], axis=1, inplace=True)
    df_comps.drop(columns=df_comps.columns[-1], axis=1, inplace=True)

    df_lge.columns = COLUMNS_FULL
    df_comps.columns = COLUMNS_FULL

    df_lge = drop_rows(df_lge, "MP", "0")
    df_lge = drop_rows(df_lge, "90s", "0.0")
    df_comps = drop_rows(df_comps, "MP", "0")
    df_comps = drop_rows(df_comps, "90s", "0.0")

    df_lge = df_lge.dropna().reset_index(drop=True)
    df_comps = df_comps.dropna().reset_index(drop=True)

    df_lge["club_name"] = team_name
    df_comps["club_name"] = team_name

    df_lge["club_id"] = fotmob_id
    df_comps["club_id"] = fotmob_id

    df_lge["lge"] = "epl"
    df_comps["lge"] = "epl"

    df_lge = df_lge.replace("gf GUF", "fr FRA")
    df_comps = df_comps.replace("gf GUF", "fr FRA")

    url_lge_mth = f"https://fbref.com/en/squads/{fbref_id}/{season}/matchlogs/c9/misc/{team_name}-Match-Logs"
    url_comps_mth = f"https://fbref.com/en/squads/{fbref_id}/{season}/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

    df_lge_mth = get_info(url_lge_mth)
    df_comps_mth = get_info(url_comps_mth)

    df_lge.to_csv(csv_lge)
    df_comps.to_csv(csv_comps)
    df_lge_mth.to_csv(csv_mth_lge)
    df_comps_mth.to_csv(csv_mth_comps)


def post_data(csv_file, team, competition):
    with open(csv_file, "r", encoding="UTF-8") as file:
        csvreader = csv.reader(file)
        next(csvreader, None)

        for row in csvreader:
            data = {}
            data["season"] = season_model
            data["player_name"] = row[1]
            data["position"] = row[3]
            data["nation"] = row[2]
            data["age"] = row[4]
            data["league"] = 47
            data["club"] = int(row[35])
            data["matches_played"] = int(row[5])
            data["starts"] = int(row[6])
            data["minutes"] = int(row[7])
            data["goals"] = int(row[9])
            data["assists"] = int(row[10])
            data["penalty_kicks"] = int(row[14])
            data["penalty_goals"] = int(row[13])
            data["yellow_cards"] = int(row[15])
            data["red_cards"] = int(row[16])
            data["xg"] = float(row[17])
            data["non_penalty_xg"] = float(row[18])
            data["xa"] = float(row[19])
            data["progressive_passes"] = int(row[22])
            data["progressive_carries"] = int(row[21])
            data["progressive_receives"] = int(row[23])

            endpoint = f"http://localhost:8000/api/{competition}-data/"

            get_response = requests.post(endpoint, json=data)
            print(get_response.json())


def post_matches(csv_mth_lge, csv_mth_comps, team):
    num_matches_league = 0
    num_matches_comps = 0

    with open(csv_mth_lge, "r", encoding="UTF-8") as file:
        csvreader = list(csv.reader(file))
        matches_record = csvreader[-1][6].split("-")

        for value in matches_record:
            num_matches_league += int(value)

    with open(csv_mth_comps, "r", encoding="UTF-8") as file:
        csvreader = list(csv.reader(file))
        matches_record = csvreader[-1][7].split("-")

        for value in matches_record:
            num_matches_comps += int(value)

    get_endpoint = f"http://localhost:8000/api/club/?team={team.replace(' ', '%20')}"
    get_response = requests.get(get_endpoint).json()
    data = get_response["results"]
    club_id = data[0]["club_id"]

    data = {
        "club": club_id,
        "season": season_model,
        "num_matches_league": num_matches_league,
        "num_matches_comps": num_matches_comps,
        "league": 47,
    }

    endpoint = f"http://localhost:8000/api/match/"

    update = requests.put(endpoint, json=data)
    print(update.json())


def main():
    df_epl = pd.read_csv("csv_data/seasons/epl.csv")
    df_epl = df_epl.iloc[:, -1:].fillna(0)
    teams = df_epl[season].values

    for team in teams:
        if not team:
            continue

        team_name = team.replace(" ", "-")

        file_path_lge = f"csv_data/{team_name.lower()}/lge"
        file_path_comps = f"csv_data/{team_name.lower()}/comps"

        if not os.path.isdir(file_path_lge):
            os.makedirs(file_path_lge)
        if not os.path.isdir(file_path_comps):
            os.makedirs(file_path_comps)

        csv_lge = os.path.join(file_path_lge, f"{season}.csv")
        csv_comps = os.path.join(file_path_comps, f"{season}.csv")
        csv_mth_lge = os.path.join(file_path_lge, f"{season}_matches.csv")
        csv_mth_comps = os.path.join(file_path_comps, f"{season}_matches.csv")

        get_team_data(
            team_name,
            csv_lge,
            csv_comps,
            csv_mth_lge,
            csv_mth_comps,
        )

        post_data(csv_lge, team, "league")
        post_data(csv_comps, team, "competition")

        post_matches(csv_mth_lge, csv_mth_comps, team)


main()
