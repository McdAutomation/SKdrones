from django.contrib import admin
from .models import Game, Stadium


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('team_a', 'team_b', 'game_date')
    search_fields = ('team_a', 'team_b')
    raw_id_fields = ('stadium',)


@admin.register(Stadium)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
