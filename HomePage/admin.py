from django.contrib import admin
from .models import Film,AllFilm
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['Key_Film','Icon', 'Name', 'Year', 'Genre', 'Description']
    search_fields = ['Name', 'Key_Film']

@admin.register(AllFilm)
class AllFilmAdmin(admin.ModelAdmin):
    list_display = ['Key_Film','Icon', 'Name', 'Year', 'Genre', 'Description']
    search_fields = ['Name', 'Key_Film']

# Register your models here.
