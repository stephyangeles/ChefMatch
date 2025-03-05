from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'users'