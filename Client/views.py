from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from  .forms import RegForm
from .models import Account,Ticket
# Create your views here.
def reg(request):
    if request.method=="POST":
        Firstname=request.POST.get("Firstname")
        Surname=request.POST.get("Surname")
        DateBirth = request.POST.get("DateBirth")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Phone = request.POST.get("Phone")

        newClient=Account(Firstname=Firstname,Surname=Surname,Date=DateBirth,Phone=Phone,Password=Password,Email=Email)
        newClient.save()
        return render(request,"success.html")
    return render(request,"reg.html",{"form":RegForm})


def login(request):
    if request.method == "POST":
        try:
            account = Account.objects.get(Email=request.POST.get('EmailLogin'),
                                          Password=request.POST.get('PasswordLogin'))
            request.session['id'] = account.id
            request.session['name'] = account.Firstname+" "+account.Surname
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        redirect(request.META.get('HTTP_REFERER'))


def logout(request):
    if 'id' in request.session: del request.session['id']
    if 'name' in request.session: del request.session['name']
    return redirect(request.META.get('HTTP_REFERER'))


def profile(request):
    if 'id' in request.session:
        acc = Account.objects.get(id=request.session['id'])
        return render(request, 'profile.html', {'account': acc})
    else:
        return render(request, 'NotLogin.html')

def print(request):
    ticket=Ticket.objects.get(id=request.GET.get('id'))
    html=render_to_string('printT.html',{'data':ticket})
    return HttpResponse(html)