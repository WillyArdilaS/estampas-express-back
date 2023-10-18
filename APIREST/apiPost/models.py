from django.db import models

# Create your models here.

class usuario(models.Model):
    tipoID = models.CharField(max_length=2)
    numeroID = models.BigIntegerField()
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    genero = models.CharField(max_length=10)
    rol = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=80)
