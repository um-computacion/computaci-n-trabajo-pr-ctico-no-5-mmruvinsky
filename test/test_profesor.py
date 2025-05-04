import unittest
from src.profesor import Profesor

  
class TestProfesor(unittest.TestCase):
       def test_crear_profesor(self):
           profesor = Profesor("Juan", "Pérez", "12345678", 50000, "Geografia")
           self.assertEqual(profesor.nombre, "Juan")
           self.assertEqual(profesor.apellido, "Pérez")
           self.assertEqual(profesor.dni, "12345678")
           self.assertEqual(profesor.sueldo, 50000)
           self.assertEqual(profesor.materia, "Geografia")

       def test_repr_profesor(self):
           profesor = Profesor("Juan", "Pérez", "12345678", 50000, "Geografia")
           expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000 Materia/s: Geografia"
           self.assertEqual(str(profesor), expected)