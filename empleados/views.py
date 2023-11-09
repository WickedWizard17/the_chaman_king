from django.shortcuts import render, get_object_or_404, redirect
from empleados.models import Empleado, Producto, Proveedor
from .forms import EmpleadoForm, ProductoForm, ProveedorForm
from django.contrib import messages


# //////////////////// Vistas para EMPLEADOS ////////////////////
def listar_empleados(request):
    # Consulta a la BD: SELECT * FROM categorias
    empleados = Empleado.objects.all()
    data = {
        'empleados': empleados
    }
    return render(request, 'empleados/empleados/empleados_list.html', data)


def agregar_empleado(request):
    data = {
        'form': EmpleadoForm()
    }
    # Verificar si el usuario ya presiono el boton de envio, valida la informacion por metodo POST
    if request.method == 'POST':
        # Formulario con los datos enviados
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado agregado!')
            return redirect(to='empleados:empleados_list')
        else:
            data['form'] = formulario  # Esto lo que hace es regresar el formulario con los errores
    return render(request, 'empleados/empleados/empleados_new.html', data)


def edit_empleado(request, id_emp):
    empleado = get_object_or_404(Empleado, id_emp=id_emp)
    data = {
        'form': EmpleadoForm(instance=empleado)
    }
    # Si el usuario dijo ya dijo que si, POST
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado actualizado!')
            return redirect(to='empleados:empleados_list')
        # Si no es valido el formulario
        data['form'] = formulario
    return render(request, 'empleados/empleados/empleados_edit.html', data)


def eliminar_empleado(request, id_emp):
    empleado = get_object_or_404(Empleado, id_emp=id_emp)
    empleado.delete()
    messages.success(request, 'Empleado eliminado!')
    return redirect(to='empleados:empleados_list')


# //////////////////// Vistas para PROVEEDOR ////////////////////
def listar_proveedores(request):
    # Consulta a la BD: SELECT * FROM categorias
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'empleados/proveedores/proveedores_list.html', data)


def agregar_proveedor(request):
    data = {
        'form': ProveedorForm()
    }
    # Verificar si el usuario ya presiono el boton de envio, valida la informacion por metodo POST
    if request.method == 'POST':
        # Formulario con los datos enviados
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Proveedor agregado!')
            return redirect(to='proveedores:proveedores_list')
        else:
            data['form'] = formulario  # Esto lo que hace es regresar el formulario con los errores
    return render(request, 'empleados/proveedores/proveedores_new.html', data)


def edit_proveedor(request, id_pro):
    proveedor = get_object_or_404(Proveedor, id_pro=id_pro)
    data = {
        'form': ProveedorForm(instance=proveedor)
    }
    # Si el usuario dijo ya dijo que si, POST
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Proveedor actualizado!')
            return redirect(to='proveedores:proveedores_list')
        # Si no es valido el formulario
        data['form'] = formulario
    return render(request, 'empleados/proveedores/proveedores_edit.html', data)


def eliminar_proveedor(request, id_pro):
    proveedor = get_object_or_404(Proveedor, id_pro=id_pro)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado!')
    return redirect(to='proveedores:proveedores_list')


# //////////////////// Vistas para PRODUCTOS ////////////////////
def listar_productos(request):
    # Consulta a la BD: SELECT * FROM categorias
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'empleados/productos/productos_list.html', data)


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    # Verificar si el usuario ya presiono el boton de envio, valida la informacion por metodo POST
    if request.method == 'POST':
        # Formulario con los datos enviados
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto agregado!')
            return redirect(to='productos:productos_list')
        else:
            data['form'] = formulario  # Esto lo que hace es regresar el formulario con los errores
    return render(request, 'empleados/productos/productos_new.html', data)


def edit_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    data = {
        'form': ProductoForm(instance=producto)
    }
    # Si el usuario dijo ya dijo que si, POST
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto actualizado!')
            return redirect(to='productos:productos_list')
        # Si no es valido el formulario
        data['form'] = formulario
    return render(request, 'empleados/productos/productos_edit.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado!')
    return redirect(to='productos:productos_list')
