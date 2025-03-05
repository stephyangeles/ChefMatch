from django.db import models
from apps.specialties.models import Specialty
from apps.reservations.models import Reservation

class Chef(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def is_available(self, date):
        existing_reservation = Reservation.objects.filter(
            chef=self,
            date=date.date()
        )
        return not existing_reservation.exists()

    class Meta:
        db_table = 'chefs'