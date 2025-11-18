from django.test import TestCase
from .models import Nacionalidad, Autor, Comuna

# Create your tests here.
class TestNacionalidad(TestCase):
    def test_objeto_nacionalidad(self):
        nacionalidad = Nacionalidad.objects.create(pais='Chile', nacionalidad='Chileno')
        self.assertEqual(nacionalidad.pais, 'Chile')
        self.assertEqual(nacionalidad.nacionalidad, 'Chileno')
        self.assertEqual(Nacionalidad.objects.filter(pais='Chile').exists(),True)

#class TestAutor(TestCase):
 #   def test_objeto_autor(self):
  #      autor = Autor.objects.create(nombre='Chile', 
   #     pseudonimo='Chileno')
    #    self.assertEqual(autor.nombre, 'Chile')
     #   self.assertEqual(autor.nacionalidad, 'Chileno')
     #   self.assertEqual(Nacionalidad.objects.filter(pais='Chile').exists())

class TestComuna(TestCase):
    def test_objeto_comuna(self):
        comuna = Comuna.objects.create(codigo='09101', nombre='Temuco')
        self.assertEqual(comuna.codigo, '09101')
        self.assertEqual(comuna.nombre,'Temuco')
        self.assertEqual(Comuna.objects.filter(codigo='09101').exists(),True)