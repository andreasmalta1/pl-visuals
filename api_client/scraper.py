import os
import time
import pandas as pd

from teams import TEAMS
from constants import COLUMNS_FULL, COLUMNS_MINI


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


def get_teams_data():
    for team_name in TEAMS:
        print(team_name)
        for season in reversed(range(1992, 2019)):
            time.sleep(60)

            fbref_id = TEAMS[team_name]["fbref_id"]
            fotmob_id = TEAMS[team_name]["fotmob_id"]
            if TEAMS[team_name].get("short_name"):
                team_name = TEAMS[team_name].get("short_name")

            url_lge = f"https://fbref.com/en/squads/{fbref_id}/{season}-{season+1}/{team_name}-Stats"
            comps_lge = f"https://fbref.com/en/squads/{fbref_id}/{season}-{season+1}/all_comps/{team_name}-Stats-All-Competitions"

            df_lge = get_info(url_lge)
            df_comps = get_info(comps_lge)

            if df_lge.empty:
                return

            df_lge.drop(columns=df_lge.columns[-1], axis=1, inplace=True)
            df_comps.drop(columns=df_comps.columns[-1], axis=1, inplace=True)

            if len(df_lge.columns) == 33:
                df_lge.columns = COLUMNS_FULL
                df_comps.columns = COLUMNS_FULL
            else:
                df_lge.columns = COLUMNS_MINI
                df_comps.columns = COLUMNS_MINI

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

            url_lge_mth = f"https://fbref.com/en/squads/{fbref_id}/{season}-{season+1}/matchlogs/c9/misc/{team_name}-Match-Logs"
            url_comps_mth = f"https://fbref.com/en/squads/{fbref_id}/{season}-{season+1}/matchlogs/all_comps/misc/{team_name}-Match-Logs-All-Competitions"

            df_lge_mth = get_info(url_lge_mth)
            df_comps_mth = get_info(url_comps_mth)

            file_path_lge = f"csv_data/{team_name.lower()}/lge"
            file_path_comps = f"csv_data/{team_name.lower()}/comps"

            if not os.path.isdir(file_path_lge):
                os.makedirs(file_path_lge)
            if not os.path.isdir(file_path_comps):
                os.makedirs(file_path_comps)

            df_lge.to_csv(os.path.join(file_path_lge, f"{season}-{season+1}.csv"))
            df_comps.to_csv(os.path.join(file_path_comps, f"{season}-{season+1}.csv"))
            df_lge_mth.to_csv(
                os.path.join(file_path_lge, f"{season}-{season+1}_matches.csv")
            )
            df_comps_mth.to_csv(
                os.path.join(file_path_comps, f"{season}-{season+1}_matches.csv")
            )


get_teams_data()
