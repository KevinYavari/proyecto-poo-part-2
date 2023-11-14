from aeronave import Aeronave

class JetPrivado(Aeronave):
    def __init__(self, codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado, propietario, servicios_a_bordo, destinos_frecuentes):
        super().__init__(codigo, marca, modelo, capacidad_pasajeros, velocidad_maxima, autonomia, anio_fabricacion, ubicacion, estado)
        self.propietario = propietario
        self.servicios_a_bordo = servicios_a_bordo
        self.destinos_frecuentes = destinos_frecuentes

    def mostrar_info(self):
        print(f"Jet Privado: {self.marca} {self.modelo}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        # ... resto de la implementación de mostrarInfo()
    
    def getCodigo(self):
        return self.codigo