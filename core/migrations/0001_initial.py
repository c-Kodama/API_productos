# Generated by Django 3.2.4 on 2022-05-13 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=30, verbose_name='nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='subCategoria',
            fields=[
                ('id_subcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_subcategoria', models.CharField(max_length=30, verbose_name='nombre sub categoria')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('Serie_producto', models.CharField(max_length=30, verbose_name='serie_producto')),
                ('marca', models.CharField(max_length=40, verbose_name='marca')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre_producto')),
                ('fecha', models.DateField()),
                ('valor', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subcategoria')),
            ],
        ),
    ]