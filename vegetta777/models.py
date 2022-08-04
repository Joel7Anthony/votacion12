from django.db import models

# Create your models here.
class djmariio(models.Model):
    nombre        = models.CharField(max_length=20)
    canalYOUTUBE  = models.CharField(max_length=20)
    descripcion   = models.TextField(blank=True)
   
class clientes(models.Model):
    nombre    = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email     = models.EmailField()
    telefonoo      = models.CharField(max_length=7)
    
class Articulus(models.Model):
    nombre  = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio  = models.IntegerField()
    
class Pedidos(models.Model):
    numero     = models.IntegerField()
    fecha      = models.DateField()
    entregado  = models.BooleanField()