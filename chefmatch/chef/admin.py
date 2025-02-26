from django.contrib import admin
from .models import User, Specialty, Reservation, Chef, GeneralLedger

admin.site.register(User)
admin.site.register(Specialty)
admin.site.register(Reservation)
admin.site.register(Chef)
admin.site.register(GeneralLedger)
