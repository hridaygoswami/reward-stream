from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.index_games, name='index_games'),
    path("stacker", views.stacker, name='stacker'),
    path("stack_3d", views.stack_3d, name='stack_3d'),
    path("cube", views.cube, name='cube'),
    path("tic_tac_toe", views.tic_tac_toe, name='tic_tac_toe')
]