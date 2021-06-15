from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField

# Create your models here.

#TABLAS DE USUARIO

class Tipodocumento(models.Model):
    idDoc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Tipouser(models.Model):
    idTipo = models.AutoField(primary_key=True)
    clieAdmin = models.CharField(max_length=30)

    def __str__(self):
        return self.clieAdmin

class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    numdoc = models.CharField(max_length=20,null=True)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    password = models.CharField(max_length=20)
    tipouser = models.ForeignKey(Tipouser, on_delete=models.CASCADE, null =True)
    tipodoc = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombres

class Contacto(models.Model):
    idConct = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    asunto = CharField(max_length=20)
    mensaje = TextField(max_length=300) 

# TABLAS PARA DIRECCION

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreRegion

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna= models.CharField(max_length=30)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nombreComuna

class Direccion (models.Model):
    idDireccion = models.AutoField(primary_key=True)
    descDireccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,blank=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.descDireccion

#TABLAS DE COMPRA

class Carro(models.Model):
    idCarro = models.AutoField(primary_key=True)
    fechaCompra= models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    totalPago = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=False)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,blank=False)
    
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID')
    nombreCat = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreCat

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True,verbose_name='Codigo de produto')
    nombreProducto = models.CharField(max_length=100, blank=False)
    precio = models.IntegerField(blank=False)
    stock = models.IntegerField()
    imagen= models.ImageField(upload_to="productos", null= True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=False)
    
    def __str__(self):
        return self.nombreProducto

class Carritopro(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    carro =  models.ForeignKey(Carro,on_delete=models.CASCADE,blank=False, null = True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=False)
