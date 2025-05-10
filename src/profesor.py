from src.persona import Persona

class Profesor(Persona):
       
       def __init__(self, nombre, apellido, dni, fecha_nacimiento, sueldo, materia=None):
           super().__init__(nombre, apellido, dni, fecha_nacimiento)
           self.sueldo = sueldo
           self.materia = materia

           if not isinstance(sueldo, (int, float)):
                raise TypeError("Formato incorrecto: El sueldo debe ser un número")
           
           if sueldo < 0:
                raise ValueError("El sueldo no puede ser negativo")

       def __repr__(self):
           return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Fecha de Nacimiento: {self.fecha_nacimiento} Sueldo: {self.sueldo} Materia/s: {self.materia}"
       
"""Clase profesor que hereda de la clase persona y representa a un profesor con nombre, apellido, dni, fecha de nacimiento, sueldo y materia."""