from django.db import models
from apps.specialties.models import Specialty

class Chef(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'chefs'