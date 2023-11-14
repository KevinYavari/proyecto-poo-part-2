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

class View:
    def __init__(self):
        st.title("Aeropuerto Alfonso Bonilla")

    def menu(self):
        st.header("Menú de opciones")
        option = st.selectbox("Seleccione rol:", ["Usuario", "Empleado"])
        return option


    def pedir_datos_pasajero(self):
        cedula = st.text_input("Cédula: ")
        nombres = st.text_input("Nombres: ")
        apellidos = st.text_input("Apellidos: ")
        fecha_de_nacimiento = st.text_input("Fecha de nacimiento: ")
        genero = st.text_input("Género: ")
        direccion = st.text_input("Dirección: ")
        numero_de_telefono = st.text_input("Número de teléfono: ")
        correo_electronico = st.text_input("Correo electrónico: ")
        nacionalidad = st.text_input("Nacionalidad: ")
        maletas = st.number_input("Ingrese el numero de pasajeros")
        info_medico = st.text_input("Información médica: ")

        ans = st.button("Crear Usuario", type="primary")

        if ans:
            return {
                "cedula": cedula,
                "nombres": nombres,
                "apellidos": apellidos,
                "fecha_de_nacimiento": fecha_de_nacimiento, 
                "genero": genero,
                "direccion": direccion,
                "numero_de_telefono": numero_de_telefono,
                "correo_electronico": correo_electronico,
                "nacionalidad": nacionalidad,
                "maletas": maletas,
                "info_medico": info_medico
            }
	
    def mostrar_vuelos(self, aerolinias, diccionario):
        AeroDeseada = st.selectbox("Seleccione Aerolínea:", aerolinias)
        st.header(AeroDeseada)
        if AeroDeseada in diccionario:
            st.header("Módulo de visualización de vuelos")
            vueloProgramados = []
            for singleVuelo in diccionario[AeroDeseada].getvuelos():
                vueloProgramados.append({
                    "codigo de vuelo": singleVuelo.codigo_de_vuelo,
                    "origen": singleVuelo.origen,
                    "fecha": singleVuelo.fecha,
                    "destino": singleVuelo.destino,
                    "Aeronave" : singleVuelo.aero.get_Codigo()
                })
            if vueloProgramados:
                st.table(vueloProgramados)
            else:
                st.info(f"No hay vuelos para la aerolínea {AeroDeseada}", icon="ℹ️")
        else:
            st.warning(f"No hay vuelos para la aerolínea {AeroDeseada}")

    def crearAerolinia(self):
        aerolinia = st.text_input("Aerolinia: ")
        ans = st.button("Crear Aerolinia", type="primary")
        if ans:
            return aerolinia
                
    def seleccionAero(self):
        aeroD = st.selectbox("Seleccione El Tipo de Aeronave:", ["Helicoptero","Avion","Jet Privado"])
        if aeroD == "Helicoptero":
            aero2 = 1
        elif aeroD == "Avion":
            aero2 = 2
        else:
            aero2 = 3
        return aero2
    
    def crearAeronav(self):
        codigo = st.text_input("Codigo: ")
        marca = st.text_input("Marca: ")
        capacidad_pasajero = st.number_input("Ingrese el numero de pasajeros",min_value=1)
        ubicacion = st.text_input("ubicacion: ")
        estado = st.selectbox("Seleccione El Tipo de Aeronave:", ["En mantenimiento","Disponible","Totalmente asignada", "En puerta de embarque","En pista de despegue","En vuelo"])
        ans = st.button("Crear Aeronave", type="primary")
        if ans:
            return {
                "Codigo" : codigo,
                "Marca": marca,
                "capacidad pasajero": capacidad_pasajero,
                "ubicacion": ubicacion,
                "estado": estado
            }
            
    def seleccionarAerolinia(self, a):
        aerolin = AeroDeseada = st.selectbox("Seleccione Aerolinia:", a)
        return aerolin
       
    def pedirDatosVuelo(self):
        codigo_de_vuelo = st.text_input("codigo de vuelo: ")
        origen = st.text_input("Origen: ")
        fecha = st.text_input("Fecha: ")
        destino = st.text_input("Destino: ")
        ans = st.button("Crear Vuelo", type="primary")
        if ans:
            return {
                "codigo de vuelo": codigo_de_vuelo,
                "Origen": origen,
                "Fecha": fecha,
                "Destino": destino
            }
    
    def elegirAeronave(self,c,b):
        AeroDeseada = st.selectbox("Seleccione Aeronave:", c)
        for i in range(len(b)):
            if	b[i] != None:
                if b[i].get_Codigo() == AeroDeseada:
                    x = b[i]
        return x
    
    
    def elegirVuelo(self, diccionario,aerolinia):
        vuelos = diccionario[aerolinia].getvuelos()
        lista = []
        for i in range(len(vuelos)):
            lista.append(vuelos[i].get_codigo_de_vuelo())
        vueloDeseado = st.selectbox("Seleccione Vuelo: ", lista)
        ans = st.button("Asignar", type="primary")
        if ans:
            return vueloDeseado
    @st.cache    
    def elegirVuelo2(self, diccionario,aerolinia):
        vuelos = diccionario[aerolinia].getvuelos()
        lista = []
        for i in range(len(vuelos)):
            lista.append(vuelos[i].get_codigo_de_vuelo())
        vueloDeseado = st.selectbox("Seleccione Vuelo: ", lista)
        return vueloDeseado
        
    def men(self, asignacion):
        if asignacion == False:
            st.info(f"La Aeronave no puede tener mas vuelos", icon="ℹ️")
        else:
            st.info(f"La asignacion fue exitosa")
    def mostrarPuertas(self, puertas):
        st.header("Puertas")
        p = []
        for puerta in puertas:
            if puerta is not None:
                p.append({
                    "Numero de identificacion": puerta.get_num_identificacion(),
                    "Ubicacion": puerta.get_ubicacion(),
                    "Hora de embarque": puerta.get_horaEmbarque(),
                })
        if p:
            st.table(p)
        else:
            st.info("No hay puertas creadas aún", icon="ℹ️")


    def mostrarVuelosEmpleado(self,vuelos):
        st.header("Vuelos")
        v = []
        for vuelo in vuelos:
            if vuelo is not None:
                v.append({
                    "codigo de vuelo": vuelo.codigo_de_vuelo,
                    "origen": vuelo.origen,
                    "fecha": vuelo.fecha,
                    "destino": vuelo.destino,
                })
        if v:
            st.table(v)
        else:
            st.info("No hay vuelos aun", icon="ℹ️")


    def asignarPuerta(self,id):
        option = st.selectbox("Seleccione puerta:" , id)
        return option

    def asignarVuelo(self,id):
        option = st.selectbox("Seleccione vuelo:", id)
        return option
    
    def mandarUbicaciones(self):
        ans = st.button("Mandar Ubicaciones", type ="primary")
        return ans
    
    def crearPuerta(self):
        num_identificacion = st.text_input("Numero de identificacion: ")
        ubicacion = st.text_input("Ubicacion: ")
        hora = st.text_input("Hora de embarque: ")
        ans = st.button("Crear Puerta", type="primary")
        if ans:
            return {
                "Numero de identificacion" : num_identificacion,
                "Ubicacion": ubicacion,
                "Hora de embarque": hora
            }
    
    def mostrarVuelosEmpleado(self,vuelos):
        st.header("Vuelos")
        v = []
        for vuelo in vuelos:
            if vuelo is not None:
                if vuelo.get_disponibilidad_vuelo():
                    v.append({
                        "codigo de vuelo": vuelo.codigo_de_vuelo,
                        "origen": vuelo.origen,
                        "fecha": vuelo.fecha,
                        "destino": vuelo.destino,
                    })
        if v:
            st.table(v)
        else:
            st.info("No hay vuelos aun", icon="ℹ️")
        
    def mostrarPuertas(self, puertas):
        st.header("Puertas")
        p = []
        for puerta in puertas:
            if puerta is not None:
                if puerta.get_disponibilidad():
                    p.append({
                        "Numero de identificacion": puerta.get_num_identificacion(),
                        "Ubicacion": puerta.get_ubicacion(),
                        "Hora de embarque": puerta.get_horaEmbarque(),
                    })
        if p:
            st.table(p)
        else:
            st.info("No hay puertas creadas aún", icon="ℹ️")
    
    def verUbicacionAeronave(self, aeronaves):
        x = None  # Inicializa x antes del bucle

        lista = []
        for i in range(len(aeronaves)):
            lista.append(aeronaves[i].get_Codigo())

        option = st.selectbox("Seleccione la Aeronave", lista)

        for i in range(len(aeronaves)):
            if option == aeronaves[i].get_Codigo():
                x = aeronaves[i]
        return x.get_Codigo()
    
    def mostrarAeronaves(self, aeronaves):
        st.header("Aeronaves")
        p = []
        for aeronave in aeronaves:
            if aeronave is not None:
                p.append({
                    "Codigo": aeronave.get_Codigo(),
                    "Marca": aeronave.get_marca(),
                    "Estado": aeronave.get_estado()
                })
        if p:
            st.table(p)
        else:
            st.info("No hay Aeronaves creadas aún", icon="ℹ️")
            
    def nombrePais(self):
        st.title("Información de Países")
        nombre_pais = st.text_input("Ingrese el nombre del país:")
        if st.button("Buscar"):
            return nombre_pais
        else:
            return None
   
    def pedir_datos_tripulante(self):
        cedula = st.text_input("Cédula: ")
        nombres = st.text_input("Nombres: ")
        apellidos = st.text_input("Apellidos: ")
        fecha_de_nacimiento = st.text_input("Fecha de nacimiento: ")
        genero = st.text_input("Género: ")
        direccion = st.text_input("Dirección: ")
        numero_de_telefono = st.text_input("Número de teléfono: ")
        correo_electronico = st.text_input("Correo electrónico: ")
        puesto = st.text_input("puesto: ")
        anos_experiencia = st.number_input("anos experiencia")
        horas_trabajo = st.text_input("horas_trabajo ")

        ans = st.button("Crear Tripulante", type="primary")

        if ans:
            return {
                "cedula": cedula,
                "nombres": nombres,
                "apellidos": apellidos,
                "fecha_de_nacimiento": fecha_de_nacimiento, 
                "genero": genero,
                "direccion": direccion,
                "numero_de_telefono": numero_de_telefono,
                "correo_electronico": correo_electronico,
                "puesto": puesto,
                "anos experiencia": anos_experiencia,
                "horas_trabajo": horas_trabajo
            }
    
    def elegirEstado(self):
        AeroDeseada = st.selectbox("Seleccione Estado:", ["En mantenimiento","Disponible","Totalmente asignada", "En puerta de embarque","En pista de despegue","En vuelo"])
        return AeroDeseada

    def elegir_Aeronave(self,codigos_id):
        Aeroele = st.selectbox("Seleccione Aeronave" , codigos_id)
        return Aeroele
    
    def verMensaje(self, msg):
        st.header("Ubicaciones")
        p = []
        for m in msg:
            if m is not None:
                p.append({
                    "Marca": m[0],
                    "Ubicacion": m[1]
                })
        if p:
            st.table(p)
        else:
            st.info("No hay ubicaciones enviadas aún", icon="ℹ️")