from rest_framework import generics

from .models import Club, League, Match, PlayerLeagueData, PlayerCompetitionData
from .serializers import (
    ClubSerializer,
    LeagueSerializer,
    MatchSerializer,
    LeagueDataSerializer,
    CompetitionDataSerializer,
)


class ClubDetailAPIView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ClubSerializer

    def get_queryset(self):
        queryset = Club.objects.all().order_by("club_id")
        team = self.request.query_params.get("team")
        if team:
            queryset = queryset.filter(club_name=team)

        return queryset


class LeagueDetailAPIView(generics.RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueListCreateAPIView(generics.ListCreateAPIView):
    queryset = League.objects.all().order_by("league_id")
    serializer_class = LeagueSerializer


class MatchDetailAPIView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        queryset = Match.objects.all().order_by("id")
        team = self.request.query_params.get("team")
        season = self.request.query_params.get("season")
        if team:
            queryset = queryset.filter(club__club_name=team)
        if season:
            queryset = queryset.filter(season=season)

        return queryset


class MatchUpdateAPIView(generics.UpdateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class LeagueDataDetailAPIView(generics.RetrieveAPIView):
    queryset = PlayerLeagueData.objects.all()
    serializer_class = LeagueDataSerializer


class LeagueDataListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LeagueDataSerializer

    def get_queryset(self):
        queryset = PlayerLeagueData.objects.all().order_by("id")
        team = self.request.query_params.get("team")
        season = self.request.query_params.get("season")
        player = self.request.query_params.get("player")
        if team:
            queryset = queryset.filter(club__club_name=team)
        if season:
            queryset = queryset.filter(season=season)
        if player:
            queryset = queryset.filter(player_name=player)

        return queryset


class LeagueDataUpdateAPIView(generics.UpdateAPIView):
    queryset = PlayerLeagueData.objects.all()
    serializer_class = LeagueDataSerializer


class CompetitionDataDetailAPIView(generics.RetrieveAPIView):
    queryset = PlayerCompetitionData.objects.all()
    serializer_class = CompetitionDataSerializer


class CompetitionDataListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CompetitionDataSerializer

    def get_queryset(self):
        queryset = PlayerCompetitionData.objects.all().order_by("id")
        team = self.request.query_params.get("team")
        season = self.request.query_params.get("season")
        player = self.request.query_params.get("player")
        if team:
            queryset = queryset.filter(club__club_name=team)
        if season:
            queryset = queryset.filter(season=season)
        if player:
            queryset = queryset.filter(player_name=player)

        return queryset


class CompetitionDataUpdateAPIView(generics.UpdateAPIView):
    queryset = PlayerCompetitionData.objects.all()
    serializer_class = CompetitionDataSerializer


club_detail_view = ClubDetailAPIView.as_view()
club_list_create_view = ClubListCreateAPIView.as_view()
league_detail_view = LeagueDetailAPIView.as_view()
league_list_create_view = LeagueListCreateAPIView.as_view()
match_detail_view = MatchDetailAPIView.as_view()
match_list_create_view = MatchListCreateAPIView.as_view()
match_update_view = MatchUpdateAPIView.as_view()
league_data_detail_view = LeagueDataDetailAPIView.as_view()
league_data_list_create_view = LeagueDataListCreateAPIView.as_view()
league_data_update_view = LeagueDataUpdateAPIView.as_view()
competition_data_detail_view = CompetitionDataDetailAPIView.as_view()
competition_data_list_create_view = CompetitionDataListCreateAPIView.as_view()
competition_data_update_view = CompetitionDataUpdateAPIView.as_view()
