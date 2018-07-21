from django.shortcuts import render
from .models import Stadium, Game
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

def draw_map(request):
    #stadiums = Stadium.objects.all()
    #return render(request,'map/plot_map.html',{'stadiums':stadiums})
    return render(request, 'map/plot_map.html')


def filter_by_year(request):
    if request.method == 'GET':
        stadiums = Stadium.objects.filter(year=request.GET['data']).values()
        return JsonResponse({'dj_data':list(stadiums)})


def popup(request):
    if request.method == 'GET':
        if request.GET.get('stadium_name', 0) != 0:
            games = Game.objects.filter(stadium__name=request.GET['stadium_name']).values()
            print(games)
            return JsonResponse({'games_played': list(games)})

        obj = json.loads(request.GET['d'])
        for i in range(len(obj['dj_data'])):
            obj['dj_data'][i]['number_of_games'] = len(Game.objects.filter(stadium__name=str(obj['dj_data'][i]['name'])))
        return JsonResponse(obj)

def open_popup_window(request):
    return render(request,'map/popup.html')
