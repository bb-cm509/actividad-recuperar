from abc import ABC, abstractmethod
class Equipo (ABC):
    def __init__(self, codigo, tipo):
        self.codigo = codigo
        self.tipo = tipo
        self.estado = "disponible"
        

    @abstractmethod
    def asignar(self, responsable):
        pass

class PC(Equipo):
    def __init__(self, codigo, procesador):
        super().__init__(codigo, "PC")
        self.procesador = procesador

    def asignar(self, responsable):
        if self.estado == "disponible":
            return super().asignar(responsable)
        else:
            raise Exception("El equipo ya está asignado")

class Impresora(Equipo):
    def __init__(self, codigo, tipo_impresion):
        super().__init__(codigo, "Impresora")
        self.tipo_impresion = tipo_impresion

    def asignar(self, responsable):
        if self.estado == "disponible":
            return super().asignar(responsable)
        else:
            raise Exception("El equipo ya está asignado")

inventario = [PC("INT-001", "i5"), PC("INT-002", "i7"), Impresora("INT-003", "Láser")]

for equipo in inventario:
    try:
        print(equipo.asignar("Juan"))
        print(equipo.asignar("María"))
    except Exception as e:
        print(f"Error: {e}")