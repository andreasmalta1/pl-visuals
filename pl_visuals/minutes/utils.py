import urllib.request
import numpy as np
from PIL import Image


def get_minutes(df):
    df["90s"] = df.apply(lambda row: np.around(np.divide(row.minutes, 90), 1), axis=1)
    df = df[
        [
            "player_name",
            "nation",
            "position",
            "age",
            "minutes",
            "matches_played",
            "starts",
            "90s",
            "league_id",
        ]
    ]
    df["minutes"] = df["minutes"].astype(float)
    df = df[df["minutes"] >= 400].reset_index(drop=True)
    df = df.sort_values(by="minutes").reset_index(drop=True)
    df = df[~df["position"].isna()]
    df["nation"] = [x.split(" ")[1].lower() for x in df["nation"]]
    df["minutes"] = [int(x) for x in df["minutes"]]
    return df


def annotate_axis(ax):
    ax.annotate(
        "Data from fbref.com",
        (0, 0),
        (0, -20),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    ax.annotate(
        "Viz by @andreascalleja",
        (0, 0),
        (0, -30),
        fontsize=8,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    return ax


def ax_logo(logo_id, ax, league=False, alpha=1):
    url = "https://images.fotmob.com/image_resources/logo/teamlogo/"
    if league:
        url = "https://images.fotmob.com/image_resources/logo/leaguelogo/"
    icon = Image.open(urllib.request.urlopen(f"{url}{logo_id}.png"))
    ax.imshow(icon, alpha=alpha)
    ax.axis("off")
    return ax


def minutes_battery(ax, minutes, num_games):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    pct = minutes / (90 * num_games)
    ax.barh([0.5], [1], fc="#EFE9E6", ec="black", height=0.35)
    ax.barh([0.5], [pct], fc="#00529F", height=0.35)
    if pct > 0.3:
        ax.annotate(
            xy=(pct, 0.5),
            text=f"{pct:.0%}",
            xytext=(-8, 0),
            textcoords="offset points",
            weight="bold",
            color="#EFE9E6",
            va="center",
            ha="center",
            size=5,
        )
    else:
        ax.annotate(
            xy=(pct + 0.01, 0.5),
            text=f"{pct:.0%}",
            weight="bold",
            color="#00529F",
            va="center",
            ha="left",
            size=5,
        )
    ax.set_axis_off()
    return ax
