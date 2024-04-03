from django.urls import path 
from . import views 

app_name = 'dashboard'

urlpatterns = [
    # navbar urls
    path("", views.index, name='Dashboard_index'),
    path("earning", views.earning, name='Dashboard_earning'),
    path("surveys", views.surveys, name="Dashboard_surveys"),
    path("surveys", views.surveys, name="Dashboard_surveys"),
    path("password", views.password, name="Dashboard_password"),
    path("withdrawal", views.withdrawal, name="Dashboard_withdrawal"),
    path("terms_conditions", views.terms_conditions, name='Dashboard_terms_conditions'),

    
    #earning internal urls
    path("earning/games", views.games, name='Dashboard_games'),
    path("earning/simple_earning", views.simple_earning, name="Dashboard_simple_earning"),
    path("earning/mega_rewards", views.mega_rewards, name='Dashboard_mega_rewards'),

    # profile internal urls
    path("profile_ui", views.profile_ui, name='Dashboard_profile_ui'),
    path("profile_graph", views.profile_graph, name="Dashboard_profile_graph")
]