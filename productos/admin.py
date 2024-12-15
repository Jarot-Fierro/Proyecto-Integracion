from django.contrib import admin

# Register your models here.

from .models import Producto,ProductoEliminado

admin.site.register(Producto)
admin.site.register(ProductoEliminado)