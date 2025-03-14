from django.db import models
from apps.reservations.models import Reservation

class Ledger(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"GeneralLedger {self.id} - Reservation {self.reservation_id}"

    class Meta:
        db_table = 'general_ledger'