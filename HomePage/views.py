from django.shortcuts import render, get_object_or_404
from .models import *



def index(request):
    return render(request, "HomePage.html")
# Create your views here.
def theFilm(request,id):
    Film=AllFilm.objects.get(Key_Film=id)
    return render(request,"template_for_film.html",{"film":Film})

def Contact(request):
    return render(request, "Contact_Adress.html")



def film(request):
    Data = AllFilm.objects.all()
    return render(request, "Films.html", {"Data": Data})

def today(request):
    Data = AllFilm.objects.all()[0:3]
    return render(request, "Cinema_today.html",{"Data":Data})


