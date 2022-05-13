from rest_framework import serializers
from core.models import producto, subCategoria, Categoria

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['id_producto','Serie_producto', 'marca', 'codigo', 'nombre', 'fecha', 'valor', 'categoria']

class subCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategoria
        fields = ['id_subcategoria','nombre_subcategoria','categoria']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre_categoria']