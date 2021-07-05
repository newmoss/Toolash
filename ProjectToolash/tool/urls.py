from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import  VistaRegistro, agregar_carrito,carrito, eliminarcarrito, eliminarcon, eliminarpr, eliminarus, gracias, ingresar_producto, inicio, listado_contacto, listado_producto, listado_usuarios, login_view, logout_view, modificar_cont, modificar_contacto, modificar_perfil, modificar_pro, modificar_producto, modificar_usu, modificar_usuario, mostrar_producto, nosotros, options, perfil, producto,servicios,servtec,seguridad, vaciarcarrito,venta,tiendas,registro,emailpass,password,registrar,contacto

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('servicios', servicios, name="servicios"),
    path('servtec', servtec, name="servtec"),
    path('seguridad', seguridad, name="seguridad"),
    path('venta', venta, name="venta"),
    path('carrito',carrito,name="carrito"),
    path('carritoo/<id>',agregar_carrito,name="carritoo"),
    path('gracias',login_required(gracias),name="gracias"),
    path('mostrarproducto/<id>', mostrar_producto, name="mostrarproducto"), #PERFIL DE PRODUCTO
    path('tiendas', tiendas, name="tiendas"),
    path('registro', registro, name="registro"),
    path('reg',VistaRegistro,name="reg"),
    path('login/',LoginView.as_view(template_name='tool/8login.html'), name="login"),
    path('logout',logout_view,name="logout"),


    path('sesion',login_view,name="sesion"),
    path('emailpass', emailpass, name="emailpass"),
    path('password', password, name="password"),
    path('options', login_required(options), name="options"),
    path('ingresar_producto', login_required(ingresar_producto), name="ingresar_producto"),
    
    #LISTADOS

    path('listadous',  login_required(listado_usuarios), name="listadous"),
    path('listadopr',  login_required(listado_producto), name="listadopr"),
    path('listadocon',  login_required(listado_contacto), name="listadocon"),
    
    #MODIFICACIONES

    path('modificar_cont/<id>', login_required(modificar_cont), name="modificar_cont"),
    path('modificar_contacto', modificar_contacto, name="modificar_contacto"),

    path('modificar_usu/<id>', login_required(modificar_usu), name="modificar_usu"),
    path('modificar_usuario', modificar_usuario, name="modificar_usuario"),
    
    path('modificar_pro/<id>', login_required(modificar_pro), name="modificar_pro"),
    path('modificar_producto', modificar_producto, name="modificar_producto"),

    path('perfil/<id>', perfil, name="perfil"),
    path('modificar_perfil', modificar_perfil, name="modificar_perfil"),


    
    #DELETE

    path('eliminarus/<id>', eliminarus, name="deleteus"),
    path('eliminarpr/<id>', eliminarpr, name="deletepr"),
    path('eliminarcon/<id>', eliminarcon, name="deletecon"),
    path('eliminarcarrito/<id>', eliminarcarrito, name="eliminarcarrito"),
    path('vaciar',vaciarcarrito,name="vaciar"),

    #REGISTRAR

    path('registrar', registrar, name="registrar"),#registrar usuario
    path('contacto', contacto, name="contacto"),#registrar contacto 
    path('producto', producto, name="producto"),#registrar usuario



]