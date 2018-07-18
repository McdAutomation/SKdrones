from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Stadium(models.Model):
    #objects = models.Manager()
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE,
                                related_name='games', default='9999')
    objects = models.Manager()
    team_a = models.CharField(max_length=50)
    team_b = models.CharField(max_length=50)
    game_date = models.DateField()


    class Meta:
        ordering = ('game_date',)

    def __str__(self):
        return '{} vs {}'.format(self.team_a, self.team_b)
