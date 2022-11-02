from Producto import *
from Usuario import *


class DetalleTemporal:

    def __init__(self, id_usuario:Usuario id_producto: Producto, cantidad: int, precio_venta: int, total:int):
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_venta = precio_venta
        self.total = total

    def get_id_usuario(self, id_usuario):
        return self.id_usuario
    def set_id_usuario(self, id_usuario:Usuario):
        self.id_usuario = id_usuario

    def get_id_producto(self, id_producto):
        return self.id_producto
    def set_id_poducto(self, id_producto:Producto):
        self.id_producto = id_producto

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self, cantidad:int):
        slef.cantidad = cantidad

    def get_precio_venta(self):
        return self.precio_venta
    def set_precio_venta(self, precio_venta:int):
        self.precio_venta = precio_venta

    def get_total(self):
        return self.total
    def set_total(self, total: int):
        self.total = total