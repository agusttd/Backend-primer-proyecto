from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from .serializer import NacionalidadSerializer as nacser, Autor_Serializer as autser, Comuna_Serializer as comser, Direccion_Serializer as dirser, Biblioteca_Serializer as bibser, Lector_Serializer as lecser, Categoria_Serializer as catser, Libro_Serializer as libser, Prestamo_Serializer as preser
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Categoria, Libro, Prestamo 
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication


# Create your views here.
@login_required    
def pagina_inicio(request):
    return render(request, 'biblioteca/inicio.html')

class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Nacionalidad.objects.all()
    serializer_class = nacser

class NacionalidadListView(ListView):
    authentication_classes = [SessionAuthentication]
    model = Nacionalidad
    template_name = 'biblioteca/nacionalidad_list.html'

class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Autor.objects.all()
    serializer_class = autser

class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Comuna.objects.all()
    serializer_class = comser

class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Direccion.objects.all()
    serializer_class = dirser

class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Biblioteca.objects.all()
    serializer_class = bibser
    

class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Lector.objects.all()
    serializer_class = lecser

class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Categoria.objects.all()
    serializer_class = catser

class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Libro.objects.all()
    serializer_class = libser

class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Prestamo.objects.all()
    serializer_class = preser