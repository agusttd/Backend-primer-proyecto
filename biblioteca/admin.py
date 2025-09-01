from django.contrib import admin
from .models import Biblioteca, Nacionalidad, Lector, Autor, Categoria, Libro, Prestamo, Direccion, Comuna

# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Nacionalidad)
admin.site.register(Lector)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Direccion)
admin.site.register(Comuna)