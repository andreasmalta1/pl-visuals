from rest_framework import generics

from .models import PlayerLeagueData, PlayerCompetitionData
from .serializers import LeagueDataSerializer, CompetitionDataSerializer


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


league_data_detail_view = LeagueDataDetailAPIView.as_view()
league_data_list_create_view = LeagueDataListCreateAPIView.as_view()
competition_data_detail_view = CompetitionDataDetailAPIView.as_view()
competition_data_list_create_view = CompetitionDataCreateAPIView.as_view()
