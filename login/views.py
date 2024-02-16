from django.shortcuts import render
from django import forms
from .models import Login

# Create your views here.
def login(request):
    return render(request, "login.html")

def redirect(request, p):
    # formResponse = request.POST
    print(request.path)
    print(p)
    # print(formResponse['email'], formResponse['password'])
    # f = Login(email=formResponse['email'], password=formResponse['password'])
    # f.save()
    return render(request, "redirect.html")

def register(request):
    print(request.POST)
    return render(request, "registration.html")