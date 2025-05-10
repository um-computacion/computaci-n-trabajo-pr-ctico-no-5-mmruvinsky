from persona import Persona
from alumno import Alumno
from profesor import Profesor

# Crear una persona común
p1 = Persona("Juanita", "Lacosturera", "30123456", "15/03/1990")
print("Persona creada:")
print(p1)

# La persona piensa
p1.pensar("Tengo hambre")
print(p1)

# Crear un alumno
a1 = Alumno("Miguel", "Martin", "45678901", "10/05/2000", 1234)
print("\nEstudiante creado:")
print(a1)

# Crear un profesor
prof = Profesor("Esteban", "Quito", "20987654", "22/07/1975", 50000, "Historia")
print("\nProfesor creado:")
print(prof)

# El profesor enseña al alumno
print("\nInteracción profesor-alumno:")
prof.enseñar(a1, "La Revolución Francesa")
print(f"El alumno piensa: {a1.ultima_idea}")
print(f"El profesor piensa: {prof.ultima_idea}")

# Más alumnos
a2 = Alumno("María", "Rodríguez", "46789012", "05/12/2001", 5678)

# Profesor enseña a varios alumnos
print("\nProfesor con múltiples alumnos:")
prof.enseñar(a1, "La Revolución Industrial")
prof.enseñar(a2, "La Guerra Fría")

print(f"\nEl profesor dio {prof.pensamientos} clases")
print(f"Miguel tuvo {a1.pensamientos} pensamientos")
print(f"María tuvo {a2.pensamientos} pensamientos")

print("\nÚltima idea de cada uno:")
print(f"Miguel: {a1.ultima_idea}")
print(f"María: {a2.ultima_idea}")
print(f"Profesor: {prof.ultima_idea}")