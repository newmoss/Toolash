from django.contrib import admin
from .models import Producto,Categoria,Carritopro,Usuario,Tipodocumento,Tipouser,Contacto,Region,Comuna,Direccion,Carro

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tipodocumento)
admin.site.register(Tipouser)
admin.site.register(Contacto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Carro)
admin.site.register(Carritopro)
admin.site.register(Categoria)
admin.site.register(Producto)


