from django.db import models


class Club(models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=100)

    def __str__(self):
        return self.club_name


class Match(models.Model):
    club = models.ForeignKey("Club", on_delete=models.CASCADE)
    season = models.CharField(max_length=10)
    num_matches = models.IntegerField()

    def __str__(self):
        return f"{self.club_name} - {self.season}"

    class Meta:
        verbose_name_plural = "Matches"


class PlayerLeagueData(models.Model):
    season = models.CharField(max_length=10)
    player_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    league = models.CharField(max_length=50)
    club = models.ForeignKey("Club", on_delete=models.CASCADE)

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
    club = models.ForeignKey("Club", on_delete=models.CASCADE)

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
