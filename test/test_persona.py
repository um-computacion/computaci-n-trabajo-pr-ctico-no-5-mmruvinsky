import unittest
from src.persona import Persona


class TestPersona(unittest.TestCase):
       def test_crear_persona(self):
           persona = Persona("Juan", "Pérez", "12345678", "pensamientos", "ultima_idea")
           self.assertEqual(persona.nombre, "Juan")
           self.assertEqual(persona.apellido, "Pérez")
           self.assertEqual(persona.dni, "12345678")
           self.assertEqual(persona.pensamientos, 0)
           self.assertEqual(persona.ultima_idea, "<no penso en nada>") 

       def test_repr_persona(self):
           persona = Persona("Juan", "Pérez", "12345678", 0, "<no penso en nada>")
           expected =  "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Pensamientos: 0 Ultima Idea: <no penso en nada>"
           self.assertEqual(str(persona), expected)

if __name__ == "__main__":
    unittest.main()

 