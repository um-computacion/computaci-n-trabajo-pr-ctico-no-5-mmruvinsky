import unittest
from src.alumno import Alumno
from src.profesor import Profesor
from src.persona import Persona

class TestInteracciones(unittest.TestCase):
    def test_enseñar(self):
        """Test para verificar la interacción entre las clases"""
        # Alumno y Profesor
        alumno = Alumno("Juan", "Pérez", "12345678", "27/01/2004", 123)
        profesor = Profesor("Juan", "Pérez", "12345678", "27/01/2004", 50000)
        
        # Enseñar alumno a profesor
        profesor.enseñar(alumno, "Geografía")
        self.assertEqual(alumno.pensamientos, 1)
        self.assertEqual(alumno.ultima_idea, "Aprendí de Juan Pérez: Geografía")
        self.assertEqual(profesor.pensamientos, 1)
        self.assertEqual(profesor.ultima_idea, "Voy a enseñar: Geografía")

if __name__ == "__main__":
    unittest.main()