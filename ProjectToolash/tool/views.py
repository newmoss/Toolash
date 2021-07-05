from django.db.models.aggregates import Aggregate, Sum
from django.db.models.query_utils import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Carro, Categoria, Tipouser, Usuario,Tipodocumento,Producto,Contacto,Carrito
from django.contrib.auth.hashers import make_password
from django.contrib import messages

class VistaRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'tool/0.html',{"form":form})
    def post(self,request):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                usuario = form.save()
                nombre_usuario = form.cleaned_data.get("username")
                messages.success(request, F"Bienvenido {nombre_usuario}")
                login(request,usuario)
                return redirect ('inicio')
            else:
                for msg in form.error_messages:
                    messages.error(request,form.error_messages[msg])


# Create your views here.
def inicio(request):
    contexto={}
    return render(request,'tool/1inicio.html',contexto)

def nosotros(request):
    contexto={}
    return render(request,'tool/2nosotros.html',contexto)

def servicios(request):
    contexto={}
    return render(request,'tool/3servicios.html',contexto)

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
    contexto={}
    return render(request,'tool/6tiendas.html',contexto)


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
    contexto={}
    return render(request,'tool/9emailpass.html',contexto)

def password(request):
    contexto={}
    return render(request,'tool/10password.html',contexto)

def ingresar_producto(request):
    cat = Categoria.objects.all()
    contexto = {"cat_m":cat}
    return render(request,'tool/Ingresar_producto.html',contexto)

def options(request):
    contexto={}    
    return render(request,'tool/options.html',contexto)



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

def perfil(request,id):
    tip = Tipodocumento.objects.all()
    userr = User.objects.all()
    user = Usuario.objects.get(numDoc = userr.id)
        #Generando select * from tabla user
    contexto={
        "user":user,
        "tip":tip,
        }
    return render(request,'tool/perfil.html',contexto)


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

    User.objects.create_user(id = rut,username= email,first_name = nombres,last_name = apellido,is_staff=0,is_active=1,email = email, password = passw)
    Usuario.objects.create(nombres = nombres,apellidos = apellido,correo = email,telefono = tel, numdoc = rut, tipodoc = tip_c , tipouser = user_c, password = passw )
    
    messages.success(request,'Usuario creado exitosamente!')
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
    #imagen_m = request.FILES['imagen']

    #IMAGEN PREDETERMINADA
    if request.FILES.get('imagen') == None:
        imagen_m = 'imagenproducto.png'
    else:
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
    dele = User.objects.get(id = delet.numdoc)
    dele.delete()
    messages.success(request,'Usuario eliminado exitosamente!')

    return redirect('listadous')

def eliminarpr(request, id):
    produc = Producto.objects.get(codigo = id)
    produc.delete()
    messages.success(request,'Producto eliminado exitosamente!')

    return redirect('listadopr')

def eliminarcon(request, id):
    contacto = Contacto.objects.get(idConct = id)
    contacto.delete()
    messages.success(request,'Eliminado exitosamente!')

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
    return redirect('listadocon')

def modificar_usuario(request):
    ide = request.POST['id']
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    numero = request.POST['numero']
    rut = request.POST['rut']
    tips = request.POST['tips']
    tipo = request.POST['tipo']
    password = request.POST['password']

    us = User.objects.get(id = rut)
    user = Usuario.objects.get(idUser = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original

    if user.nombres != nombre:
        user.nombres = nombre
        us.first_name = nombre
    
    if user.apellidos != apellido:
        user.apellidos = apellido
        us.last_name = apellido
    
    if user.correo != email:
        user.correo = email
        us.email = email
    
    if user.telefono != numero:
        user.telefono = numero

    if user.numdoc != rut:
        user.numdoc = rut
    
    if user.password != password:
        user.password = password
        us.password = make_password(password)
    #user.nombres = nombre
    #user.apellidos = apellido
    #user.correo = email
    #user.telefono = numero
    #user.numdoc = rut
    #user.password = password

    tipo_2 = Tipouser.objects.get(idTipo = tipo)
    tip_2 = Tipodocumento.objects.get(idDoc = tips)

    #if user.tipodoc != tip_2:
     #   user.tipdoc = tip_2
    
    if tipo_2.idTipo == 1:
        us.is_staff = 0
    if tipo_2.idTipo == 2:
        us.is_staff = 1
    if user.tipouser != tipo_2:
        user.tipouser = tipo_2
    user.tipodoc = tip_2
    #user.tipouser = tipo_2

    user.save()
    us.save()
    #messages.success(request, 'Usuario Modificado')
    return redirect('listadous')

def modificar_producto(request):
    ide = request.POST['id']
    nombre = request.POST['nombreProducto']
    precio = request.POST['precio']
    stock = request.POST['stock']
    #imagen_2 = request.FILES['imagen']
    cate = request.POST['cat']

    pro = Producto.objects.get(codigo = ide)#el registro original
    #comienzo a reemplazar los valores en ese registro original    
    
    #MANTENER IMAGEN SI ES VACIA
    if request.FILES.get('imagen') != None:
        pro.imagen= request.FILES['imagen']
    
    if pro.nombreProducto != nombre:
        pro.nombreProducto = nombre

    if pro.precio != precio:
        pro.precio = precio

    if pro.stock != stock:
        pro.stock = stock

    #pro.nombreProducto = nombre
    #pro.precio = precio
    #pro.stock = stock
    
    cat_m2 = Categoria.objects.get(idCategoria = cate)

    if pro.categoria != cat_m2:
        pro.categoria = cat_m2
    #pro.categoria = cat_m2

    pro.save()
    messages.success(request, 'Producto Modificado')
    return redirect('listadopr')


def modificar_perfil(request):
    ide = request.POST['id']
    nombre = request.POST['nombres']
    apellido = request.POST['apellidos']
    email = request.POST['email']
    numero = request.POST['numero']
    rut = request.POST['rut']
    password = request.POST['password']


    user = Usuario.objects.get(idUser = ide)#el registro original
    us = User.objects.get(id = rut)
    
    #comienzo a reemplazar los valores en ese registro original

    if user.nombres != nombre:
        user.nombres = nombre
        us.first_name = nombre
    
    if user.apellidos != apellido:
        user.apellidos = apellido
        us.last_name = apellido
    
    if user.correo != email:
        user.correo = email
        us.email = email
    
    if user.telefono != numero:
        user.telefono = numero

    if user.numdoc != rut:
        user.numdoc = rut
    
    if user.password != password:
        user.password = password
        us.password = make_password(password)
    #user.nombres = nombre
    #user.apellidos = apellido
    #user.correo = email
    #user.telefono = numero
    #user.numdoc = rut
    #user.password = password


    #user.tipodoc = tip_2
    #user.tipouser = tipo_2

    user.save()
    us.save()
    messages.success(request, 'Usuario Modificado')
    return redirect('inicio')


# CARRITO
@login_required
def carrito(request):
    userr = Usuario.objects.get(numdoc = request.user.id) #Generando select * from tabla user
    us2 = Usuario.objects.get(numdoc = request.user.id)
    carrito = Carrito.objects.filter(usuario = us2)
    total2 = Carrito.objects.filter(usuario = us2).count()
    if total2 == 0 :
        total = 0
        n = 0
    else: 
        total = Carrito.objects.filter(usuario = us2).aggregate(Sum('subtotal'))
        n = 1 
    context = {
        "carrito":carrito,
        "total":total,
        "n":n,
        "usu":userr
    }
    return render(request,'tool/carrito.html',context)

def agregar_carrito (request,id):
    can = request.POST['cant']
    pro = Producto.objects.get(codigo = id)
    usu = Usuario.objects.get(numdoc = request.user.id)
    subtotal = int(can) * int(pro.precio)
    Carrito.objects.create(cantidad = can, subtotal = subtotal, usuario = usu, producto = pro)
    messages.success(request,'Producto agregado al carrito!')
    return redirect('carrito')

def eliminarcarrito(request, id):
    contacto = Carrito.objects.get(idCarrito = id)
    contacto.delete()
    #messages.success(request,'Producto eliminado del carro!')

    return redirect('carrito')
def gracias (request):
    return render(request,'tool/gracias.html')

def vaciarcarrito(request):
    ru = Usuario.objects.get(numdoc = request.user.id)
    vac = Carrito.objects.filter(usuario = ru.idUser)
    vac.delete()
    return redirect('gracias')