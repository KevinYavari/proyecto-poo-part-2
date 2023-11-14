from persona import Persona

class Pasajero(Persona):
    def __init__(self, cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, numero_de_telefono, correo_electronico, nacionalidad, maletas, info_medico):
        super().__init__(cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, numero_de_telefono, correo_electronico)
        self.nacionalidad = nacionalidad
        self.maletas = maletas
        self.info_medico = info_medico

    def imprimir_informacion(self):
        print("Cédula:", self.get_cedula())
        print("Nombres:", self.get_nombres())
        print("Apellidos:", self.get_apellidos())
        print("Fecha de Nacimiento:", self.get_fecha_de_nacimiento())
        print("Género:", self.get_genero())
        print("Dirección:", self.get_direccion())
        print("Número de Teléfono:", self.get_numero_de_telefono())
        print("Correo Electrónico:", self.get_correo_electronico())
        print("Nacionalidad:", self.nacionalidad)
        print("Número de Maletas:", self.maletas)
        print("Información Médica:", self.info_medico)

    def get_nacionalidad(self):
        return self.nacionalidad

    def get_maletas(self):
        return self.maletas

    def get_info_medico(self):
        return self.info_medico
