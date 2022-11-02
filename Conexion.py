import pymysql

class Conexion:

    def __init__(self):
        pass

    def conectar(self):
        return pymysql.connect(
            host="localhost",
            port=2974,
            user="root",
            password="",
            db="sistema_ventas"
        )
