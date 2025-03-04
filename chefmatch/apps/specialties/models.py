from django.db import models

class Specialty(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'specialty'

class Chef(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'chef'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'

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