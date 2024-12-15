"""
URL configuration for web_inventario project.

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
from django.urls import path
from web import views
from django.shortcuts import render
from django.conf.urls import handler404

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('usuarios/login',views.login_view,name='login_view'),
    path('usuarios/logout',views.logout_view,name='logout_view'),
    path('actualizar_producto/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('index',views.index,name='index'),
    path('gestion/productos',views.gestion_productos,name='gestion_productos'),
    path('reportes/productos',views.reportes,name='reportes'),
    path('descargar/reportes',views.descargar_reportes,name='descargar_reportes'),
    path('admin/', admin.site.urls),
]
handler404 = 'web.views.error_404'