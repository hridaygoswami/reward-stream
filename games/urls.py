from django.urls import path 
from . import views 

app_name = 'games'

urlpatterns = [
    path("", views.index, name='Games_index'),
    path("stacker", views.stacker, name='Stacker'),
    path("stacker_3d", views.stacker_3d, name='Stacker_3d'),
    path("cube", views.cube, name='Cube'),
    path("tic_tac_toe", views.tic_tac_toe, name='Tic_tac_toe')
]