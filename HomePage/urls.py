from django.urls import path
from . import views
app_name = 'HomePage'
urlpatterns = [
    path('', views.index, name='index'),
path("today", views.today, name='today'),
path("film", views.film, name='film'),
path("Contact", views.Contact, name='Contact'),
]

