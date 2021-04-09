from django.urls import path
from . import views

app_name = 'Client'
urlpatterns = [
    path('/reg', views.reg, name='reg'),
    path('/login', views.login, name='login'),

]
