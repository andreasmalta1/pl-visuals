from django.shortcuts import render
import pandas as pd


from api.models import Match, Club, PlayerLeagueData, PlayerCompetitionData
from minutes.utils import get_minutes
from minutes.plots import plt_minutes


def home(request):
    teams = Club.objects.all().order_by("club_name")
    ctx = {"teams": teams}
    return render(request, "minutes/teams.html", ctx)


def teams(request, id):
    club = Club.objects.get(club_id=id)
    league_seasons = (
        PlayerLeagueData.objects.filter(club=club)
        .values_list("season", flat=True)
        .distinct()
    )
    competition_seasons = (
        PlayerCompetitionData.objects.filter(club=club)
        .values_list("season", flat=True)
        .distinct()
    )

    context = {
        "league_seasons": league_seasons,
        "competition_seasons": competition_seasons,
    }
    # Can I use this  routing in pl table ?
    return render(request, "minutes/seasons.html", context)


# minutes = pd.DataFrame(
#     list(PlayerCompetitionData.objects.filter(club=10260).all().values())
# )

# matches = Match.objects.filter(club=10260).first()
# num_matches = matches.num_matches

# df_comps = get_minutes(minutes)

# graph_path = plt_minutes(df_comps, "Manchester-United", num_matches, 10260, "comps")

# return render(request, "minutes/index.html", {"data": graph_path})
