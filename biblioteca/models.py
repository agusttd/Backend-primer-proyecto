from django.db import models

# Create your models here.
class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    nombre = models.CharField(max_length=70, null=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)
    calle = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=255, null=False)
    nacionalidad = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, null=True)
    pseudonimo = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    web = models.URLField(null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=350, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField(null=False)
    copias = models.IntegerField(null=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250, null=False)
    rut = models.IntegerField(null=False)
    dig_verificador = models.CharField(max_length=1, null=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    id_direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE, null=True)
    habilitado = models.BooleanField(default=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=False)
    fecha_entrega = models.DateTimeField(auto_now=True,null=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
