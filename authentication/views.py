from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello from authentication")
    return redirect("account_login")