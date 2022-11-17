import tkinter
from tkinter import *
from tkinter import messagebox
from Conexion import *
from Principal import *

import pymysql

class VentanaLogin():

    def __init__(self):
        pass

    def ventanaLogin(self):
        master = Tk()
        master.geometry("350x400")
        master.wm_title("Inicio de sesion")
        #self.master = master
        Label(text="INICIAR SESION", bg="navy", fg="white", width="100", height="3", font=("Calibri", 15)).pack()
        Label(text="").pack()
        global usuario_verify
        global password_verify
        usuario_verify = StringVar()
        password_verify = StringVar()
        global usuario_entry
        global password_entry
        Label(text="Usuario", font=("Calibri", 13)).pack()
        usuario_entry = Entry(master, width=25, font=("Calibri", 12), textvariable=usuario_verify)
        usuario_entry.pack()
        Label(master).pack()
        Label(text="Contraseña", font=("Calibri", 13)).pack()
        password_entry = Entry(master, show="*", width=25, font=("Calibri", 12), textvariable=password_verify)
        password_entry.pack()
        Label(master).pack()
        Label(master).pack()
        Button(master, text="Ingresar", height="2", width="15", font=("Calibri", 15), bg="BLUE",
               command=self.login).pack()
        master.mainloop()

    def create_widgets(self):
        pass

    def login(self):
        if self.validar_datos_login() == False:
            messagebox.showinfo(message="Faltan campos por rellenar", title="Aviso")
            return
        con = Conexion()
        bd = con.conectar()
        fcursor = bd.cursor()
        sql = "SELECT * FROM usuario " \
              "WHERE usuario = '" + usuario_verify.get() + "' and " \
                     "clave = '" + password_verify.get() + "' and " \
                     "estado = 1"
        try:
            fcursor.execute(sql)
            if (fcursor.fetchall()):
                #messagebox.showinfo(message="Usuario y contraseña correctos", title="Aviso")
                master
                self.iniciar_sesion()
                bd.commit()
            else:
                messagebox.showinfo(message="Usuario y/o contraseña incorrectos", title="Aviso")
                bd.rollback()
        except:
            bd.rollback()
            messagebox.showinfo(message="Fallo en la conexion...", title="Aviso")
        bd.close()

    def validar_datos_login(self):
        usuario = usuario_verify.get()
        passw = password_verify.get()
        return len(usuario) > 0 and len(passw) > 0

    def iniciar_sesion(self):
        pp = Principal()
        pp.ventana_principal()




def main():
    #root = Tk()
    #root.wm_title("Inicio de sesion")
    #app = VentanaLogin(root)
    app = VentanaLogin()
    app.mainloop()



