from . import views
from django.urls import path

urlpatterns = [
    path('', views.listar_empleados, name='home'),
    path('empleados/', views.listar_empleados, name='empleados_list'),
    path('empleados-new/', views.agregar_empleado, name='empleados_new'),
    path('empleados-edit/<id_emp>/', views.edit_empleado, name='empleados_edit'),
    path('empleados-delete/<id_emp>/', views.eliminar_empleado, name='empleado_delete'),

    path('proveedores/', views.listar_proveedores, name='proveedores_list'),
    path('proveedores-new/', views.agregar_proveedor, name='proveedores_new'),
    path('proveedores-edit/<id_pro>/', views.edit_proveedor, name='proveedores_edit'),
    path('proveedores-delete/<id_pro>/', views.eliminar_proveedor, name='proveedores_delete'),

    path('productos/', views.listar_productos, name='productos_list'),
    path('productos-new/', views.agregar_producto, name='productos_new'),
    path('productos-edit/<codigo>/', views.edit_producto, name='productos_edit'),
    path('productos-delete/<id>/', views.eliminar_producto, name='productos_delete'),
]
