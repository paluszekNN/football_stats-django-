from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    tier = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=20)
    club = models.CharField(max_length=100, default='none')
    league = models.CharField(max_length=100, default='none')
    rate = models.FloatField(default=0)
    goals = models.FloatField(default=0)
    assists = models.FloatField(default=0)
    minutes = models.FloatField(default=0)
    accurate_passes = models.FloatField(default=0)
    passes = models.FloatField(default=0)
    created_situations = models.FloatField(default=0)
    key_passes = models.FloatField(default=0)
    dribble = models.FloatField(default=0)
    fouls_on = models.FloatField(default=0)
    offsides = models.FloatField(default=0)
    mistakes = models.FloatField(default=0)
    culpable_goals = models.FloatField(default=0)
    accurate_cross = models.FloatField(default=0)
    heads = models.FloatField(default=0)
    tackles = models.FloatField(default=0)
    key_heads = models.FloatField(default=0)
    interceptions = models.FloatField(default=0)
    catch_saves = models.FloatField(default=0)
    saves = models.FloatField(default=0)
    saves_on_corner = models.FloatField(default=0)
    complete_tackles = models.FloatField(default=0)
    accurate_shots = models.FloatField(default=0)
    shots = models.FloatField(default=0)
    key_tackles = models.FloatField(default=0)
    win_heads = models.FloatField(default=0)
    crosses = models.FloatField(default=0)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def split_league(self):
        return self.league.split(' ')

    def split_club(self):
        return self.club.split(' ')
