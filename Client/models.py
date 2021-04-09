from django.db import models


class Client(models.Model):
    Firstname = models.CharField(max_length=100, verbose_name='Имя')
    Surname = models.CharField(max_length=100, verbose_name='Фамилия')
    Date = models.DateField(verbose_name='Дата рождения',null=True)
    Phone = models.CharField(max_length=100,verbose_name='Телефон')
    Password = models.IntegerField(verbose_name='Пароль')
    Email = models.CharField(max_length=100, verbose_name='Почта')

    def __str__(self):
        return self.Surname
