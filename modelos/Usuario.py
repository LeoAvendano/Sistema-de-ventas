

class Usuario:

    def __init__(self, nombre:str, correo:str, usuario:str, clave:str, estado=1:int):
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.clave = clave
        self.estado = estado

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre:str):
        self.nombre = nombre

    def get_correo(self):
        return self.correo
    def set_correo(self, correo:str):
        self.correo = correo

    def get_usuario(self):
        return self.usuario;
    def set_usuario(self, usuario:str):
        self.usuario = usuario

    def get_clave(self):
        return self.clave
    def set_clave(self, clave:str):
        self.clave = clave

    def get_estado(self):
        return self.estado
    def set_estado(self, estado:int):
        self.estado = estado