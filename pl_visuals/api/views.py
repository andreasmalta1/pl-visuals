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
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class LeagueDetailAPIView(generics.RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueListCreateAPIView(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class MatchDetailAPIView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchListCreateAPIView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class LeagueDataDetailAPIView(generics.RetrieveAPIView):
    queryset = PlayerLeagueData.objects.all()
    serializer_class = LeagueDataSerializer


class LeagueDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = PlayerLeagueData.objects.all()
    serializer_class = LeagueDataSerializer


class CompetitionDataDetailAPIView(generics.RetrieveAPIView):
    queryset = PlayerCompetitionData.objects.all()
    serializer_class = CompetitionDataSerializer


class CompetitionDataCreateAPIView(generics.ListCreateAPIView):
    queryset = PlayerCompetitionData.objects.all()
    serializer_class = CompetitionDataSerializer


club_detail_view = ClubDetailAPIView.as_view()
club_list_create_view = ClubListCreateAPIView.as_view()
league_detail_view = LeagueDetailAPIView.as_view()
league_list_create_view = LeagueListCreateAPIView.as_view()
match_detail_view = MatchDetailAPIView.as_view()
match_list_create_view = MatchListCreateAPIView.as_view()
league_data_detail_view = LeagueDataDetailAPIView.as_view()
league_data_list_create_view = LeagueDataListCreateAPIView.as_view()
competition_data_detail_view = CompetitionDataDetailAPIView.as_view()
competition_data_list_create_view = CompetitionDataCreateAPIView.as_view()
