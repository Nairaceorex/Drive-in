from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


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

def cart(request):
   forms=CartAddProductForm
   return render(request, "detail.html",{'forms':forms})




def product_detail(request, id, slug):
    product = get_object_or_404(AllFilm, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'HomePage/templates/template_for_film.html', {'product': product, 'cart_product_form': cart_product_form})
