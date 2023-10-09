from django.db import models

# Create your models here.

class register(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    numId = models.BigIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=80)

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=80)