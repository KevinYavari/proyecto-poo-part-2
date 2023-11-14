from aeronave import Aeronave
from avion import Avion
from helicoptero import Helicoptero
from JetPrivado import JetPrivado

class AeronaveFactory:
    @staticmethod
    def crear_avion(codigo, marca, capacidad_pasajeros, ubicacion, estado, modelo=None, velocidad_maxima=100, autonomia=100, anio_fabricacion=None, altitud_maxima=50, cantidad_motores=2, categoria=None):
        return Avion(codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, altitud_maxima, cantidad_motores, categoria)

    @staticmethod
    def crear_helicoptero(codigo, marca, capacidad_pasajeros, ubicacion, estado, modelo=None, velocidad_maxima=100, autonomia=100, anio_fabricacion=None, cantidad_rotores=2, capacidad_elevacion=12, uso_especifico=None):
        return Helicoptero(codigo,marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, cantidad_rotores, capacidad_elevacion, uso_especifico)

    @staticmethod
    def crear_jet_privado(codigo, marca, capacidad_pasajeros, ubicacion, estado, modelo=None, velocidad_maxima=100, autonomia=100, anio_fabricacion=None, propietario=None, servicios_a_bordo=None, destinos_frecuentes=None):
        return JetPrivado(codigo,marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, propietario, servicios_a_bordo, destinos_frecuentes)
