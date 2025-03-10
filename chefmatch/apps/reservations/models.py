from datetime import datetime
from django.db import models
from apps.chefs.models import Chef
from apps.users.models import User
from django.core.exceptions import ValidationError

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.user} with {self.chef} on {self.date}"

    def clean(self):
        """
        Validate that the chef is not already reserved on the same day.
        """
        if not self.date:
            raise ValidationError("Date is required.")

        existing_reservation = Reservation.objects.filter(
            chef=self.chef,
            date__date=self.date.date()  # Compare only the date part (ignoring time)
        ).exclude(id=self.id)  # Exclude the current instance if updating

        if existing_reservation.exists():
            raise ValidationError("This chef is already reserved on the selected day.")

    def save(self, *args, **kwargs):
        """
        Call full_clean to enforce validation before saving.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'reservations'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'