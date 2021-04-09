from django.shortcuts import render, redirect
from  .forms import RegForm
from .models import Client
# Create your views here.
def reg(request):
    if request.method=="POST":
        Firstname=request.POST.get("Firstname")
        Surname=request.POST.get("Surname")
        DateBirth = request.POST.get("DateBirth")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Phone = request.POST.get("Phone")

        newClient=Client(Firstname=Firstname,Surname=Surname,Date=DateBirth,Phone=Phone,Password=Password,Email=Email)
        newClient.save()
        return render(request,"success.html")
    return render(request,"reg.html",{"form":RegForm})

def login(request):
    if request.method == "POST":
        try:
            account = Client.objects.get(Email=request.POST.get('EmailLogin'),
                                          Password=request.POST.get('PasswordLogin'))
            request.session['id'] = account.id
            request.session['name'] = account.Firstname+" "+account.Surname
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        redirect(request.META.get('HTTP_REFERER'))