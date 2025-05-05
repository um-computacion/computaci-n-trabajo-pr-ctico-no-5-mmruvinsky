from src.persona import Persona

class Alumno(Persona):
       
       def __init__(self, nombre, apellido, dni, fecha_nacimiento, legajo):
           super().__init__(nombre, apellido, dni, fecha_nacimiento)
           self.legajo = legajo

       def __repr__(self):
           return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Fecha de Nacimiento: {self.fecha_nacimiento} Legajo: {self.legajo}" 

"""Clase alumno que hereda de la clase persona y representa a un alumno con nombre, apellido, dni, fecha de nacimiento y legajo."""