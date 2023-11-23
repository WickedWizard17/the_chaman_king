from django import forms
from .models import Empleado, Proveedor, Producto

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields='__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields='__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
        widgets = {
            'caducidad': forms.DateInput(attrs={'type': 'date'})
        }