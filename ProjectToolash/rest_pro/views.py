from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from .serializers import ProductoSerializador,UsuarioSerializador,ContactoSerializador
from tool.models import Producto,Usuario,Contacto


@csrf_exempt
@api_view(['GET','POST'])
def vista_producto(request):
    if request.method == 'GET':
        m = Producto.objects.all()
        serializer = ProductoSerializador(m, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializador(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','POST'])
def vista_usuario(request):
    if request.method == 'GET':
        m = Usuario.objects.all()
        serializer = UsuarioSerializador(m, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializador(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','POST'])
def vista_contacto(request):
    if request.method == 'GET':
        m = Contacto.objects.all()
        serializer = ContactoSerializador(m, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactoSerializador(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def datos_producto(request, id):
    try:
        m = Producto.objects.get(codigo = id)
    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializador(m)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializador(m, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        m.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)