
class Aeronave:
    def __init__(self, codigo,marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.autonomia = autonomia
        self.anio_fabricacion = anio_fabricacion
        self.ubicacion = ubicacion
        self.estado = estado
        self.msg = []
        self.cantidad_vuelos = 0
        self.volar = False
    
    def get_Codigo(self):
        return self.codigo   

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_autonomia(self):
        return self.autonomia

    def get_anio_fabricacion(self):
        return self.anio_fabricacion

    def get_estado(self):
        return self.estado

    def get_ubicacion(self):
        return self.ubicacion

    def recibir_mensaje(self, mensajes):
        mensajes_restantes = []
        for mensaje in mensajes:
            print(mensaje[0])
            print(self.marca)
            if mensaje[0] != self.marca:
                mensajes_restantes.append(mensaje)

        self.msg = mensajes_restantes
        print(len(self.msg))

    def ver_ubicaciones(self):
        print(f"Desde: {self.marca} se recibe ubicación de:")
        for mensaje in self.msg:
            print(f"Aeronave: {mensaje[0]}, Altitud: {mensaje[1]}")

    def get_cant_vuelo(self):
        return cant_vuelos

    def get_volar(self):
        return volar

    def set_volar(self):
        self.volar = True
        self.cant_vuelos -= 1
    
    def get_msg(self):
        return self.msg

    def set_estado(self, estado):
        self.estado = estado