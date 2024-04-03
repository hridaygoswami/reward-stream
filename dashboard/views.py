from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    user = request.user
    # return HttpResponse(f"Hello from dashboard {user}")
    return render(request, "profile.html", {
        "user":user,
        "cPage":"profile"
    })

def earning(request):
    return render(request, "earning.html")

def surveys(request):
    # return HttpResponse("This is surveys")
    return render(request, "surveys.html")

def password(request):
    # return HttpResponse("This is password")
    return render(request, "password.html")

def withdrawal(request):
    # return HttpResponse("This is withdrawal")
    return render(request, "withdrawal.html")




# earning internal links
def games(request):
    return render(request, "games.html")

def simple_earning(request):
    return render(request, "simple_earning.html")

def mega_rewards(request):
    return render(request, "mega_rewards.html")

def terms_conditions(request):
    return render(request, "terms_conditions.html")


# profile internal links
def profile_ui(request):
    user = request.user
    return render(request, "profile_ui.html", {
        "user":user
    })

def profile_graph(request):
    return render(request, "profile_graph.html")