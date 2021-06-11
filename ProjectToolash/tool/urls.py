from django.contrib import admin
from django.urls import path, include
from .views import  eliminarcon, eliminarpr, eliminarus, inicio, listado_contacto, listado_producto, listado_usuarios, modificar_cont, modificar_contacto, modificar_usu, modificar_usuario, nosotros,servicios,servtec,seguridad,venta,tiendas,registro,login,emailpass,password,producto,registrar,contacto

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('servicios', servicios, name="servicios"),
    path('servtec', servtec, name="servtec"),
    path('seguridad', seguridad, name="seguridad"),
    path('venta', venta, name="venta"),
    path('tiendas', tiendas, name="tiendas"),
    path('registro', registro, name="registro"),
    path('login', login, name="login"),
    path('emailpass', emailpass, name="emailpass"),
    path('password', password, name="password"),
    path('producto', producto, name="producto"),
    
    path('listadous', listado_usuarios, name="listadous"),
    path('listadopr', listado_producto, name="listadopr"),
    path('listadocon', listado_contacto, name="listadocon"),
    
    path('modificar_cont/<id>', modificar_cont, name="modificar_cont"),
    path('modificar_contacto', modificar_contacto, name="modificar_contacto"),

    path('modificar_usu/<id>', modificar_usu, name="modificar_usu"),
    path('modificar_usuario', modificar_usuario, name="modificar_usuario"),
    #delete
    path('eliminarus/<id>', eliminarus, name="deleteus"),
    path('eliminarpr/<id>', eliminarpr, name="deletepr"),
    path('eliminarcon/<id>', eliminarcon, name="deletecon"),

    path('registrar', registrar, name="registrar"),#registrar usuario
    path('contacto', contacto, name="contacto"),#registrar contacto 
   

]