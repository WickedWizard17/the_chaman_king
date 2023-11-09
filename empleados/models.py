from django.db import models

# Create your models here.


# Modelo de empleados
class Empleado(models.Model):
    id_emp = models.PositiveIntegerField(unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=40, unique=True, blank=False, null=False)
    puesto = models.CharField(max_length=20, blank=False, null=False)
    horario = models.CharField(max_length=20, blank=False, null=False)
    sueldo = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    telefono = models.CharField(max_length=10, unique=True, blank=False, null=False)
    correo = models.CharField(max_length=30, unique=True, blank=False, null=False)
    contrasena = models.CharField(max_length=30, blank=False, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Modelo de proveedores
class Proveedor(models.Model):
    id_pro = models.PositiveIntegerField(unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=40, unique=True, blank=False, null=False)
    ciudad = models.CharField(max_length=40, blank=False, null=False)
    cp = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.CharField(max_length=10, unique=True, blank=False, null=False)
    correo = models.CharField(max_length=30, unique=True, blank=False, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Modelo de productos
class Producto(models.Model):
    codigo = models.CharField(max_length=30, unique=True, blank=False, null=False)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=40, unique=True, blank=False, null=False)
    descripcion = models.TextField(max_length=150, blank=True, null=True)
    existencia = models.IntegerField(default=0, blank=False, null=False)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    caducidad = models.CharField(max_length=10, blank=False, null=False)
    cura = models.TextField(max_length=100, blank=True, null=True)
    presentacion = models.CharField(max_length=20, blank=False, null=False)
    habilitado = models.BooleanField(default=True)
    # imagen = models.ImageField()

    def __str__(self):
        return self.nombre
