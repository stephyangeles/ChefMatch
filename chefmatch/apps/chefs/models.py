from django.db import models
from apps.reservations.models import Reservation
from apps.specialties.models import Specialty

class Chef(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name
