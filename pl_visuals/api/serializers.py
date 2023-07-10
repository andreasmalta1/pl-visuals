from rest_framework import serializers

from .models import Club, League, Match, PlayerLeagueData, PlayerCompetitionData


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["club_id", "club_name"]


class ClubPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["club_name"]


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ["league_id", "name", "code", "country", "confederation"]


class LeaguePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ["name"]


class MatchSerializer(serializers.ModelSerializer):
    club_info = ClubPublicSerializer(source="club", read_only=True)
    league_info = LeaguePublicSerializer(source="league", read_only=True)

    class Meta:
        model = Match
        fields = [
            "id",
            "club",
            "club_info",
            "league",
            "league_info",
            "season",
            "num_matches_league",
            "num_matches_comps",
        ]


class LeagueDataSerializer(serializers.ModelSerializer):
    club_info = ClubPublicSerializer(source="club", read_only=True)
    league_info = LeaguePublicSerializer(source="league", read_only=True)

    class Meta:
        model = PlayerLeagueData
        fields = [
            "id",
            "club",
            "club_info",
            "league",
            "league_info",
            "season",
            "player_name",
            "nation",
            "position",
            "age",
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
    club_info = ClubPublicSerializer(source="club", read_only=True)
    league_info = LeaguePublicSerializer(source="league", read_only=True)

    class Meta:
        model = PlayerCompetitionData
        fields = [
            "id",
            "club",
            "club_info",
            "league",
            "league_info",
            "season",
            "player_name",
            "nation",
            "position",
            "age",
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
