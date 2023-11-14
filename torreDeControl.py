from aeronave import Aeronave
from vuelo import Vuelo
from puertaEmbarque import PuertaEmbarque

class TorreDeControl:
    def __init__(self):
        self.aeronaves = []
        self.vuelos = []
        self.puertas = []
        self.mensajes = []

    def registrar_aeronave(self, aeronave):
        self.aeronaves.append(aeronave)

    def registrar_vuelos(self, vuelo):
        self.vuelos.append(vuelo)

    def registrar_puertas(self, puerta):
        self.puertas.append(puerta)

    def enviar_ubicaciones(self, lista_aeronaves):
        mensajes = []
        for aeronave in lista_aeronaves:
            if aeronave.get_estado() == "En vuelo":
                mensajes.append((aeronave.get_marca(), aeronave.get_ubicacion()))

        for aeronave in lista_aeronaves:
            if aeronave.get_estado() == "En vuelo":
                aeronave.recibir_mensaje(mensajes)

    def asignar_puerta_vuelo(self):
        print("Vuelos sin asignar:")
        for i, vuelo in enumerate(self.vuelos, start=1):
            if vuelo.get_disponibilidad_vuelo():
                print(f"{i}:")
                vuelo.mostrar_informacion()

        print("Puertas sin asignar:")
        for j, puerta in enumerate(self.puertas, start=1):
            if puerta.get_disponibilidad():
                print(f"{j}:")
                puerta.ver_informacion()

        p = int(input("Selecciona el vuelo a asignar con el índice: "))
        q = int(input("Selecciona la puerta para el vuelo con el índice: "))

        self.puertas[q - 1].asignar_vuelo(self.vuelos[p - 1])
        self.puertas[q - 1].agregar_vuelo_historial(self.vuelos[p - 1])

    def ver_puertas_asignadas(self):
        for puerta in self.puertas:
            if not puerta.get_disponibilidad():
                puerta.ver_informacion()

    def ver_ultima(self):
        self.puertas[-1].ver_informacion()

    def ver_puertas(self):
        for puerta in self.puertas:
            puerta.ver_informacion()