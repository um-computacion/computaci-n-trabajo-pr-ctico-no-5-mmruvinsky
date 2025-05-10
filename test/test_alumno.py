import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
       def test_crear_alumno(self):
           alumno = Alumno("Juan", "Pérez", "12345678", "27/01/2004", 123)
           self.assertEqual(alumno.nombre, "Juan")
           self.assertEqual(alumno.apellido, "Pérez")
           self.assertEqual(alumno.dni, "12345678")
           self.assertEqual(alumno.fecha_nacimiento, "27/01/2004")
           self.assertEqual(alumno.legajo, 123)

       def test_repr_alumno(self):
           alumno = Alumno("Juan", "Pérez", "12345678", "27/01/2004", 123)
           expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Fecha de Nacimiento: 27/01/2004 Legajo: 123"
           self.assertEqual(str(alumno), expected)

class TestAlumnoCasosEdge(unittest.TestCase):
    """Test para casos edge de la clase Alumno."""
    
    def test_legajo_invalido(self):
        """Test para verificar validaciones del sueldo"""
        # Sueldo negativo
        with self.assertRaises(ValueError) as e:
            Alumno("Juan", "Pérez", "12345678", "27/01/2004", -123)
        self.assertEqual(str(e.exception), "El legajo no puede ser negativo")
        
        # Sueldo no numérico
        with self.assertRaises(TypeError) as e:
            Alumno("Juan", "Pérez", "12345678", "27/01/2004", "ABC")
        self.assertEqual(str(e.exception), "Formato incorrecto: El legajo debe ser un número")