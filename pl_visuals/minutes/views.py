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

    league_season_list = [int(season[:4]) for season in league_seasons]
    competitions_season_list = [int(season[:4]) for season in competition_seasons]

    context = {
        "league_seasons": league_season_list,
        "competition_seasons": competitions_season_list,
        "club": club,
    }
    return render(request, "minutes/seasons.html", context)


def league_graph(request, id, season):
    club = Club.objects.get(club_id=id)
    season = f"{season}/{season+1}"
    minutes = pd.DataFrame(
        list(PlayerLeagueData.objects.filter(club=club, season=season).all().values())
    )

    matches = Match.objects.filter(club=club, season=season).first()
    num_matches = matches.num_matches_league

    df = get_minutes(minutes)

    graph = plt_minutes(df, club.club_name, num_matches, club.club_id, "lge")

    return render(request, "minutes/graph.html", {"data": graph})


def comp_graph(request, id, season):
    club = Club.objects.get(club_id=id)
    season = f"{season}/{season+1}"
    minutes = pd.DataFrame(
        list(
            PlayerCompetitionData.objects.filter(club=club, season=season)
            .all()
            .values()
        )
    )

    matches = Match.objects.filter(club=club, season=season).first()
    num_matches = matches.num_matches_comps

    df = get_minutes(minutes)

    graph = plt_minutes(df, club.club_name, num_matches, club.club_id, "comps")

    return render(request, "minutes/graph.html", {"data": graph})
