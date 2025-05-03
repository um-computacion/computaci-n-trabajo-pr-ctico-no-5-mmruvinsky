

class Persona:
       
       def __init__(self, nombre, apellido, dni, pensamientos=None, ultima_idea=None):
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.pensamientos = 0
           self.ultima_idea = "<no penso en nada>"


       def pensar(self, idea):
           self.pensamientos += 1
           self.ultima_idea = idea


       def __repr__(self):
              return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Pensamientos: {self.pensamientos} Ultima Idea: {self.ultima_idea}"
       
"""Clase persona que representa a una persona con nombre, apellido, dni, pnesamientos y ultima idea.
    La clase tiene un metodo pensar que incrementa el contador de pensamientos y actualiza la ultima idea."""