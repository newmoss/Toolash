from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Categoria, Tipouser, Usuario,Tipodocumento,Producto,Contacto
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'tool/1inicio.html')

def nosotros(request):
    return render(request,'tool/2nosotros.html')

def servicios(request):
    return render(request,'tool/3servicios.html')

def servtec(request):
    queryset = request.GET.get("search") 
    print(queryset)
    produc = Producto.objects.filter(nombreProducto = True)
    if queryset:
        produc = Producto.objects.filter(
            Q(nombreProducto__icontains= queryset)
        ).distinct()#BUSCAR

    num_produ=Producto.objects.all()
    num_produ=Producto.objects.filter(categoria = 3)
    context={'num_prod':num_produ,"productos":produc}
    return render(request,'tool/5.3servtec.html',context)

def seguridad(request):
    queryset = request.GET.get("search") 
    print(queryset)
    produc = Producto.objects.filter(nombreProducto = True)
    if queryset:
        produc = Producto.objects.filter(
            Q(nombreProducto__icontains= queryset)
        ).distinct()#BUSCAR

    num_produ=Producto.objects.all()
    num_produ=Producto.objects.filter(categoria = 2)
    context={'num_prod':num_produ,"productos":produc}
    return render(request,'tool/5.2seguridad.html',context)

def venta(request):
    queryset = request.GET.get("search") 
    print(queryset)
    produc = Producto.objects.filter(nombreProducto = True)
    if queryset:
        produc = Producto.objects.filter(
            Q(nombreProducto__icontains= queryset)
        ).distinct()#BUSCAR

    num_produ=Producto.objects.all()
    num_produ=Producto.objects.filter(categoria = 1)
    context={'num_prod':num_produ,"productos":produc}
    return render(request,'tool/5venta.html',context)

def mostrar_producto(request,id):
    pro = Producto.objects.get(codigo = id) #Generando select * from tabla user
    contexto = {"productos":pro}
    return render(request,'tool/5.1producto.html',contexto)

def lol4(request):
    return render(request,'tool/lol4.html')


def tiendas(request):
    return render(request,'tool/6tiendas.html')


def registro(request):
    tip = Tipodocumento.objects.all()
    #tip = Tipodocumento.objects.filter(idDoc = 1)

    user = Tipouser.objects.all()
    user = Tipouser.objects.filter(idTipo = 1)
    contexto = {"tipodoc":tip,"user":user}
    return render(request,'tool/7registro.html',contexto)

#INICIO SESION

def login_view(request):
    u = request.POST['username']
    c = request.POST['password']

    user = authenticate(username = u, password = c)

    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('inicio')
        else:
            messages.error(request,'Usuario Inactivo')
    else:
        messages.error(request,'Usuario y/o contraseña incorrecta')

    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('inicio')
#-----------------------------------------------------------
def emailpass(request):
    return render(request,'tool/9emailpass.html')

def password(request):
    return render(request,'tool/10password.html')

def ingresar_producto(request):
    cat = Categoria.objects.all()
    contexto = {"cat_m":cat}
    return render(request,'tool/Ingresar_producto.html',contexto)

def buscar_pro(request):
    queryset = request.GET.get("search") 
    print(queryset)
    produc = Producto.objects.filter(nombreProducto = True)
    if queryset:
        produc = Producto.objects.filter(
            Q(nombreProducto__icontains= queryset)
        ).distinct()
    contexto={"productos":produc}
    return render(request,'tool/buscar_pro.html',contexto)



#------------------------LISTADOS----------------------------

def listado_usuarios(request):
    queryset = request.GET.get("search") 
    print(queryset)
    us = Usuario.objects.filter(nombres= True)
    if queryset:
        us = Usuario.objects.filter(
            Q(nombres__icontains= queryset)
        ).distinct()

    user = Usuario.objects.all() #Generando select * from tabla user
    
    contexto = {"usuarios":user,"usuario":us}
    return render(request,'tool/11Listado_Usuarios.html',contexto)

def listado_producto(request):
    queryset = request.GET.get("search") 
    print(queryset)
    produc = Producto.objects.filter(nombreProducto = True)
    if queryset:
        produc = Producto.objects.filter(
            Q(nombreProducto__icontains= queryset)
        ).distinct()
    
    producto = Producto.objects.all() #Generando select * from tabla user

    contexto = {"productos":producto,"producto":produc}
    return render(request,'tool/11Listado_Producto.html',contexto)


def listado_contacto(request):
    queryset = request.GET.get("search") 
    print(queryset)
    cont = Contacto.objects.filter(nombres = True)
    if queryset:
        cont = Contacto.objects.filter(
            Q(nombres__icontains= queryset)
        ).distinct()

    contacto = Contacto.objects.all() #Generando select * from tabla user
    
    contexto = {"contacto":contacto,"contactos":cont}
    return render(request,'tool/11Listado_Contacto.html',contexto)



#----------------------------VISTAS MODIFICAR---------------------------


def modificar_cont(request,id):
    cont = Contacto.objects.get(idConct = id) #Generando select * from tabla user
    contexto = {"contacto":cont}
    return render(request,'tool/12modificar.html',contexto)

def modificar_usu(request,id):
    tip = Tipodocumento.objects.all()
    tipo = Tipouser.objects.all()
    user = Usuario.objects.get(idUser = id) #Generando select * from tabla user
    contexto = {"user":user,"tip":tip,"tipo":tipo}
    return render(request,'tool/12modificar_usuario.html',contexto)

def modificar_pro(request,id):
    cat = Categoria.objects.all()
    pro = Producto.objects.get(codigo = id) #Generando select * from tabla user
    contexto = {"producto":pro ,"cat":cat}
    return render(request,'tool/12modificar_producto.html',contexto)



#-------------------------------ENVIAR FORMULARIOS A BD--------------------------------#

def registrar(request):
    nombres = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    tel = request.POST['numero']
    rut = request.POST['rut']
    tip = request.POST['tipodoc']
    user = request.POST['user']
    passw = request.POST['password']


    user_c = Tipouser.objects.get(idTipo = user)
    tip_c = Tipodocumento.objects.get(idDoc = tip)
    
    Usuario.objects.create(nombres = nombres,apellidos = apellido,correo = email,telefono = tel, numdoc = rut, tipodoc = tip_c , tipouser = user_c, password = passw )
    messages.success(request,'Usuario registrado')
    return redirect('login')


def contacto(request):
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    asunt = request.POST['asunto']
    msj = request.POST['mensaje']

    Contacto.objects.create(nombres = nombre,apellidos = apellido,correo = email, asunto = asunt, mensaje = msj )

    messages.success(request,'Mensaje enviado')
    return redirect('inicio')

def producto(request):
    nombre_m = request.POST['nombreProducto']
    precio_m = request.POST['precio']
    stock_m = request.POST['stock']
    cat_m = request.POST['cat']
    imagen_m = request.FILES['imagen']

    cat_c = Categoria.objects.get(idCategoria= cat_m)

    Producto.objects.create(nombreProducto = nombre_m ,precio = precio_m ,stock = stock_m , imagen = imagen_m , categoria = cat_c )

    messages.success(request,'Producto Registrado')
    return redirect('ingresar_producto')
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


#----------------------------MODIFICAR ACCION------------------------------
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
    rut = request.POST['rut']
    tip = request.POST['tip']
    tipo = request.POST['tipo']
    password = request.POST['password']

    user = Usuario.objects.get(idUser = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original
    user.nombres = nombre
    user.apellidos = apellido
    user.correo = email
    user.telefono = numero
    user.numdoc = rut
    user.password = password

    tipo_2 = Tipouser.objects.get(idTipo = tipo)
    tip_2 = Tipodocumento.objects.get(idDoc = tip)
    user.tipodoc = tip_2
    user.tipouser = tipo_2

    user.save()
    messages.success(request, 'Usuario Modificado')
    return redirect('listadous')

def modificar_producto(request):
    ide = request.POST['id']
    nombre = request.POST['nombreProducto']
    precio = request.POST['precio']
    stock = request.POST['stock']
    imagen_2 = request.FILES['imagen']
    cate = request.POST['cat']
    

    pro = Producto.objects.get(codigo = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original
    pro.codigo = ide
    pro.nombreProducto = nombre
    pro.precio = precio
    pro.stock = stock
    pro.imagen.url= imagen_2
    
    cat_m2 = Categoria.objects.get(idCategoria = cate)
    pro.categoria = cat_m2

    pro.save()
    messages.success(request, 'Producto Modificado')
    return redirect('listadopr')

