import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
       def test_crear_alumno(self):
           alumno = Alumno("Juan", "Pérez", "12345678", "27/01/2004", "A123")
           self.assertEqual(alumno.nombre, "Juan")
           self.assertEqual(alumno.apellido, "Pérez")
           self.assertEqual(alumno.dni, "12345678")
           self.assertEqual(alumno.fecha_nacimiento, "27/01/2004")
           self.assertEqual(alumno.legajo, "A123")

       def test_repr_alumno(self):
           alumno = Alumno("Juan", "Pérez", "12345678", "27/01/2004", "A123")
           expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Fecha de Nacimiento: 27/01/2004 Legajo: A123"
           self.assertEqual(str(alumno), expected)