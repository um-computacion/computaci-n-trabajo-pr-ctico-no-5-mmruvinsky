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

class TestProfesorCasosEdge(unittest.TestCase):
    """Test para casos edge de la clase Profesor."""
    
    def test_sueldo_invalido(self):
        """Test para verificar validaciones del sueldo"""
        # Sueldo negativo
        with self.assertRaises(ValueError) as e:
            Profesor("Juan", "Pérez", "12345678", "27/01/2004", -50000, "Geografia")
        self.assertEqual(str(e.exception), "El sueldo no puede ser negativo")
        
        # Sueldo no numérico
        with self.assertRaises(TypeError) as e:
            Profesor("Juan", "Pérez", "12345678", "27/01/2004", "cinquenta mil", "Geografia")
        self.assertEqual(str(e.exception), "Formato incorrecto: El sueldo debe ser un número")