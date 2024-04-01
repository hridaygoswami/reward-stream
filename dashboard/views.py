from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    user = request.user
    # return HttpResponse(f"Hello from dashboard {user}")
    return render(request, "index.html", {
        "user":user
    })

def earning(request):
    user = request.user
    return render(request, "earning.html", {
        "user":user
    })