from Usuario import *


class Producto:

    def __init__(self, codigo:int, descripcion:str, precio:int, existencia:int, usuario_id:Usuario, estado=1:int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.existencia = existencia
        self.usuario_id = usuario_id
        self.estado = estado

    def get_codigo(self):
        return self.codigo
    def set_codigo(self, codigo:int):
        self.codigo = codigo

    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion:str):
        self.descripcion = descripcion

    def get_precio(self):
        return self.precio
    def set_precio(self, precio:int):
        self.precio = precio

    def get_existencia(self):
        return self.existencia
    def set_existencia(self, existencia:int):
        self.existencia = existencia

    def get_usuario_id(self):
        return self.usuario_id;
    def set_usuario_id(self, usuario_id:Usuario):
        self.usuario_id = usuario_id

    def get_estado(self):
        return self.estado
    def set_estado(self, estado:int):
        self.estado = estado




