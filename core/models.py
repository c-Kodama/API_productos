from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=30, verbose_name='nombre categoria')

    def __str__(self):
        return self.nombre_categoria

class subCategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=30, verbose_name='nombre sub categoria')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_subcategoria

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    Serie_producto = models.CharField(max_length=30, verbose_name='serie_producto')
    marca = models.CharField(max_length=40, verbose_name='marca')
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100, verbose_name='nombre_producto')
    fecha = models.DateField()
    valor = models.IntegerField()
    categoria = models.ForeignKey(subCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre






