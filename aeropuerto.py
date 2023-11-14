from vuelo import Vuelo
from JetPrivado import JetPrivado
from helicoptero import Helicoptero
from avion import Avion
from aeronave import Aeronave
from pasajero import Pasajero
from tripulacion import Tripulacion
from torreDeControl import TorreDeControl


class Aeropuerto:
    def __init__(self, nombre_aeropuerto):
        self.nombre_aeropuerto = nombre_aeropuerto
        self.vuelos = []
        self.aeronaves = []
        self.tripulacion = []
        self.torre = TorreDeControl()
        self.puertas = []

    def agregarPuerta(self, puerta):
        self.puertas.append(puerta)

    def quitar_vuelos(self, vuelo):
        for v in self.vuelos:
            if v.get_codigo_de_vuelo() == vuelo.get_codigo_de_vuelo():
                self.vuelos.remove(v)
                break

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def agregar_aeronave(self, aeronave):
        self.aeronaves.append(aeronave)

    def agregar_pasajero_a_vuelo(self, codigo, pasajero):
        for vuelo in self.vuelos:
            if codigo == vuelo.get_codigo_de_vuelo():
                vuelo.agregar_pasajero(pasajero)
                vuelo.quitar_asiento()

    def agregar_tripulante(self, tripulante):
        self.tripulacion.append(tripulante)

    def get_aeronaves(self):
        return self.aeronaves

    def get_vuelos(self):
        return self.vuelos

    def mostrar_vuelos(self):
        print(f"Lista de Vuelos en {self.nombre_aeropuerto}:")
        for vuelo in self.vuelos:
            vuelo.mostrar_informacion()
            print("-----------------------")


    def get_TorreControl(self):
        return self.torre


    def mostrar_pasajeros(self, codigo_vuelo):
        for vuelo in self.vuelos:
            if vuelo.get_codigo_de_vuelo() == codigo_vuelo:
                vuelo.mostrar_pasajeros()

    def mostrar_tripulantes(self, codigo_vuelo):
        for vuelo in self.vuelos:
            if vuelo.get_codigo_de_vuelo() == codigo_vuelo:
                vuelo.mostrar_tripulantes()

    def mostrar_aeronaves(self):
        for i, aeronave in enumerate(self.aeronaves, start=1):
            print(i)
            aeronave.mostrar_info()

    def cambiar_volar(self, index_aeronave):
        aeronave = self.aeronaves[index_aeronave - 1]
        if not aeronave.get_volar():
            aeronave.set_volar(True)
            print("La aeronave ha despegado")
        else:
            aeronave.set_volar(False)
            print("La aeronave ha aterrizado")

    def agregarPuerta(self,puerta):
        self.puertas.append(puerta)

    def get_Puertas(self):
        return self.puertas

    def eliminarPuertaAsignada(self,puerta):
        self.puertas