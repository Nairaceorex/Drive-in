from django.shortcuts import render
from  .models import *

def index(request):
    return render(request, "HomePage.html")
# Create your views here.

def Contact(request):
    return render(request, "Contact_Adress.html")

def film(request):
    Data = AllFilm.objects.all()
    k = 0
    Buff = []
    NewData = []
    for gr in Data:
        if k == 3:
            NewData.append(Buff)
            Buff = []
            k = 0
        Buff.append(gr)
        k += 1
    if k != 0: NewData.append(Buff)
    return render(request, "Films.html", {"Data": NewData})

def today(request):
    Data = Film.objects.all()
    k=0
    Buff=[]
    NewData=[]
    for gr in Data:
        if k==3:
            NewData.append(Buff)
            Buff=[]
            k=0
        Buff.append(gr)
        k+=1
    if k!=0: NewData.append(Buff)
    return render(request, "Cinema_today.html",{"Data":NewData})
