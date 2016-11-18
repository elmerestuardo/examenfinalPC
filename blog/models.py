from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Year(models.Model):
    y = models.IntegerField()

    def __str__(self):
        return self.y

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
    isbn = models.IntegerField()
    titulo = models.CharField(max_length=150)
    #portada = models.ImageField()
    autor = models.ForeignKey(Autor)
    editorial = models.ForeignKey(Editorial)
    pais = models.ForeignKey(Pais)
    año = models.ForeignKey(Year)

    def __str__(self):
        return self.titulo

class Usuarios(models.Model):
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    dpi = models.CharField(max_length=25)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellidos, self.dpi,)

class Prestamos(models.Model):
    fecha_prestamo = models.DateField()
    fecha_devolucion_prop = models.DateField()
    fecha_devolucion_real = models.DateField()
    libro = models.ManyToManyField(Libro)
    usuario = models.ForeignKey(Usuarios)

    def __str__(self):
        return '%s %s %s' % (self.fecha_prestamo, self.fecha_devolucion_prop, self.fecha_devolucion_real,)
