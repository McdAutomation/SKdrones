from django.shortcuts import render
from .models import Stadium, Game
from django.http import HttpResponse
# Create your views here.

def draw_map(request):
    stadiums = Stadium.objects.all()
    return render(request,'map/plot_map.html',{'stadiums':stadiums})


def popup(request):
    print(request.GET['data'])
    if request.method == 'GET':
        arr = Game.objects.filter(stadium__name=str(request.GET['data']))

        return HttpResponse(len(arr))

def open_popup_window(request):
    return render(request,'map/popup.html')
