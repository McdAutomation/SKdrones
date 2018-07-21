from django.urls import path
from . import views

app_name = 'visual'

urlpatterns = [
    # post views
    path('', views.draw_map, name='draw_map'),
    path('popup',views.popup,name='popup'),
    path('filter_by_year',views.filter_by_year,name='filter_by_year'),
    path('open_popup_window',views.open_popup_window,name='opened_popup_window'),
]