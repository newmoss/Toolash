from django.urls import path
from rest_pro.views import vista_producto,vista_usuario,vista_contacto,datos_producto
urlpatterns = [
    path('listapro',vista_producto,name="listapro"),
    path('listaus',vista_usuario,name="listaus"),
    path('listacon',vista_contacto,name="listacon"),
    path('datospro/<id>',datos_producto,name="datospro"),


]