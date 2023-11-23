from django.contrib import admin
from entrega2.models import Producto, Proveedor, Empleado

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Empleado)