from pasajero import Pasajero
from tripulacion import Tripulacion
from aeronave import Aeronave


class Vuelo:
    def __init__(self, codigo_de_vuelo, origen, fecha, destino, aero):
        self.codigo_de_vuelo = codigo_de_vuelo
        self.origen = origen
        self.fecha = fecha
        self.destino = destino
        self.aero = aero
        self.asientos = 0
        self.pasaje = []
        self.tripulantes = []
        self.disponible = True

    def get_origen(self):
        return self.origen

    def get_fecha(self):
        return self.fecha

    def get_destino(self):
        return self.destino

    def get_codigo_de_vuelo(self):
        return self.codigo_de_vuelo

    def mostrar_informacion(self):
        print("Codigo de Vuelo:", self.codigo_de_vuelo)
        print("Origen:", self.origen)
        print("Fecha:", self.fecha)
        print("Destino:", self.destino)
        print("Asientos disponibles:", self.asientos)
        print("Informacion de la Aeronave:")
        if self.aero:
            print("Marca de la Aeronave:", self.aero.get_marca())
            print("Modelo de la Aeronave:", self.aero.get_modelo())
        else:
            print("Aeronave no asignada")

    def agregar_pasajero(self, pasa):
        self.pasaje.append(pasa)

    def agregar_tripulacion(self, tripu):
        self.tripulantes.append(tripu)

    def quitar_asiento(self):
        self.asientos -= 1

    def mostrar_pasajeros(self):
        for pasa in self.pasaje:
            pasa.imprimir_informacion()

    def mostrar_tripulantes(self):
        for tripu in self.tripulantes:
            tripu.imprimir_informacion()

    def get_disponibilidad_vuelo(self):
        return self.disponible

    def set_disponibilidad(self,valor):
        self.disponible = valor
