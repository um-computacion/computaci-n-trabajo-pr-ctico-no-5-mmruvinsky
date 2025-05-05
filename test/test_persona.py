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
           expected =  "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Fecha de Nacimiento: 27/01/2004 Pensamientos: 0 Ultima Idea: <no penso en nada>"
           self.assertEqual(str(persona), expected)

       def test_pensar_incrementa_contador(self):
            persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
            persona.pensar("Hola mundo")
            self.assertEqual(persona.pensamientos, 1)

       def test_pensar_actualiza_ultima_idea(self):
            persona = Persona("Juan", "Pérez", "12345678", "27/01/2004")
            persona.pensar("Hola mundo")
            self.assertEqual(persona.ultima_idea, "Hola mundo")
  

if __name__ == "__main__":
    unittest.main()

 