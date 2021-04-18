from django.contrib import admin
from .models import Account, Ticket, Cinema


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Surname','Date','Phone','Password','Email']
    search_fields = ['Surname', 'Age']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','NumPark','Date','Time','Film','Cost']
    search_fields = ['NumPark', 'Date']

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Address','NumSeats']
    search_fields = ['NumSeats', 'Address']