from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
class Zapato(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.IntegerField()
    color = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    