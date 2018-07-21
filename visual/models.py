from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def game_stage_choices():
    return [('Group','Group'),('Round of 16','Round of 16'),('Quarter','Quarter'),('Semis','Semis')]
# Create your models here.
class Stadium(models.Model):
    #objects = models.Manager()
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    #world_cup_year = models.DateField(default='2018-06-14')
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year())

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
    score = models.CharField(max_length=5,default='0-0')
    stage = models.CharField(max_length=20,choices=game_stage_choices(),default='Group')
    game_date = models.DateField()


    class Meta:
        ordering = ('game_date',)

    def __str__(self):
        return '{} vs {}'.format(self.team_a, self.team_b)
