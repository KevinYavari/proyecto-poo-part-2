from vuelo import Vuelo

class PuertaEmbarque:
    def __init__(self, num_identificacion, ubicacion, hora_embarque):
        self.num_identificacion = num_identificacion
        self.ubicacion = ubicacion
        self.hora_embarque = hora_embarque
        self.disponibilidad = True
        self.historial = []
        self.vuelo_asociado = None

    def ver_informacion(self):
        print("Número de Identificación:", self.num_identificacion)
        print("Ubicación:", self.ubicacion)
        if self.disponibilidad:
            print("Puerta Disponible")
        else:
            print("Puerta No Disponible")
        print("Hora de Embarque:", self.hora_embarque)
        if self.vuelo_asociado is None:
            print("No hay vuelo asociado")
        else:
            print("Información del vuelo asociado:")
            self.vuelo_asociado.mostrar_informacion()

    def get_num_identificacion(self):
        return self.num_identificacion

    def get_ubicacion(self):
        return self.ubicacion

    def get_horaEmbarque(self):
        return self.hora_embarque

    def get_disponibilidad(self):
        return self.disponibilidad

    def agregar_vuelo_historial(self, vuelo):
        self.historial.append(vuelo)

    def ver_historial(self):
        for i, vuelo in enumerate(self.historial, start=1):
            print(f"Vuelo #{i}")
            vuelo.mostrar_informacion()
            print()

    def asignar_vuelo(self, vuelo):
        self.vuelo_asociado = vuelo
        self.disponibilidad = False