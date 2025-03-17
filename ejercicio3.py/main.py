class ObraDeArte:
    def __init__(self, titulo, autor, adscripcion_cronologica, tecnica, sub_tecnica, material_soporte, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.adscripcion_cronologica = adscripcion_cronologica
        self.tecnica = tecnica
        self.sub_tecnica = sub_tecnica
        self.material_soporte = material_soporte
        self.descripcion = descripcion

class Replica(ObraDeArte):
    def __init__(self, titulo, autor, adscripcion_cronologica, tecnica, sub_tecnica, material_soporte, descripcion, original):
        super().__init__(titulo, autor, adscripcion_cronologica, tecnica, sub_tecnica, material_soporte, descripcion)
        self.original = original

# Datos de la obra original
original = ObraDeArte(
    titulo="La Gioconda",
    autor="Leonardo Da Vinci",
    adscripcion_cronologica="1503 — 1516",
    tecnica="óleo",
    sub_tecnica="sfumato",
    material_soporte="madera de álamo",
    descripcion="La Gioconda, también conocida como Mona Lisa, es una obra maestra del Renacimiento, expuesta en el Museo Louvre de París."
)

# Datos de la réplica
replica = Replica(
    titulo="La Gioconda (Réplica)",
    autor="Anónimo",
    adscripcion_cronologica="1503 — 1516",
    tecnica="óleo",
    sub_tecnica="pincelada simple",
    material_soporte="madera de nogal",
    descripcion=("Existen muchas réplicas o copias de La Gioconda (expuesta en el Museo Louvre de París), "
                 "aunque ésta, que se encontraba en el Museo del Prado (Madrid) desde su inauguración, "
                 "procedente de las Colecciones Reales, es la más antigua que se conoce. La conclusión del estudio "
                 "efectuado en el Prado es que la réplica de Madrid fue realizada por un alumno de la escuela de "
                 "Leonardo al mismo tiempo que el artista italiano pintaba su obra maestra. Por ello, las hipótesis "
                 "sobre su autoría se ciñeron al círculo de discípulos que trabajaron con Leonardo. Su estado de "
                 "conservación es mucho mejor que el de la obra original."),
    original=original
)

# Imprimir detalles de la réplica y la obra original
print(f"Título: {replica.titulo}")
print(f"Autor: {replica.autor}")
print(f"Adscripción cronológica: {replica.adscripcion_cronologica}")
print(f"Técnica: {replica.tecnica}")
print(f"Sub-técnica: {replica.sub_tecnica}")
print(f"Material de soporte: {replica.material_soporte}")
print(f"Descripción: {replica.descripcion}")
print(f"Obra original: {replica.original.titulo} de {replica.original.autor}")