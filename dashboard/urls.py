from django.urls import path 
from . import views 

app_name = 'dashboard'

urlpatterns = [
    path("", views.index, name='Dashboard_index'),
    path("earning", views.earning, name='Dashboard_earning')
]