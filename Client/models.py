from django.db import models
from HomePage.models import *


class Account(models.Model):
    Firstname = models.CharField(max_length=100, verbose_name='Имя')
    Surname = models.CharField(max_length=100, verbose_name='Фамилия')
    Date = models.DateField(verbose_name='Дата рождения',null=True)
    Phone = models.CharField(max_length=100,verbose_name='Телефон')
    Password = models.IntegerField(verbose_name='Пароль')
    Email = models.CharField(max_length=100, verbose_name='Почта')

    def __str__(self):
        return self.Surname


class Cinema(models.Model):
    Name = models.CharField(verbose_name="Наименование",max_length=100)
    Address = models.CharField(verbose_name="Адрес",max_length=100)
    NumSeats = models.PositiveSmallIntegerField(verbose_name="Количество мест")

    def __str__(self):
        return str(self.id)


class Ticket(models.Model):
    Date = models.DateField(verbose_name="Дата")
    Time = models.TimeField(verbose_name="Время")
    NumPark = models.PositiveSmallIntegerField(verbose_name="Номер парковки")
    Cost = models.PositiveSmallIntegerField(verbose_name="Цена")
    Cinema = models.ForeignKey(Cinema,  on_delete=models.CASCADE, verbose_name=u"Кинотеатр")
    Film = models.ForeignKey(AllFilm, on_delete=models.CASCADE, verbose_name="Фильм")
    FullnameClient = models.CharField(max_length=303, verbose_name="ФИО клиента")
    PhoneNumberClient = models.CharField(verbose_name="Номер телефона клиента",max_length=100)
    EmailClient = models.EmailField(verbose_name="Email клиента")

    def __str__(self):
        return self.NumPark

