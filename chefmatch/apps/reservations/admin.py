from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chef', 'date', 'location', 'confirmed_at', 'canceled_at', 'completed_at')