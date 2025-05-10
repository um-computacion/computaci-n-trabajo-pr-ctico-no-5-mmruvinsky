import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")
        self.assertEqual(persona.fecha_nacimiento, "27/01/2004")
        self.assertEqual(persona.pensamientos, 0)
        self.assertEqual(persona.ultima_idea, "<no penso en nada>") 

    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Fecha de Nacimiento: 27/01/2004 Pensamientos: 0 Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_pensar_incrementa_contador(self):
        persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")

class TestPersonaCasosEdge(unittest.TestCase):
    """Test para casos edge de la clase Persona."""
    
    def test_dni_invalido(self):
        """Test para verificar validaciones del DNI"""
        # DNI no numérico
        with self.assertRaises(ValueError) as e:
            Persona("Juan", "Pérez", "123ABC78", "27/01/2004")
        self.assertEqual(str(e.exception), "El DNI debe contener solo dígitos")
        
        # DNI muy corto
        with self.assertRaises(ValueError) as e:
            Persona("Juan", "Pérez", "123456", "27/01/2004")
        self.assertEqual(str(e.exception), "El DNI debe tener entre 7 y 8 dígitos")
        
        # DNI muy largo
        with self.assertRaises(ValueError) as e:
            Persona("Juan", "Pérez", "123456789", "27/01/2004")
        self.assertEqual(str(e.exception), "El DNI debe tener entre 7 y 8 dígitos")

    def test_fecha_invalida(self):
        """Test para verificar validaciones de la fecha"""
        # Formato incorrecto (falta barra)
        with self.assertRaises(ValueError) as e:
            Persona("Juan", "Pérez", "12345678", "27-01-2004")
        self.assertEqual(str(e.exception), "La fecha de nacimiento debe tener el formato DD/MM/AAAA")
        
        # Longitud incorrecta
        with self.assertRaises(ValueError) as e:
            Persona("Juan", "Pérez", "12345678", "1/1/2004")
        self.assertEqual(str(e.exception), "La fecha de nacimiento debe tener el formato DD/MM/AAAA")

    def test_none_values(self):
        """Test para verificar el manejo de valores None"""
        # Nombre None
        with self.assertRaises(TypeError) as e:
            Persona(None, "Pérez", "12345678", "27/01/2004")
        self.assertEqual(str(e.exception), "El nombre debe ser una cadena de texto")
        
        # Apellido None
        with self.assertRaises(TypeError) as e:
            Persona("Juan", None, "12345678", "27/01/2004")
        self.assertEqual(str(e.exception), "El apellido debe ser una cadena de texto")
        
        # DNI None
        with self.assertRaises(TypeError) as e:
            Persona("Juan", "Pérez", None, "27/01/2004")
        self.assertEqual(str(e.exception), "El DNI debe ser una cadena de texto")
        
        # Fecha None
        with self.assertRaises(TypeError) as e:
            Persona("Juan", "Pérez", "12345678", None)
        self.assertEqual(str(e.exception), "La fecha de nacimiento debe ser una cadena de texto")

if __name__ == "__main__":
    unittest.main()