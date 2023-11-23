from django.db import models


# Create your models here.

class Empleado(models.Model):
    PUESTOS = (
        ('ADMINISTRADOR', 'ADMINISTRADOR'),
        ('CAJERO', 'CAJERO'),
        ('MOSTRADOR', 'MOSTRADOR')
    )
    HORARIOS = (
        ('MATUTINO', 'MATUTINO'),
        ('VESPERTINO', 'VESPERTINO')
    )

    id_emp = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    puesto = models.CharField(max_length=15, blank=False, null=False, choices=PUESTOS)
    horario = models.CharField(max_length=10, blank=False, null=False, choices=HORARIOS)
    sueldo = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    telefono = models.CharField(max_length=10, unique=True, blank=False, null=False)
    correo = models.CharField(max_length=30, unique=True, blank=False, null=False)
    contrasena = models.CharField(max_length=30, blank=False, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Modelo de proveedores
class Proveedor(models.Model):
    id_pro = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    ciudad = models.CharField(max_length=40, blank=False, null=False)
    cp = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.CharField(max_length=10, unique=True, blank=False, null=False)
    correo = models.CharField(max_length=30, unique=True, blank=False, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    PRESENTACION = (
        ('COMPRIMIDO', 'COMPRIMIDO'),
        ('CÁPSULA', 'CÁPSULA'),
        ('TABLETA', 'TABLETA'),
        ('JARABE', 'JARABE'),
        ('INYECCIÓN', 'INYECCIÓN'),
        ('SUPOSITORIOS', 'SUPOSITORIOS'),
        ('GOTAS', 'GOTAS'),
        ('AEROSOL', 'AEROSOL'),
        ('PARCHE', 'PARCHE'),
        ('INHALADOR', 'INHALADOR'),
        ('POMADA', 'POMADA'),
        ('GEL', 'GEL'),
        ('SOLUCIÓN', 'SOLUCIÓN'),
        ('BEBIBLES', 'BEBIBLES'),
        ('SUPLEMENTO', 'SUPLEMENTO')
    )
    codigo = models.CharField(primary_key=True, max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=50, unique=True, blank=False, null=False)
    descripcion = models.TextField(max_length=150, blank=True, null=True)
    existencia = models.IntegerField(default=0, blank=False, null=False)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    caducidad = models.DateField(blank=False, null=False)
    cura = models.TextField(max_length=100, blank=True, null=True)
    presentacion = models.CharField(max_length=20, blank=False, null=False, choices=PRESENTACION)
    habilitado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productosC/', blank=True, null=True)

    def __str__(self):
        return self.nombre
