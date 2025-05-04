from src.persona import Persona

class Profesor(Persona):
       
       def __init__(self, nombre, apellido, dni, sueldo, materia=None):
           super().__init__(nombre, apellido, dni, materia)
           self.sueldo = sueldo
           self.materia = materia

       def __repr__(self):
           return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo} Materia/s: {self.materia}"
       
"""Clase profesor que hereda de la clase persona y representa a un profesor con nombre, apellido, dni y sueldo."""