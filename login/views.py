from django.shortcuts import render
from django import forms
from .models import SignIn, SignUp
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

# Create your views here.
def signIn(request):
    return render(request, "signIn.html")

def redirect(request):
    data = request.POST
    csrf_token = data["csrfmiddlewaretoken"]
    if len(data)==3:
        email = data['email']
        password = data['password']
        print("Login page", email, password, csrf_token)
    elif len(data)==6:
        fullName = data['fname']
        age = data['age']
        email = data['email']
        password = data['password']
        confirmPassword = data['cPassword']
        if (password == confirmPassword):
            print("Everythin is fine")
            print("Register Page", fullName, age, email, password, confirmPassword)
            # return render(request, "redirect.html")
            return HttpResponseRedirect(f"{csrf_token}/main/{fullName}")
        else:
            print("Everything is not fine")
            # return reverse("signup")
            return HttpResponseRedirect("signup")
            # return HttpResponse("Passwords not same")

def signUp(request):
    return render(request, "signUp.html")


def index(request, token, fname):
    # return HttpResponse(token)
    return render(request, "index.html", {
        "tk":token,
        "f":fname
    })