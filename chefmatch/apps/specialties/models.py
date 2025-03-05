from django.db import models
from apps.reservations.models import Reservation

class Specialty(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'specialty'
        

class GeneralLedger(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"Ledger {self.id} - Reservation {self.reservation.id}"

    class Meta:
        db_table = 'general_ledger'