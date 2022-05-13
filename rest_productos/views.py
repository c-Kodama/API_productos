from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt #crea un token
from core.models import producto, subCategoria, Categoria
from .serializers import productoSerializer, subCategoriaSerializer, CategoriaSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def lista_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)