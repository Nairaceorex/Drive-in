from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import *
from Client.models import Cinema, Ticket, Account


def index(request):
    return render(request, "HomePage.html")


def theFilm(request,id):
    Film=AllFilm.objects.get(Key_Film=id)
    return render(request,"template_for_film.html",{"film":Film})


def GetCinema(request):
    request.session['idFilm'] = request.GET.get('id')

    cinema = Cinema.objects.all()
    print('lol')
    html = render_to_string('Note/CinemaList.html', {'Data': cinema})
    return HttpResponse(html)


def Contact(request):
    return render(request, "Contact_Adress.html")


def film(request):
    Data = AllFilm.objects.all()
    return render(request, "Films.html", {"Data": Data})


def today(request):
    Data = AllFilm.objects.all()[0:3]
    return render(request, "Cinema_today.html",{"Data":Data})

def getplace(request):

    request.session['date'] = request.GET.get('date')
    request.session['time'] = request.GET.get('time')
    Data=Cinema.objects.get(id=request.session['idCinema'])
    Data.placedata=[]
    for i in range(Data.NumSeats):
        Data.placedata.append(True)
    html=render_to_string('Note/Place.html', {'Data': Data})
    return HttpResponse(html)

def getdate(request):
    id=request.session['idFilm']
    request.session['idCinema']=request.GET.get('id')
    film=AllFilm.objects.get(Key_Film=id)
    html = render_to_string('Note/Date.html', {'Data': film})
    return HttpResponse(html)

def successticket(request):
    idfilm=request.session['idFilm']
    idcinema=request.session['idCinema']
    date=request.session['date']
    time=request.session['time']
    place=request.session['place']=request.GET.get('place')
    film = AllFilm.objects.get(Key_Film=idfilm)
    cinema= Cinema.objects.get(id=idcinema)
    html = render_to_string('Note/Success.html', {'Film': film,'Place':place,'Date':date,'Time': time,'Cinema':cinema})

    return HttpResponse(html)

def successed(request):
    idfilm = request.session['idFilm']
    idcinema = request.session['idCinema']
    date = request.session['date']
    time = request.session['time']
    place = request.session['place']
    account=Account.objects.get(id=request.session['id'])

    film = AllFilm.objects.get(Key_Film=idfilm)
    cinema = Cinema.objects.get(id=idcinema)
    newticket=Ticket(Date=date,Time=time,NumPark=place,Cost=film.price,Cinema=cinema,Film=film,FullnameClient=account.Firstname + account.Surname, PhoneNumberClient=account.Phone,EmailClient=account.Email)
    newticket.save()
    html='<h1 aling="center">Спасибо, приятного просмотра!</h1>'
    return HttpResponse(html)