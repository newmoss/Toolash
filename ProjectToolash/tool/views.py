from django.shortcuts import redirect, render
from .models import Usuario,Tipodocumento,Direccion,Producto,Contacto
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

def login(request):
    return render(request,'tool/8login.html')

def emailpass(request):
    return render(request,'tool/9emailpass.html')

def password(request):
    return render(request,'tool/10password.html')


#---------------------------------------------------------------
def listado_usuarios(request):
    user = Usuario.objects.all() #Generando select * from tabla user
    contexto = {"usuarios":user}
    return render(request,'tool/11Listado_Usuarios.html',contexto)

def listado_producto(request):
    producto = Producto.objects.all() #Generando select * from tabla user

    contexto = {"productos":producto}
    return render(request,'tool/11Listado_Producto.html',contexto)

def listado_contacto(request):
    contacto = Contacto.objects.all() #Generando select * from tabla user
    contexto = {"contacto":contacto}
    return render(request,'tool/11Listado_Contacto.html',contexto)
#------------------------------------------------------------------



def modificar_cont(request,id):
    cont = Contacto.objects.get(idConct = id) #Generando select * from tabla user
    contexto = {"contacto":cont}
    return render(request,'tool/12modificar.html',contexto)

def modificar_usu(request,id):
    user = Usuario.objects.get(idUser = id) #Generando select * from tabla user
    contexto = {"user":user}
    return render(request,'tool/12modificar_usuario.html',contexto)


#-------------------------------------------------------------------------------#
def registrar(request):
    nombres = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    tel = request.POST['numero']
    passw = request.POST['password']
    Usuario.objects.create(nombres = nombres,apellidos = apellido,correo = email,telefono = tel, password = passw )
    messages.success(request,'Usuario registrado')
    return redirect('login')


#enviar contacto inicio
def contacto(request):
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    asunt = request.POST['asunto']
    msj = request.POST['mensaje']

    Contacto.objects.create(nombres = nombre,apellidos = apellido,correo = email, asunto = asunt, mensaje = msj )

    messages.success(request,'Mensaje enviado')
    return redirect('inicio')
#-------------------------------------------------------------------------------------------------------------
#DELETE


def eliminarus(request, id):
    delet = Usuario.objects.get(idUser = id)
    delet.delete()
    messages.success(request,'Eliminado exitosamente')

    return redirect('listadous')

def eliminarpr(request, id):
    produc = Producto.objects.get(codigo = id)
    produc.delete()
    messages.success(request,'Eliminado exitosamente')

    return redirect('listadopr')

def eliminarcon(request, id):
    contacto = Contacto.objects.get(idConct = id)
    contacto.delete()
    messages.success(request,'Eliminado exitosamente')

    return redirect('listadocon')


#-----------------------------------------------------------------------
def modificar_contacto(request):
    ide = request.POST['id']
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    asunt = request.POST['asunto']
    msj = request.POST['mensaje']

    contacto = Contacto.objects.get(idConct = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original
    contacto.nombres = nombre
    contacto.apellidos = apellido
    contacto.correo = email
    contacto.asunto = asunt
    contacto.mensaje = msj

    contacto.save()
    messages.success(request, 'Contacto Modificado')
    return redirect('listadocon')

def modificar_usuario(request):
    ide = request.POST['id']
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    numero = request.POST['numero']
    password = request.POST['password']

    user = Usuario.objects.get(idUser = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original
    user.nombres = nombre
    user.apellidos = apellido
    user.correo = email
    user.telefono = numero
    user.password = password

    user.save()
    messages.success(request, 'Usuario Modificado')
    return redirect('listadous')

