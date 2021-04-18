from django.urls import path
from . import views
app_name = 'HomePage'
urlpatterns = [
    path('', views.index, name='index'),
path("today", views.today, name='today'),
path("film", views.film, name='film'),
path("Contact", views.Contact, name='Contact'),
path("theFilm\<int:id>",views.theFilm, name='theFilm'),
path("GetCinema", views.GetCinema, name='GetCinema'),
    path("getplace",views.getplace,name='getplace'),
path("getdate",views.getdate,name='getdate'),
    path("successticket", views.successticket, name='successticket'),
path("successed", views.successed, name='successed'),

]

