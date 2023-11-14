from persona import Persona

class Tripulacion(Persona):
    def __init__(self, cedula=0, nombres="", apellidos="", fecha_nacimiento="", genero="", direccion="", numero_telefono=0,
                 correo_electronico="", puesto="", anos_experiencia=0, horas_trabajo=0):
        super().__init__(cedula, nombres, apellidos, fecha_nacimiento, genero, direccion, numero_telefono, correo_electronico)
        self.puesto = puesto
        self.anos_experiencia = anos_experiencia
        self.horas_trabajo = horas_trabajo

    def get_puesto(self):
        return self.puesto

    def get_anos_experiencia(self):
        return self.anos_experiencia

    def get_horas_trabajo(self):
        return self.horas_trabajo

    def imprimir_informacion(self):
        print("Cédula:", self.get_cedula())
        print("Nombres:", self.get_nombres())
        print("Apellidos:", self.get_apellidos())
        print("Fecha de Nacimiento:", self.get_fecha_nacimiento())
        print("Género:", self.get_genero())
        print("Dirección:", self.get_direccion())
        print("Número de Teléfono:", self.get_numero_telefono())
        print("Correo Electrónico:", self.get_correo_electronico())
        print("Puesto:", self.puesto)
        print("Experiencia en años:", self.anos_experiencia)
        print("Horas de trabajo:", self.horas_trabajo)
