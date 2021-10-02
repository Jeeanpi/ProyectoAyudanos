from django.contrib.auth import logout
from django.urls import path
from .views import index ,servicios, registro, contratarPlan,\
agregar_Cliente, listar_Cliente, modificar_Cliente, eliminar_Cliente, agregar_Mascota,\
listar_Mascota, modificar_Mascota, eliminar_Mascota, misMascotas, miPerfil

urlpatterns = [
    path('', index, name="index"),
    path('servicios/', servicios, name="servicios"),
    path('registro/', registro, name="registro"),
    path('contratarPlan/', contratarPlan, name="contratarPlan"),
    path('agregar-Cliente/', agregar_Cliente, name="agregar_cliente"),
    path('listar-Cliente/', listar_Cliente, name="listar_cliente"),
    path('modificar-Cliente/<id>/', modificar_Cliente, name="modificar_cliente"),
    path('eliminar-Cliente/<id>/', eliminar_Cliente, name="eliminar_cliente"),
    path('agregar-Mascota/', agregar_Mascota, name="agregar_mascota"),
    path('listar-Mascota/', listar_Mascota, name="listar_mascota"),
    path('modificar-Mascota/<id>/', modificar_Mascota, name="modificar_mascota"),
    path('eliminar-Mascota/<id>/', eliminar_Mascota, name="eliminar_mascota" ),
    path('mis-Mascotas/', misMascotas, name="mis_mascotas"),
    path('miPerfil/', miPerfil, name="mi_perfil")
    
]