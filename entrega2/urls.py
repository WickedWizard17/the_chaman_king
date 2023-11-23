from . import views
from django.urls import path

urlpatterns = [
    # Rutas de Empleados
    path('empleadosC-list/', views.EmpleadoListView.as_view(), name="empleadosC_list"),
    path('empleadosC-new/', views.EmpleadoCreateView.as_view(), name="empleadosC_new"),
    path('empleadosC-update/<pk>', views.EmpleadoUpdateView.as_view(), name="empleadosC_update"),
    path('empleadosC-delete/<pk>', views.EmpleadoDeleteView.as_view(), name="empleadosC_delete"),

    # Rutas de Proveedores
    path('proveedoresC-list/', views.ProveedorListView.as_view(), name="proveedoresC_list"),
    path('proveedoresC-new/', views.ProveedorCreateView.as_view(), name="proveedoresC_new"),
    path('proveedoresC-update/<pk>', views.ProveedorUpdateView.as_view(), name="proveedoresC_update"),
    path('proveedoresC-delete/<pk>', views.ProveedorDeleteView.as_view(), name="proveedoresC_delete"),

    # Rutas de Productos
    path('productosC-list/', views.ProductoListView.as_view(), name="productosC_list"),
    path('productosC-new/', views.ProductoCreateView.as_view(), name="productosC_new"),
    path('productosC-update/<pk>', views.ProductoUpdateView.as_view(), name="productosC_update"),
    path('productosC-delete/<pk>', views.ProductoDeleteView.as_view(), name="productosC_delete"),
]
