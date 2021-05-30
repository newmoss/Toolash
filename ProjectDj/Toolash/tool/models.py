from django.db import models


# Create your models here.


    
class Carritopro(models.Model):
    idCarrito = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID')
    nombreCat = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreCat

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo de prudcto')
    nombreProducto = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(blank=False)
    stock = models.IntegerField()
    imagen= models.CharField(max_length=50)
    producto = models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nombreProducto