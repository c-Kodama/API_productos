from django.contrib import admin
from .models import producto, subCategoria, Categoria

# Register your models here.

admin.site.register(producto)
admin.site.register(subCategoria)
admin.site.register(Categoria)