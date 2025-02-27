from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.name