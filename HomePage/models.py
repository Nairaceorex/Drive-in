from django.db import models
import PIL

class Film(models.Model):
    Key_Film = models.BigAutoField(primary_key=True, verbose_name='Код фильма')
    Name = models.CharField(max_length=100, verbose_name='Название')
    Year = models.IntegerField(verbose_name='Год')
    Description = models.TextField(verbose_name='Описание')
    Genre = models.CharField(max_length=50, verbose_name='Жанр')
    Icon = models.ImageField(verbose_name='Иконка')

    def __str__(self):
        return self.Name

class AllFilm(models.Model):
    Key_Film = models.BigAutoField(primary_key=True, verbose_name='Код фильма')
    Name = models.CharField(max_length=100, verbose_name='Название')
    Year = models.IntegerField(verbose_name='Год')
    Description = models.TextField(verbose_name='Описание')
    Genre = models.CharField(max_length=50, verbose_name='Жанр')
    Icon = models.ImageField(verbose_name='Иконка')

    def __str__(self):
        return self.Name

# Create your models here.
