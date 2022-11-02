from Producto import *
from Venta import *

class DetalleVenta:

    def __init__(self, id_producto: Producto, id_venta: Venta, cantidad: int, precio: int):
        self.id_producto = id_producto
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self, id_producto):
        return self.id_producto
    def set_id_poducto(self, id_producto:Producto):
        self.id_producto = id_producto

    def get_id_venta(self):
        return self.id_venta
    def set_id_venta(self, id_venta:Venta):
        self.id_venta = id_venta

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self, cantidad:int):
        slef.cantidad = cantidad

    def get_precio(self):
        return self.precio
    def set_precio(self, precio:int):
        self.precio = precio