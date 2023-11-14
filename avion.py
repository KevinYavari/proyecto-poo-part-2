from aeronave import Aeronave

class Avion(Aeronave):
    def __init__(self, codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, altitud_maxima, cantidad_motores, categoria):
        super().__init__(codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado)
        self.altitud_maxima = altitud_maxima
        self.cantidad_motores = cantidad_motores
        self.categoria = categoria

    def mostrar_info(self):
        print(f"Avión: {self.marca} {self.modelo}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print(f"Autonomía: {self.autonomia}")

    def get_altitud_maxima(self):
        return self.altitud_maxima

    def get_cantidad_motores(self):
        return self.cantidad_motores

    def get_categoria(self):
        return self.categoria

    def getCodigo(self):
        return self.codigo
