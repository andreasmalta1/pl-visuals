import os
import pandas as pd


def get_teams():
    df_seasons = pd.DataFrame()

    for season in range(1992, 2023):
        url = f"https://fbref.com/en/comps/9/{season}-{season+1}/{season}-{season+1}-Premier-League-Stats"
        html = pd.read_html(url, header=0)
        df = html[0][["Squad"]]
        col_name = f"{season}-{season+1}"
        col_list = df.Squad.values.tolist()
        df_seasons[col_name] = pd.Series(col_list)

    path = "csv_data/seasons"
    if not os.path.isdir(path):
        os.makedirs(path)

    df_seasons.to_csv(os.path.join(path, "epl.csv"))


def get_teams_list():
    df = pd.read_csv("csv_data/seasons/epl.csv")
    teams = []
    for col in df.columns:
        team_list = df[col].unique().tolist()
        for team in team_list:
            if team not in teams:
                teams.append(team)


get_teams()
