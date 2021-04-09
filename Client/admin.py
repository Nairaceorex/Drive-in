from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Surname','Date','Phone','Password','Email']
    search_fields = ['Surname', 'Age']