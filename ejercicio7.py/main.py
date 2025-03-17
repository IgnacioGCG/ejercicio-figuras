class Proyecto:
    """
    Clase que representa un proyecto en el que participo.
    """
    def __init__(self, nombre, descripcion, duracion, tecnologias):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.tecnologias = tecnologias

class Tecnologia:
    """
    Clase que representa una tecnología utilizada en los proyectos.
    """
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Participante:
    """
    Clase que representa a un participante en el proyecto.
    """
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia

# Ejemplo de uso
tecnologias = [
    Tecnologia("Python", "Lenguaje de programación"),
    Tecnologia("Django", "Framework web"),
    Tecnologia("React", "Biblioteca de JavaScript")
]

participantes = [
    Participante("Nacho", "Desarrollador", "5 años"),
    Participante("Ana", "Diseñadora", "3 años"),
    Participante("Luis", "Gestor de proyectos", "7 años")
]

proyecto = Proyecto(
    nombre="Desarrollo de una aplicación web",
    descripcion="Proyecto para desarrollar una aplicación web de gestión de tareas.",
    duracion="6 meses",
    tecnologias=tecnologias
)

print(f"Proyecto: {proyecto.nombre}")
print(f"Descripción: {proyecto.descripcion}")
print(f"Duración: {proyecto.duracion}")
print("Tecnologías utilizadas:")
for tech in proyecto.tecnologias:
    print(f"- {tech.nombre} ({tech.tipo})")