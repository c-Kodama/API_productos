from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt #crea un token
from core.models import producto, subCategoria, Categoria
from .serializers import productoSerializer, subCategoriaSerializer, CategoriaSerializer

# Create your views here.

#Listar Categorias
@csrf_exempt
@api_view(['GET'])
def lista_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

#Obtener pruductos
@csrf_exempt    
@api_view(['GET'])
def lista_productos(request):
    if request.method == 'GET':
        productos = producto.objects.all()
        serializer = productoSerializer(productos, many=True)
        return Response(serializer.data)

#obtener un producto
@csrf_exempt
@api_view(['GET', 'POST'])
def obtenerProducto(request):
    if request.method == 'POST':
        productoCodigo = producto.objects.get(codigo=request.data.get("codigo"))
        serializer = productoSerializer(productoCodigo)
        return Response(serializer.data)