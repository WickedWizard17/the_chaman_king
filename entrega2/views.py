from django.urls import reverse_lazy
from entrega2.models import Empleado, Proveedor, Producto
from .forms import EmpleadoForm, ProveedorForm, ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class EmpleadoListView(ListView):
    # 1. Nombre del template que va a utilizar
    template_name = 'entrega2/empleados/empleadosC_list.html'
    # 2. Nombre del modelo
    model = Empleado
    # 3. Nombre del contexto
    context_object_name = 'empleados'
    # 4. Paginación
    # paginate_by = 5

class EmpleadoCreateView(CreateView):
    template_name = 'entrega2/empleados/empleadosC_new.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('entrega2:empleadosC_list')

class EmpleadoUpdateView(UpdateView):
    template_name = 'entrega2/empleados/empleadosC_update.html'
    form_class = EmpleadoForm
    model=Empleado
    success_url = reverse_lazy('entrega2:empleadosC_list')

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name = 'entrega2/empleados/empleadosC_delete.html'
    success_url = reverse_lazy('entrega2:empleadosC_list')

class ProveedorListView(ListView):
    # 1. Nombre del template que va a utilizar
    template_name = 'entrega2/proveedores/proveedoresC_list.html'
    # 2. Nombre del modelo
    model = Proveedor
    # 3. Nombre del contexto
    context_object_name = 'proveedores'
    # 4. Paginación
    # paginate_by = 5

class ProveedorCreateView(CreateView):
    template_name = 'entrega2/proveedores/proveedoresC_new.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('entrega2:proveedoresC_list')

class ProveedorUpdateView(UpdateView):
    template_name = 'entrega2/proveedores/proveedoresC_update.html'
    form_class = ProveedorForm
    model=Proveedor
    success_url = reverse_lazy('entrega2:proveedoresC_list')

class ProveedorDeleteView(DeleteView):
    model=Proveedor
    template_name = 'entrega2/proveedores/proveedoresC_delete.html'
    success_url = reverse_lazy('entrega2:proveedoresC_list')

class ProductoListView(ListView):
    # 1. Nombre del template que va a utilizar
    template_name = 'entrega2/productos/productosC_list.html'
    # 2. Nombre del modelo
    model = Producto
    # 3. Nombre del contexto
    context_object_name = 'productos'
    # 4. Paginación
    # paginate_by = 5

class ProductoCreateView(CreateView):
    template_name = 'entrega2/productos/productosC_new.html'
    form_class = ProductoForm
    success_url = reverse_lazy('entrega2:productosC_list')

class ProductoUpdateView(UpdateView):
    template_name = 'entrega2/productos/productosC_update.html'
    form_class = ProductoForm
    model=Producto
    success_url = reverse_lazy('entrega2:productosC_list')

class ProductoDeleteView(DeleteView):
    model=Producto
    template_name = 'entrega2/productos/productosC_delete.html'
    success_url = reverse_lazy('entrega2:productosC_list')