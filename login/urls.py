from django.urls import path 
from . import views 
app_name = 'login'
urlpatterns = [
    path("signup", views.signUp, name='signup'),
    path("redirect", views.redirect, name='redirect'),
    path("signin",views.signIn, name='signin'),
    path("<str:token>/main/<str:fname>", views.index, name='login_index')
]