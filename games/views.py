from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_games(request):
    return HttpResponse("Hello from games")

def stacker(request):
    # return HttpResponse("This is stacker")
    return render(request, 'stack.html')

def stack_3d(request):
    # return HttpResponse("This is stacker_3d")
    return render(request, 'stack_3d.html')

def cube(request):
    # return HttpResponse("This is cube")
    return render(request, 'cube.html')

def tic_tac_toe(request):
    # return HttpResponse("This is tic tac toe")
    return render(request, 'tic_tac_toe.html')