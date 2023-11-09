from django import forms

from empleados.models import Empleado, Producto, Proveedor


class EmpleadoForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Empleado
        # fields = ['clave', 'nombre', 'descripcion', 'descuento', 'estado']
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Proveedor
        # fields = ['clave', 'nombre', 'descripcion', 'descuento', 'estado']
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Producto
        # fields = ['clave', 'nombre', 'descripcion', 'descuento', 'estado']
        fields = '__all__'


