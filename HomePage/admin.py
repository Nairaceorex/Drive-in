from django.contrib import admin
from .models import AllFilm

@admin.register(AllFilm)
class AllFilmAdmin(admin.ModelAdmin):
    list_display = ['Key_Film','Icon', 'Name', 'Year', 'Genre','Mark','price']
    search_fields = ['Name', 'Key_Film']

# Register your models here.
