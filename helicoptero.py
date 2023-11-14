from aeronave import Aeronave

class Helicoptero(Aeronave):
    def __init__(self, codigo,marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, cantidad_rotores, capacidad_elevacion, uso_especifico):
        super().__init__(codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado)
        self.cantidad_rotores = cantidad_rotores
        self.capacidad_elevacion = capacidad_elevacion
        self.uso_especifico = uso_especifico



    def get_cantidad_rotores(self):
        return self.cantidad_rotores

    def get_capacidad_elevacion(self):
        return self.capacidad_elevacion

    def get_uso_especifico(self):
        return self.uso_especifico

    def getCodigo(self):
        return self.codigo
