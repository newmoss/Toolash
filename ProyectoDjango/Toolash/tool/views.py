from django.shortcuts import render

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