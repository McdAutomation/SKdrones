from django.urls import path
from . import views

app_name = 'visual'

urlpatterns = [
    # post views
    path('', views.draw_map, name='draw_map'),
    path('popup',views.popup,name='popup'),
    path('open_popup_window',views.open_popup_window,name='opened_popup'),
]