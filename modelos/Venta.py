from Cliente import *
from Usuario import *


class Venta:

    def __init__(self, id_cliente: Cliente, total: int, id_usuario: Usuario, fecha: datetime):
        self.id_cliente = id_cliente
        self.total = total
        self.id_ususario = id_usuario
        self.fecha = fecha

    def get_id_cliente(self):
        return self.id_cliente
    def set_id_cliente(self, id_cliente:Cliente):
        self.id_cliente = id_cliente

    def get_total(self):
        return self.total
    def set_total(self, total:int):
        self.total = total

    def get_id_usuario(self):
        return self.id_ususario
    def set_id_usuario(self, id_usuario:Usuario):
        self.id_ususario = id_usuario

    def get_fecha(self):
        return self.fecha
    def set_fecha(self, fecha:datetime):
        self.fecha = fecha