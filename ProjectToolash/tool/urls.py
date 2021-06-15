from django.contrib import admin
from django.urls import path, include
from .views import  buscar_pro, eliminarcon, eliminarpr, eliminarus, ingresar_producto, inicio, listado_contacto, listado_producto, listado_usuarios, modificar_cont, modificar_contacto, modificar_pro, modificar_producto, modificar_usu, modificar_usuario, mostrar_producto, nosotros, producto,servicios,servtec,seguridad,venta,tiendas,registro,login,emailpass,password,registrar,contacto

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('servicios', servicios, name="servicios"),
    path('servtec', servtec, name="servtec"),
    path('seguridad', seguridad, name="seguridad"),
    path('venta', venta, name="venta"),
    path('mostrarproducto/<id>', mostrar_producto, name="mostrarproducto"), #PERFIL DE PRODUCTO
    path('tiendas', tiendas, name="tiendas"),
    path('registro', registro, name="registro"),
    path('login', login, name="login"),
    path('emailpass', emailpass, name="emailpass"),
    path('password', password, name="password"),
    path('buscar_pro', buscar_pro, name="buscar_pro"),
     path('ingresar_producto', ingresar_producto, name="ingresar_producto"),
    
    #LISTADOS

    path('listadous', listado_usuarios, name="listadous"),
    path('listadopr', listado_producto, name="listadopr"),
    path('listadocon', listado_contacto, name="listadocon"),
    
    #MODIFICACIONES

    path('modificar_cont/<id>', modificar_cont, name="modificar_cont"),
    path('modificar_contacto', modificar_contacto, name="modificar_contacto"),

    path('modificar_usu/<id>', modificar_usu, name="modificar_usu"),
    path('modificar_usuario', modificar_usuario, name="modificar_usuario"),
    
    path('modificar_pro/<id>', modificar_pro, name="modificar_pro"),
    path('modificar_producto', modificar_producto, name="modificar_producto"),
    
    #DELETE

    path('eliminarus/<id>', eliminarus, name="deleteus"),
    path('eliminarpr/<id>', eliminarpr, name="deletepr"),
    path('eliminarcon/<id>', eliminarcon, name="deletecon"),

    #REGISTRAR

    path('registrar', registrar, name="registrar"),#registrar usuario
    path('contacto', contacto, name="contacto"),#registrar contacto 
    path('producto', producto, name="producto"),#registrar usuario



]