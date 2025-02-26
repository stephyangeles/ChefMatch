from django.db import models

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class Chef(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

class GeneralLedger(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

