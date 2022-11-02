


class Cliente:

    def __init__(self, nombre:str, telefono:str, direccion:str, usuario_id:int, estado=1):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.usuario_id = usuario_id
        self.estado = estado

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre:str):
        self.nombre = nombre

    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono:str):
        self.telefono = telefono

    def get_usuario_id(self):
        return self.usuario_id;
    def set_usuario_id(self, usuario_id):int
        self.usuario_id = usuario_id

    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion:str):
        self.direccion = direccion

    def get_estado(self):
        return self.estado
    def set_estado(self, estado:int):
        self.estado = estado