from django import forms

from empleados.models import Empleado, Producto, Proveedor


class EmpleadoForm(forms.ModelForm):
    TIPO=(
        (0,"TIPO A"),
        (1,"TIPO B"),
        (2,"TIPO C")
    )
    horario = forms.DateField(
        widget=forms.Select(choices=TIPO)
    )
    # horario = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=TIPO,
    # )
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


