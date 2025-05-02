class Persona:
       def __init__(self, nombre, apellido, dni, pensamientos, ultima_idea):
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.pensamientos = 0
           self.ultima_idea = "<no penso en nada>"

       def __repr__(self):
              return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Pensamientos: {self.pensamientos} Ultima Idea: {self.ultima_idea}"