from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.login, name='login'),
    path("redirect", views.redirect, name='redirect'),
    path("register",views.register, name='register')
]