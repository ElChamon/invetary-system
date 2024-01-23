from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    superuser = models.BooleanField()
    dni = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=255)
