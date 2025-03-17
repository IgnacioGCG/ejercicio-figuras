class Persona:
    def __init__(self, nombre, apellido1, apellido2, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}, Nacido el: {self.fecha_nacimiento}, Sexo: {self.sexo}, ID: {self.numero_identificacion}"