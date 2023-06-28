from django.shortcuts import render
import pandas as pd


from api.models import PlayerCompetitionData, Match
from minutes.utils import get_minutes
from minutes.plots import plt_minutes


def home(request):
    minutes = pd.DataFrame(
        list(PlayerCompetitionData.objects.filter(club=10260).all().values())
    )

    matches = Match.objects.filter(club=10260).first()
    num_matches = matches.num_matches

    df_comps = get_minutes(minutes)

    graph_path = plt_minutes(df_comps, "Manchester-United", num_matches, 10260, "comps")

    return render(request, "minutes/index.html", {"data": graph_path})
