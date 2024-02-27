from django.shortcuts import render
from django import forms
from .models import SignIn, SignUp
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# from django.urls import reverse

# @ensure_csrf_cookie
# Create your views here.
def signIn(request):
    return render(request, "signIn.html")

def redirect(request):
    data = request.POST
    if len(data) == 7:
        print("On signup with t&c approved")
    elif len(data) == 6:
        print("On signup without t&c approved")
    # print(len(data))
    return render(request, 'redirect.html')

def signUp(request):
    return render(request, "signUp.html")


def index(request, token, fname):
    # return HttpResponse(token)
    return render(request, "login_index.html", {
        "tk":token,
        "f":fname
    })