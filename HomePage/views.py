from datetime import datetime

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
    film = AllFilm.objects.get(Key_Film=request.session['idFilm'])
    day = film.GetSchedule()[int(request.GET.get('date'))]
    date = day['date']
    time = day['schedule'][int(request.GET.get('time'))]
    request.session['date'] = date
    request.session['time'] = time
    Data=Cinema.objects.get(id=request.session['idCinema'])

    Data.placedata=[]
    DATE = f'{datetime.today().year}-{date.split(".")[1]}-{date.split(".")[0]}'
    print(DATE)
    tickets = Ticket.objects.filter(Date__year=datetime.today().year,
                                    Date__month=date.split(".")[1],
                                    Date__day=date.split(".")[0],
                                    Cinema=Data, Film=film, Time=time)
    for i in range(Data.NumSeats):
        try:
            tickets.get(NumPark=i + 1)
            Data.placedata.append(False)
        except:
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
    film = AllFilm.objects.get(Key_Film=idfilm)
    date=request.session['date']
    time=request.session['time']
    place=request.session['place']=request.GET.get('place')
    cinema= Cinema.objects.get(id=idcinema)
    html = render_to_string('Note/Success.html', {'Film': film,'Place':place,'Date':date,'Time': time,'Cinema':cinema})

    return HttpResponse(html)

def successed(request):
    idfilm = request.session['idFilm']
    idcinema = request.session['idCinema']
    date = request.session['date'].split('.')
    time = request.session['time']
    place = request.session['place']
    account=Account.objects.get(id=request.session['id'])
    today = datetime.today()
    film = AllFilm.objects.get(Key_Film=idfilm)
    cinema = Cinema.objects.get(id=idcinema)
    newticket=Ticket(Date= f'{today.year}-{date[1]}-{date[0]}', Time=time, NumPark=place,
                     Cost=film.price, Cinema=cinema, Film=film,
                     FullnameClient=account.Firstname +' '+ account.Surname,
                     PhoneNumberClient=account.Phone, EmailClient=account.Email)
    newticket.save()
    html=render_to_string('Note/PrintTicket.html',{'id':newticket.id})
    return HttpResponse(html)