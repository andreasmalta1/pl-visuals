from django.db import models


class Club(models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=100)

    def __str__(self):
        return self.club_name


class League(models.Model):
    league_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    country = models.CharField(max_length=30)
    confederation = models.CharField(max_length=30)


class Match(models.Model):
    club = models.ForeignKey("Club", on_delete=models.CASCADE)
    league = models.ForeignKey("League", on_delete=models.SET_NULL, null=True)
    season = models.CharField(max_length=10)
    num_matches_league = models.IntegerField()
    num_matches_comps = models.IntegerField()

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
    league = models.ForeignKey("League", on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey("Club", on_delete=models.CASCADE)

    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    penalty_kicks = models.IntegerField()
    penalty_goals = models.IntegerField()
    xg = models.FloatField(null=True)
    non_penalty_xg = models.FloatField(null=True)
    xa = models.FloatField(null=True)

    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    progressive_passes = models.IntegerField(null=True)
    progressive_carries = models.IntegerField(null=True)
    progressive_receives = models.IntegerField(null=True)

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
    league = models.ForeignKey("League", on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey("Club", on_delete=models.CASCADE)

    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    penalty_kicks = models.IntegerField()
    penalty_goals = models.IntegerField()
    xg = models.FloatField(null=True)
    non_penalty_xg = models.FloatField(null=True)
    xa = models.FloatField(null=True)

    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    progressive_passes = models.IntegerField(null=True)
    progressive_carries = models.IntegerField(null=True)
    progressive_receives = models.IntegerField(null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name
