from django.urls import path
from rest_productos.views import lista_categorias

urlpatterns = [
    path('categorias/', lista_categorias, name='lista de categorias'),
]