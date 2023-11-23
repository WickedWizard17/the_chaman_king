"""
URL configuration for the_chaman_king project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('empleados.urls')),
    path('empleados/', include(('empleados.urls', 'empleados'), namespace='empleados')),
    path('proveedores/', include(('empleados.urls', 'empleados'), namespace='proveedores')),
    path('productos/', include(('empleados.urls', 'empleados'), namespace='productos')),

    path('', include('entrega2.urls')),
    path('entrega2/', include(('entrega2.urls', 'entrega2'), namespace='entrega2'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
