from typing import ContextManager
from django.shortcuts import redirect, render
from .models import User,Tipodocumento,Direccion,Producto,Contacto
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'tool/1inicio.html')

def nosotros(request):
    return render(request,'tool/2nosotros.html')

def servicios(request):
    return render(request,'tool/3servicios.html')

def servtec(request):
    return render(request,'tool/5.3servtec.html')

def seguridad(request):
    return render(request,'tool/5.2seguridad.html')

def producto(request):
    return render(request,'tool/5.1producto.html')

def venta(request):
    return render(request,'tool/5venta.html')

def lol4(request):
    return render(request,'tool/lol4.html')


def tiendas(request):
    return render(request,'tool/6tiendas.html')


def registro(request):
    return render(request,'tool/7registro.html')

def registrar(request):
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    tel = request.POST['numero']
    rut = request.POST['rut']
    dir= request.POST['direccion']
    passw = request.POST['password']

    User.objects.create(nombres = nombre,apellidos = apellido,correo = email, telefono = tel, password = passw )
    Tipodocumento.objects.create(numDoc = rut)
    Direccion.objects.create(descDireccion = dir)

    messages.success(request,'Usuario registrado')
    return redirect('login')

def login(request):
    return render(request,'tool/8login.html')

def emailpass(request):
    return render(request,'tool/9emailpass.html')

def password(request):
    return render(request,'tool/10password.html')

def listado(request):
    user = User.objects.all() #Generando select * from tabla user
    producto = Producto.objects.all()
    contexto = {"usuarios":user,"productos":producto}
    return render(request,'tool/11Listado.html',contexto)

def contacto(request):
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    asunt = request.POST['asunto']
    msj = request.POST['mensaje']

    Contacto.objects.create(nombres = nombre,apellidos = apellido,correo = email, asunto = asunt, mensaje = msj )

    messages.success(request,'Mensaje enviado')
    return redirect('venta')