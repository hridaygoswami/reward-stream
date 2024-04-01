from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello from games")

def stacker(request):
    # return HttpResponse("Stacker")
    return render(request, "stacker.html")

def stacker_3d(request):
    # return HttpResponse("Stacker 3d")
    return render(request, "stacker_3d.html")

def cube(request):
    # return HttpResponse("The Cube")
    return render(request, "cube.html")

def tic_tac_toe(request):
    # return HttpResponse("Tic Tac Toe")
    return render(request, "tic_tac_toe.html")