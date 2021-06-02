from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, NullBooleanField

# Create your models here.


#TABLAS DE USUARIO

class User(models.Model):
    idUser = models.IntegerField(primary_key=True)
    correo = models.CharField(max_length=30)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres

class Tipodocumento(models.Model):
    numDoc = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.descripcion

class Tipouser(models.Model):
    idTip = models.IntegerField(primary_key=True)
    clieAdmin = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.clieAdmin

class Contacto(models.Model):
    idConct = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    asunto = CharField(max_length=20)
    mensaje = CharField(max_length=300)



# TABLAS PARA DIRECCION

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True)
    nombreRegion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreRegion

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True)
    nombreComuna= models.CharField(max_length=30)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nombreComuna


class Direccion (models.Model):
    idDireccion = models.IntegerField(primary_key=True)
    descDireccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.descDireccion


#TABLAS DE COMPRA

class Carritopro(models.Model):
    idCarrito = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

class Carro(models.Model):
    idCarro = models.IntegerField(primary_key=True)
    fechaCompra= models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    totalPago = models.IntegerField()
    carritopro =  models.ForeignKey(Carritopro,on_delete=models.CASCADE,blank=False)
    

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID')
    nombreCat = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreCat

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo de produto')
    nombreProducto = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(blank=False)
    stock = models.IntegerField()
    imagen= models.ImageField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=False)
    carritopro = models.ForeignKey(Carritopro,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nombreProducto

