from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField(default = 0)
    stock = models.IntegerField(default = 0)
    fecha_compra = models.DateField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.nombre_producto
    
class ProductoEliminado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    fecha_compra = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    fecha_eliminacion = models.DateTimeField(default=timezone.now)  # Campo para la fecha de eliminación

    def __str__(self):
        return self.nombre_producto