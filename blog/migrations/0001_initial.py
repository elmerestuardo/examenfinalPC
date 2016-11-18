# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('isbn', models.IntegerField()),
                ('titulo', models.CharField(max_length=150)),
                ('autor', models.ForeignKey(to='blog.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion_prop', models.DateField()),
                ('fecha_devolucion_real', models.DateField()),
                ('libro', models.ManyToManyField(to='blog.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('dpi', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='prestamos',
            name='usuario',
            field=models.ForeignKey(to='blog.Usuarios'),
        ),
        migrations.AddField(
            model_name='libro',
            name='año',
            field=models.ForeignKey(to='blog.Year'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(to='blog.Editorial'),
        ),
        migrations.AddField(
            model_name='libro',
            name='pais',
            field=models.ForeignKey(to='blog.Pais'),
        ),
    ]
