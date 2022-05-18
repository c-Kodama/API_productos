from django.urls import path
from rest_productos.views import lista_categorias, lista_productos, obtenerProducto

urlpatterns = [
    path('categorias/', lista_categorias, name='lista de categorias'),
    path('productos/', lista_productos, name='lista de productos'),
    path('producto/', obtenerProducto, name='obtener un producto por codigo'),

]