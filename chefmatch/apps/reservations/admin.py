from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Call the model's clean method to enforce validation
        obj.full_clean()
        super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)