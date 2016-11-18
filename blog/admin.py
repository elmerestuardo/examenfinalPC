from django.contrib import admin
from .models import Editorial, Libro, Autor, Pais, Year, Prestamos, Usuarios

admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Pais)
admin.site.register(Year)
admin.site.register(Prestamos)
admin.site.register(Usuarios)

# Register your models here.
