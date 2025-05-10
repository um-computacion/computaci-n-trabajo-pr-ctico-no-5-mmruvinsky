

class Persona:
       
       def __init__(self, nombre, apellido, dni, fecha_nacimiento, pensamientos=None, ultima_idea=None):
           
           if not isinstance(dni, str):
             raise TypeError("El DNI debe ser una cadena de texto")
           if not dni.isdigit():
            raise ValueError("El DNI debe contener solo dígitos")
           if len(dni) < 7 or len(dni) > 8:
            raise ValueError("El DNI debe tener entre 7 y 8 dígitos")
           
           if not isinstance(fecha_nacimiento, str):
             raise TypeError("La fecha de nacimiento debe ser una cadena de texto")
           if len(fecha_nacimiento) != 10:
            raise ValueError("La fecha de nacimiento debe tener el formato DD/MM/AAAA")
           if not fecha_nacimiento[2] == "/" or not fecha_nacimiento[5] == "/":
            raise ValueError("La fecha de nacimiento debe tener el formato DD/MM/AAAA")
           
           if not isinstance(nombre, str):
                raise TypeError("El nombre debe ser una cadena de texto")
           if not isinstance(apellido, str):
                raise TypeError("El apellido debe ser una cadena de texto")
           
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.fecha_nacimiento = fecha_nacimiento
           self.pensamientos = 0
           self.ultima_idea = "<no penso en nada>"



       def pensar(self, idea):
           self.pensamientos += 1
           self.ultima_idea = idea


       def __repr__(self):
              return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Fecha de Nacimiento: {self.fecha_nacimiento} Pensamientos: {self.pensamientos} Ultima Idea: {self.ultima_idea}"
       
"""Clase persona que representa a una persona con nombre, apellido, dni, pnesamientos y ultima idea.
    La clase tiene un metodo pensar que incrementa el contador de pensamientos y actualiza la ultima idea."""