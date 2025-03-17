from datetime import date

class ActuacionArqueologica:
    def __init__(self, fecha_inicio: date, fecha_fin: date, tipo: str):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

    def __str__(self):
        return f"Actuación Arqueológica: {self.tipo} desde {self.fecha_inicio} hasta {self.fecha_fin}"