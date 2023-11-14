from view import View
from model import model
import streamlit as st
import requests
import json


class controller:
	def __init__(self):
		self.model = model()
		self.View = View()


	def showmenu(self):
		option = self.View.menu()
		if option == "Usuario":
			st.write("Bienvenido al menú para Usuarios.")
			ans = st.sidebar.selectbox("Elige una opción", ("Ver Vuelos", "Comprar Vuelo", "Informacion Pais"))
			if ans == "Ver Vuelos":
				self.mostrarVuelosPasajero()
			
			elif ans == "Comprar Vuelo":
				nuevoUsuario = self.controllerCrearUsuario()
				if nuevoUsuario != None:
					e = self.comprarVuelo()
					if e != None:
						self.model.reserva(e, nuevoUsuario)

			elif ans == "Informacion Pais":
				self.mostrarPaises()

		else:
			st.write("Bienvenido al menú para Empleados.")
			ans = st.sidebar.selectbox("Elige una opción", ("Crear Aerolinea", "Crear Vuelo", "Crear Aeronave", "Asignar Aeronave a Vuelo",  "Crear puerta de embarque", "Ver Ubicaciones", "Crear Tripulante"))
			if ans == "Crear Aerolinea":
				crearAerolinea = self.controllerAerolia()		
			elif ans == "Crear Vuelo":
				crearVuelo = self.controllerVuelo()
			elif ans == "Crear Aeronave":
				crearAeronave = self.crearAeronaves()
			elif ans == "Asignar Aeronave a Vuelo":
				asignar = self.asignarVueloAeronaves()
			elif ans == "Crear puerta de embarque":
				crearPuerta = self.crearPuerta()
			elif ans == "Ver Ubicaciones":
				self.mostrar_aeronaves()
				self.verUbicacion()
			elif ans == "Crear Tripulante":
				self.crearTripulacion()


			ans1 = st.sidebar.selectbox("Menu Torre de Control", ("Mandar Ubicaion", "Asignar puerta a vuelo", "Control estados aeronves"))
			st.header("Menu Torre de Control")
			if ans1 == "Mandar Ubicaion":
				ubi = self.reportarUbicaciones()
			elif ans1 == "Asignar puerta a vuelo":
				self.mostrarPuertas()
				self.mostrarVuelosEmpleado()
				self.asignar_puerta_vuelo()
			elif ans1 == "Control estados aeronves":
				self.controlEstadosAeronaves()
    
	def controlEstadosAeronaves(self):
		ids = self.model.obtenerIdsAeronaves()
		aeronave = self.View.elegir_Aeronave(ids)
		estado = self.View.elegirEstado()
		ans = st.button("Cambiar Estado" , type = "primary")
		if ans:
			aero = self.model.buscarAeronave(aeronave)
			self.model.asignarEstadoAeronave(estado,aero)

 
	def controllerCrearUsuario(self):
		pasajero = self.View.pedir_datos_pasajero()
		if pasajero:
			nuevoPasajero = self.model.crearPasajero(pasajero["cedula"], pasajero["nombres"], pasajero["apellidos"], pasajero["fecha_de_nacimiento"],
				pasajero["genero"], pasajero["direccion"], pasajero["numero_de_telefono"], pasajero["correo_electronico"],
				pasajero["nacionalidad"], pasajero["maletas"], pasajero["info_medico"])
			return nuevoPasajero
		else:
			return None

	def mostrarVuelosPasajero(self):
		aerolinias = self.model.getAerolinia()
		diccionario = self.model.getAer()
		self.View.mostrar_vuelos(aerolinias, diccionario)
        
	def controllerAerolia(self):
		aeroline = self.View.crearAerolinia()
		if aeroline:
			nuevoAerolinea = self.model.AnadirAerolinia(aeroline)
   
	def crearAeronaves(self):
		x = self.View.seleccionAero()
		a = self.model.getAerolinia()
		aerolinia = self.View.seleccionarAerolinia(a)
		aerona = self.View.crearAeronav()
		if aerona:
			if x == 1:
				nuevaAeronave = self.model.crearHelicoptero(aerona["Codigo"],aerona["Marca"],aerona["capacidad pasajero"], aerona["ubicacion"],aerona["estado"], aerolinia )
				self.model.aerolinia[aerolinia].agregar_aeronave(nuevaAeronave)
				#self.model.anadirAeronaveAeropuerto(nuevaAeronave)
			elif x == 2:
				nuevaAeronave = self.model.crearAvion(aerona["Codigo"], aerona["Marca"],aerona["capacidad pasajero"], aerona["ubicacion"],aerona["estado"], aerolinia)
				self.model.aerolinia[aerolinia].agregar_aeronave(nuevaAeronave)
				#self.model.anadirAeronaveAeropuerto(nuevaAeronave)
			elif x == 3:
				nuevaAeronave = self.model.crearJet(aerona["Codigo"], aerona["Marca"],aerona["capacidad pasajero"], aerona["ubicacion"],aerona["estado"], aerolinia)
				self.model.aerolinia[aerolinia].agregar_aeronave(nuevaAeronave)
				#self.model.anadirAeronaveAeropuerto(nuevaAeronave)
    	
	def controllerVuelo(self):
		a = self.model.getAerolinia()
		aerolinia = self.View.seleccionarAerolinia(a)
		vuel = self.View.pedirDatosVuelo()
		aero = ""
		if vuel:
			self.model.crearVuelo(vuel["codigo de vuelo"],vuel["Origen"], vuel["Fecha"], vuel["Destino"], aero, aerolinia)
   
	def asignarVueloAeronaves(self):
		a = self.model.getAerolinia()
		aerolinia = self.View.seleccionarAerolinia(a)
		c = self.model.codigos(aerolinia)
		b = self.model.getAeronaves(aerolinia)
		d = self.View.elegirAeronave(c, b)
		diccionario = self.model.getAer()
		e = self.View.elegirVuelo(diccionario, aerolinia)
		if e:
			asignacion = self.model.registrarVuelos(aerolinia,e, d)
			mensaje = self.View.men(asignacion)
	
	def comprarVuelo(self):
		a = self.model.getAerolinia()
		aerolinia = self.View.seleccionarAerolinia(a)
		c = self.model.codigos(aerolinia)
		diccionario = self.model.getAer()
		e = self.View.elegirVuelo2(diccionario, aerolinia)
		return e


	def crearPuerta(self):
		puerta = self.View.crearPuerta()
		if puerta:
			nuevaPuerta = self.model.crearPuertaDeEmbarque(puerta["Numero de identificacion"],puerta["Ubicacion"],puerta["Hora de embarque"])
			self.model.agregarPuertaAeropuerto(nuevaPuerta)


	def reportarUbicaciones(self):
		data = self.View.mandarUbicaciones()
		if data:
			self.model.reportarUbicacion()
			st.write("Se han mandado las ubicaiones")

	def asignar_puerta_vuelo(self):
		st.header("Seleccion la puerta y la aerolinea que desea asignar:")
		idsP = self.model.obtenerIdsPuertas()
		idsV = self.model.obtenerIdsVuelos()
		puertaS = self.View.asignarPuerta(idsP)
		vueloS = self.View.asignarVuelo(idsV)

		button = st.button("Realizar" , type = "primary")
		if button:
			p = self.model.buscarPuerta(puertaS)
			v = self.model.buscarVuelo(vueloS)
			self.model.asignar_puerta_vuelo(p, v)
   
	def mostrarPuertas(self):
		puertas = self.model.obtenerAerolineas()
		self.View.mostrarPuertas(puertas)
	
	def mostrarVuelosEmpleado(self):
		vuelos = self.model.obtenerVuelos()
		self.View.mostrarVuelosEmpleado(vuelos)
  
	def verUbicacion(self):
		aeronaves = self.model.get_Aeronaves()
		option = self.View.verUbicacionAeronave(aeronaves)
		aeronave = self.model.buscarAeronave(option)
		st.write(len(aeronave.get_msg()))
		self.View.verMensaje(aeronave.get_msg())
	
	def mostrar_aeronaves(self):
		aeronaves = self.model.get_Aeronaves()
		self.View.mostrarAeronaves(aeronaves)
  
	def mostrarPaises(self):
		pais = self.View.nombrePais()
		paisEligido = self.model.get_country_data(pais)
		mostrar = self.model.show_country_info(paisEligido)
  
	def crearTripulacion(self):
		tripulante = self.View.pedir_datos_tripulante()
		if tripulante:
			nuevoTripulante = self.model.crearTripulante(tripulante["cedula"],tripulante["nombres"],tripulante["apellidos"],tripulante["fecha_de_nacimiento"],
                                                tripulante["genero"],tripulante["direccion"],
                                                tripulante["numero_de_telefono"],tripulante["correo_electronico"],tripulante["puesto"],
                                                tripulante["anos experiencia"],tripulante["horas_trabajo"])
			return nuevoTripulante
		else:
			return None
	