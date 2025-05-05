import unittest
from src.profesor import Profesor

  
class TestProfesor(unittest.TestCase):
       def test_crear_profesor(self):
           profesor = Profesor("Juan", "Pérez", "12345678", "27/01/2004", 50000, "Geografia")
           self.assertEqual(profesor.nombre, "Juan")
           self.assertEqual(profesor.apellido, "Pérez")
           self.assertEqual(profesor.dni, "12345678")
           self.assertEqual(profesor.fecha_nacimiento, "27/01/2004")
           self.assertEqual(profesor.sueldo, 50000)
           self.assertEqual(profesor.materia, "Geografia")

       def test_repr_profesor(self):
           profesor = Profesor("Juan", "Pérez", "12345678", "27/01/2004", 50000, "Geografia")
           expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Fecha de Nacimiento: 27/01/2004 Sueldo: 50000 Materia/s: Geografia"
           self.assertEqual(str(profesor), expected)