from aeronave import Aeronave
from avion import Avion
from helicoptero import Helicoptero
from JetPrivado import JetPrivado
from aeropuerto import Aeropuerto
from vuelo import Vuelo

class aerolinia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelosA = []
        self.aeronaves = []  # Cambié el nombre a "aeronaves"

    def vuelosAl(self, vuelo):
        self.vuelosA.append(vuelo)

    def agregar_aeronave(self, aero):  # Cambié el nombre del método
        self.aeronaves.append(aero)

    def reservarVuelo(self, vuelo, pasajero):
        i = 0
        while i < len(self.vuelosA):
            if self.vuelosA[i] == vuelo:
                if self.vuelosA[i].asientos < self.vuelosA[i].aero.capacidad_pasajeros:
                    self.vuelosA[i].agregar_pasajero(pasajero)

    def getNombre(self):
        return self.nombre

    def getvuelos(self):
    	return self.vuelosA

    def getAeronaves(self):
    	return self.aeronaves

    def getCodigosAeronaves(self):
    	lista = []
    	for i in range(len(self.aeronaves)):
    		if self.aeronaves[i] != None:
	    		aeronave = self.aeronaves[i].get_Codigo()
	    		lista.append(aeronave)
    	return lista



