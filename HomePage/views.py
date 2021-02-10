from django.shortcuts import render

def index(request):
    return render(request, "HomePage.html")
# Create your views here.
