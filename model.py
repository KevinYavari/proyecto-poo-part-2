from aeronaveFactory import AeronaveFactory
from aeronave import Aeronave
from avion import Avion
from helicoptero import Helicoptero
from JetPrivado import JetPrivado
from aeropuerto import Aeropuerto
from vuelo import Vuelo
from pasajero import Pasajero
from tripulacion import Tripulacion
from torreDeControl import TorreDeControl
from puertaEmbarque import PuertaEmbarque
from aerolinia import aerolinia
import streamlit as st
import requests
import json

class model:
    def __init__(self):
        if 'aerolinia' not in st.session_state:
            self.aerolinia = st.session_state['aerolinia'] = {}
        else:
            self.aerolinia = st.session_state['aerolinia']

        if 'aeropuerto' not in st.session_state:
            self.aeropuerto = st.session_state['aeropuerto'] = Aeropuerto("Aeropuerto Alfonso Bonilla")
        else:
            self.aeropuerto = st.session_state['aeropuerto']

    def crearAvion(self, codigo, marca, capacidad_pasajeros, ubicacion, estado, aeroli):
        avion = AeronaveFactory.crear_avion(codigo, marca, capacidad_pasajeros, ubicacion, estado)
        self.aerolinia[aeroli].agregar_aeronave(avion)
        self.aeropuerto.agregar_aeronave(avion)

    def crearHelicoptero(self, codigo, marca, capacidad_pasajeros, ubicacion, estado, aeroli):
        helicoptero = AeronaveFactory.crear_helicoptero(codigo, marca, capacidad_pasajeros, ubicacion, estado)
        self.aerolinia[aeroli].agregar_aeronave(helicoptero)
        self.aeropuerto.agregar_aeronave(helicoptero)

    def crearJet(self, codigo, marca, capacidad_pasajeros, ubicacion, estado, aeroli):
        jet = AeronaveFactory.crear_jet_privado(codigo, marca, capacidad_pasajeros, ubicacion, estado)
        self.aerolinia[aeroli].agregar_aeronave(jet)
        self.aeropuerto.agregar_aeronave(jet)

    def registrarVuelos(self, aerol, vuelo, aeronave):
        ans = True
        if aeronave.cantidad_vuelos != 3:
            x = self.aerolinia[aerol].getvuelos()
            for i in range(len(x)):
                if x[i] != None:
                    if x[i].get_codigo_de_vuelo() == vuelo:
                        self.aerolinia[aerol].vuelosA[i].aero = aeronave
                        self.aerolinia[aerol].asientos = aeronave.capacidad_pasajeros
            aeronave.cantidad_vuelos += 1
            
        else:
            ans = False
        return ans

    def crearVuelo(self, codigo_de_vuelo, origen, fecha, destino, aero, aerolinia):
        vuelo = Vuelo(codigo_de_vuelo, origen, fecha, destino, aero)
        self.aerolinia[aerolinia].vuelosAl(vuelo)
        self.aeropuerto.agregar_vuelo(vuelo)

    def crearAerolina(self, nombre):
        nueva_aerolinea = aerolinia(nombre)
        self.aerolinia[nueva_aerolinea] = []

    def reserva(self, aerolinia, vuelo, pasajero):
        self.aerolinia[aerolinia].reservarVuelo(self, vuelo, pasajero)

    def crearPuertaDeEmbarque(self, id, ubi, hora):
        puerta = PuertaEmbarque(id, ubi, hora)
        self.aeropuerto.agregarPuerta(puerta)

    def crearPasajero(self, cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, 
        numero_de_telefono, correo_electronico, nacionalidad, maletas, info_medico):
        nuevo_pasajero = Pasajero(cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, 
            numero_de_telefono, correo_electronico, nacionalidad, maletas, info_medico)
        return nuevo_pasajero 
    
    def crearTripulante(self, cedula, nombres, apellidos, fecha_nacimiento, genero, direccion, numero_telefono,
                 correo_electronico, puesto, anos_experiencia, horas_trabajo):
        nuevo_tripu = Tripulacion(cedula, nombres, apellidos, fecha_nacimiento, genero, direccion, numero_telefono,
                 correo_electronico, puesto, anos_experiencia, horas_trabajo)
        self.aeropuerto.agregar_tripulante(nuevo_tripu)
        return nuevo_tripu

    def asignar_puerta_vuelo(self, puerta, vuelo):
        puerta.asignar_vuelo(vuelo)
        vuelo.set_disponibilidad(False)

    def despegar(self, aeronave):
        aeronave.set_volar()

    def getAerolinia(self):
        lista = []
        for aerolinea_instance in self.aerolinia.values():
            lista.append(aerolinea_instance.getNombre())
        return lista

    def getAer(self):
        return self.aerolinia

    def AnadirAerolinia(self, nombre):
        aerolinias = aerolinia(nombre)
        self.aerolinia[nombre] = aerolinias
    
    def getAeronaves(self,a):
        nombre_aerolinea = a
        aeronaves_de_aerolinea = self.aerolinia[nombre_aerolinea].getAeronaves()
        return aeronaves_de_aerolinea
    
    def codigos(self, b):
        codigos = self.aerolinia[b].getCodigosAeronaves()
        return codigos
    
    def agregarPuertaAeropuerto(self,puerta):
        self.aeropuerto.agregarPuerta(puerta)

    def anadirAeronaveAeropuerto(self,aeronave):
        self.aeropuerto.agregar_aeronave(aeronave)

    def obtenerAerolineas(self):
        return self.aeropuerto.get_Puertas()

    def obtenerVuelos(self):
        return self.aeropuerto.get_vuelos()

    def obtenerIdsPuertas(self):
        ids = []
        puertas = self.aeropuerto.get_Puertas()
        for puerta in puertas:
            if puerta is not None:
                if puerta.get_disponibilidad():
                    ids.append(puerta.get_num_identificacion())
        return ids

    def obtenerIdsVuelos(self):
        ids = []
        vuelos = self.aeropuerto.get_vuelos()
        for vuelo in vuelos:
            if vuelo is not None:
                if vuelo.get_disponibilidad_vuelo():
                    ids.append(vuelo.get_codigo_de_vuelo())
        return ids
    
    def buscarPuerta(self,id):
        ans = None
        puertas = self.aeropuerto.get_Puertas()
        for puerta in puertas:
            if puerta is not None:
                if puerta.get_num_identificacion() == id:
                    ans = puerta
                    break
        return ans

    def buscarVuelo(self,id):
        ans = None
        vuelos = self.aeropuerto.get_vuelos()
        for vuelo in vuelos:
            if vuelo is not None:
                if vuelo.get_codigo_de_vuelo() == id:
                    ans = vuelo
                    break
        return ans
    
    def get_Aeronaves(self):
        return self.aeropuerto.get_aeronaves()

    def verMensaje(self,aeronave):
        aeronave.ver_ubicaciones()
        
    def get_country_data(self, pais):
        url = f"https://restcountries.com/v3.1/name/{pais}"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data[0]
        else:
            return None
    
    def show_country_info(self, country_data):
        if country_data is not None:
            st.write(f"Nombre del país: {country_data.get('name', 'No disponible')}")

            # Acceder a la lista de capitales de manera segura
            capitals = country_data.get('capital', [])
            capital = capitals[0] if capitals else 'No disponible'
            st.write(f"Capital: {capital}")

            # Acceder a la lista de 'currencies' de manera segura
            currencies_info = country_data.get('currencies', {})
            moneda = currencies_info.get('COP', {}).get('name', 'No disponible')
            st.write(f"Moneda: {moneda}")

            st.write(f"Región: {country_data.get('region', 'No disponible')}")
            st.write(f"Subregión: {country_data.get('subregion', 'No disponible')}")
            st.write(f"Población: {country_data.get('population', 'No disponible')}")

            # Mostrar la bandera
            bandera_url = country_data.get('flags', {}).get('png', 'No disponible')
            st.image(bandera_url, caption='Bandera', use_column_width=True)
        else:
            st.error("Error al obtener la información del país. Verifica el nombre e inténtalo de nuevo.")
            
    def obtenerIdsAeronaves(self):
        ids = []
        aeronaves = self.aeropuerto.get_aeronaves()
        for aeronave in aeronaves:
            if aeronave is not None:
                ids.append(aeronave.get_Codigo())
        return ids

    def asignarEstadoAeronave(self,estado,aeronave):
        aeronave.set_estado(estado)
            
    def reportarUbicacion(self):
        self.aeropuerto.get_TorreControl().enviar_ubicaciones(self.aeropuerto.get_aeronaves())
        st.write(len(self.aeropuerto.get_aeronaves()[0].get_msg()))
        
    def buscarAeronave(self,id):
        ans = None
        aeronaves = self.aeropuerto.get_aeronaves()
        for aeronave in aeronaves:
            if aeronave is not None:
                if aeronave.get_Codigo() == id:
                    ans = aeronave
                    break
        return ans
    
    
        