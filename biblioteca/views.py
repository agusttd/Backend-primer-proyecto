from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer as nacser, Autor_Serializer as autser, Comuna_Serializer as comser, Direccion_Serializer as dirser, Biblioteca_Serializer as bibser, Lector_Serializer as lecser, Categoria_Serializer as catser, Libro_Serializer as libser, Prestamo_Serializer as preser
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Categoria, Libro, Prestamo 


# Create your views here.

def pagina_inicio(request):
    return render(request, 'biblioteca/inicio.html')

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = nacser

class NacionalidadListView(ListView):
    model = Nacionalidad
    template_name = 'biblioteca/nacionalidad_list.html'

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = autser

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = comser

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = dirser

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = bibser

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = lecser

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = catser

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = libser

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = preser