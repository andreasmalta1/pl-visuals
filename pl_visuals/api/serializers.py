from rest_framework import serializers

from .models import PlayerLeagueData, PlayerCompetitionData


class LeagueDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerLeagueData
        fields = [
            "season",
            "player_name",
            "nation",
            "position",
            "age",
            "league",
            "club",
            "club_id",
            "matches_played",
            "starts",
            "minutes",
            "goals",
            "assists",
            "penalty_kicks",
            "penalty_goals",
            "xg",
            "non_penalty_xg",
            "xa",
            "yellow_cards",
            "red_cards",
            "progressive_passes",
            "progressive_carries",
            "progressive_receives",
        ]


class CompetitionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCompetitionData
        fields = [
            "season",
            "player_name",
            "nation",
            "position",
            "age",
            "league",
            "club",
            "club_id",
            "matches_played",
            "starts",
            "minutes",
            "goals",
            "assists",
            "penalty_kicks",
            "penalty_goals",
            "xg",
            "non_penalty_xg",
            "xa",
            "yellow_cards",
            "red_cards",
            "progressive_passes",
            "progressive_carries",
            "progressive_receives",
        ]
