from rest_framework import serializers

from .models import Club, Match, PlayerLeagueData, PlayerCompetitionData


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["club_id", "club_name"]


class MatchSerializer(serializers.ModelSerializer):
    clubs = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="club_name"
    )

    class Meta:
        model = Match
        fields = ["clubs", "season", "num_matches"]


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
