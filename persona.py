class Persona:
    def __init__(self, cedula, nombres, apellidos, fecha_de_nacimiento, genero, direccion, numero_de_telefono, correo_electronico):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.genero = genero
        self.direccion = direccion
        self.numero_de_telefono = numero_de_telefono
        self.correo_electronico = correo_electronico

    def get_cedula(self):
        return self.cedula

    def get_nombres(self):
        return self.nombres

    def get_apellidos(self):
        return self.apellidos

    def get_fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento

    def get_genero(self):
        return self.genero

    def get_direccion(self):
        return self.direccion

    def get_numero_de_telefono(self):
        return self.numero_de_telefono

    def get_correo_electronico(self):
        return self.correo_electronico
