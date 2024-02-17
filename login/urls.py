from django.urls import path 
from . import views 

urlpatterns = [
    path("signup", views.signUp, name='signup'),
    path("redirect", views.redirect, name='redirect'),
    path("signin",views.signIn, name='signip'),
    path("<str:token>/main/<str:fname>", views.index, name='index')
]