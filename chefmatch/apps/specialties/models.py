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