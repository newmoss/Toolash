from django.contrib import admin
from django.urls import path, include
from .views import inicio, nosotros,servicios,servtec,seguridad,venta,tiendas,registro,login,emailpass,password,producto,listado,registrar,contacto

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
    
    
    path('listado', listado, name="listado"),

    path('registrar', registrar, name="registrar"),
    path('contacto', contacto, name="contacto"),

]