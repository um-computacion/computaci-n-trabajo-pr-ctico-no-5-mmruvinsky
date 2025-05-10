from persona import Persona
from alumno import Alumno

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
       

       def enseñar(self, alumno, concepto):
                """
                El profesor enseña un concepto a un alumno, lo que hace que el alumno 
                piense en ese concepto.
                
                Args:
                    alumno (Alumno): El alumno al que enseñar
                    concepto (str): El concepto que se enseña
                """
                if not isinstance(alumno, Alumno):
                    raise TypeError("Solo se puede enseñar a un alumno")
                
                # El profesor piensa en lo que va a enseñar
                self.pensar(f"Voy a enseñar: {concepto}")
                
                # El alumno piensa en lo que aprende
                alumno.pensar(f"Aprendí de {self.nombre} {self.apellido}: {concepto}")
                
                return f"{self.nombre} enseñó '{concepto}' a {alumno.nombre}"
       
       """Clase profesor que hereda de la clase persona y representa a un profesor con nombre, apellido, dni, fecha de nacimiento, sueldo y materia."""