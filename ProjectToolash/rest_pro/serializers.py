from django.db.models.base import Model
from tool.models import Producto,Usuario,Contacto
from rest_framework import serializers

class ProductoSerializador(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['codigo','nombreProducto','precio','stock','imagen','categoria']

class UsuarioSerializador(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['idUser','nombres','apellidos','numdoc','correo','telefono','password','tipouser','tipodoc']

class ContactoSerializador(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = ['idConct','nombres','apellidos','correo','asunto','mensaje']