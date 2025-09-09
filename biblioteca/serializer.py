from rest_framework import serializers
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Categoria, Libro, Prestamo 

class Nacionalidad_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Nacionalidad
        fields = '_all_'

class Autor_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Autor
        fields = '_all_'

class Comuna_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Comuna
        fields = '_all_'

class Direccion_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Direccion
        fields = '_all_'

class Biblioteca_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Biblioteca
        fields = '_all_'

class Lector_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Lector
        fields = '_all_'

class Categoria_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Categoria
        fields = '_all_'

class Libro_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Libro
        fields = '_all_'

class Prestamo_Serializer(serializers.ModelSerilizer):
    class Meta:
        model = Prestamo 
        fields = '_all_'