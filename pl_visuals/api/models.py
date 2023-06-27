from django.db import models


class PlayerLeagueData(models.Model):
    season = models.CharField(max_length=10)
    player_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    league = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    club_id = models.IntegerField()

    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    penalty_kicks = models.IntegerField()
    penalty_goals = models.IntegerField()
    xg = models.FloatField()
    non_penalty_xg = models.FloatField()
    xa = models.FloatField()

    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    progressive_passes = models.IntegerField()
    progressive_carries = models.IntegerField()
    progressive_receives = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name


class PlayerCompetitionData(models.Model):
    season = models.CharField(max_length=10)
    player_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    league = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    club_id = models.IntegerField()

    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    penalty_kicks = models.IntegerField()
    penalty_goals = models.IntegerField()
    xg = models.FloatField()
    non_penalty_xg = models.FloatField()
    xa = models.FloatField()

    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    progressive_passes = models.IntegerField()
    progressive_carries = models.IntegerField()
    progressive_receives = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name
