import pymysql

class Conexion:

    def __init__(self):
        self.bd = None

    def conectar(self, host:str, port:int, user:str, password:str, db:str):
        return pymysql.connect(host= host, port=port, user= user, password= password, db= db)