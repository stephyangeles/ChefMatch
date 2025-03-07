from django.db import models
from django.contrib.auth.models import User 
from apps.chef.models import Chef

<<<<<<< HEAD

=======
>>>>>>> 29e395885ea19eca3288f93d41400ed20ff449cf
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Reservation {self.id} - {self.user.name} - {self.chef.name}"

    class Meta:
        db_table = 'reservations'